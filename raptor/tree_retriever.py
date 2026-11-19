import logging
import os
import threading
from typing import Dict, List, Set

import numpy as np
import tiktoken
from tenacity import retry, stop_after_attempt, wait_random_exponential

from .EmbeddingModels import BaseEmbeddingModel, OpenAIEmbeddingModel
from .Retrievers import BaseRetriever
from .tree_structures import Node, Tree
from .utils import (SEGMENTS_SUFFIX, cosine_distances,
                    distances_to_nearest_segment, get_children, get_embeddings,
                    get_node_list, get_text,
                    indices_of_nearest_neighbors_from_distances,
                    reverse_mapping)

# logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.ERROR)


class TreeRetrieverConfig:
    def __init__(
        self,
        tokenizer=None,
        threshold=None,
        top_k=None,
        selection_mode=None,
        context_embedding_model=None,
        embedding_model=None,
        num_layers=None,
        start_layer=None,
    ):
        if tokenizer is None:
            tokenizer = tiktoken.get_encoding("cl100k_base")
        self.tokenizer = tokenizer

        if threshold is None:
            threshold = 0.5
        if not isinstance(threshold, float) or not (0 <= threshold <= 1):
            raise ValueError("threshold must be a float between 0 and 1")
        self.threshold = threshold

        if top_k is None:
            top_k = 5
        if not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be an integer and at least 1")
        self.top_k = top_k

        if selection_mode is None:
            selection_mode = "top_k"
        if not isinstance(selection_mode, str) or selection_mode not in [
            "top_k",
            "threshold",
        ]:
            raise ValueError(
                "selection_mode must be a string and either 'top_k' or 'threshold'"
            )
        self.selection_mode = selection_mode

        if context_embedding_model is None:
            context_embedding_model = "OpenAI"
        if not isinstance(context_embedding_model, str):
            raise ValueError("context_embedding_model must be a string")
        self.context_embedding_model = context_embedding_model

        if embedding_model is None:
            embedding_model = OpenAIEmbeddingModel()
        if not isinstance(embedding_model, BaseEmbeddingModel):
            raise ValueError(
                "embedding_model must be an instance of BaseEmbeddingModel"
            )
        self.embedding_model = embedding_model

        if num_layers is not None:
            if not isinstance(num_layers, int) or num_layers < 0:
                raise ValueError("num_layers must be an integer and at least 0")
        self.num_layers = num_layers

        if start_layer is not None:
            if not isinstance(start_layer, int) or start_layer < 0:
                raise ValueError("start_layer must be an integer and at least 0")
        self.start_layer = start_layer

    def log_config(self):
        config_log = """
        TreeRetrieverConfig:
            Tokenizer: {tokenizer}
            Threshold: {threshold}
            Top K: {top_k}
            Selection Mode: {selection_mode}
            Context Embedding Model: {context_embedding_model}
            Embedding Model: {embedding_model}
            Num Layers: {num_layers}
            Start Layer: {start_layer}
        """.format(
            tokenizer=self.tokenizer,
            threshold=self.threshold,
            top_k=self.top_k,
            selection_mode=self.selection_mode,
            context_embedding_model=self.context_embedding_model,
            embedding_model=self.embedding_model,
            num_layers=self.num_layers,
            start_layer=self.start_layer,
        )
        return config_log


class TreeRetriever(BaseRetriever):

    # A layer (or pool) of at least this many nodes is ranked with the matrix of the whole tree (see ``_distances_via_matrix``);
    # shorter ones are stacked on the fly, which is cheaper than a product over every node of the tree.
    LARGE_LAYER = 4096

    def __init__(self, config, tree) -> None:
        if not isinstance(tree, Tree):
            raise ValueError("tree must be an instance of Tree")

        if config.num_layers is not None and config.num_layers > tree.num_layers + 1:
            raise ValueError(
                "num_layers in config must be less than or equal to tree.num_layers + 1"
            )

        if config.start_layer is not None and config.start_layer > tree.num_layers:
            raise ValueError(
                "start_layer in config must be less than or equal to tree.num_layers"
            )

        self.tree = tree
        self.num_layers = (
            config.num_layers if config.num_layers is not None else tree.num_layers + 1
        )
        self.start_layer = (
            config.start_layer if config.start_layer is not None else tree.num_layers
        )

        if self.num_layers > self.start_layer + 1:
            raise ValueError("num_layers must be less than or equal to start_layer + 1")

        self.tokenizer = config.tokenizer
        self.top_k = config.top_k
        self.threshold = config.threshold
        self.selection_mode = config.selection_mode
        self.embedding_model = config.embedding_model
        self.context_embedding_model = config.context_embedding_model

        self.tree_node_index_to_layer = reverse_mapping(self.tree.layer_to_nodes)
        self._matrix_lock = threading.Lock()
        self._matrix = None
        self._all_node_list = None

        logging.info(
            f"Successfully initialized TreeRetriever with Config {config.log_config()}"
        )

    def create_embedding(self, text: str) -> List[float]:
        """
        Generates embeddings for the given text using the specified embedding model.

        Args:
            text (str): The text for which to generate embeddings.

        Returns:
            List[float]: The generated embeddings.
        """
        return self.embedding_model.create_embedding(text)

    def node_distances(self, query_embedding, node_list: List[Node]):
        """Distances of the query to the nodes. A node with embeddings of several windows of its text (a text longer than
        the encoder reads) is as close as its closest window; if no node has them this is the plain cosine distance.

        The embeddings are assumed not to change after the first query: a large layer is ranked with a matrix of the whole
        tree that is built once (build a new ``TreeRetriever`` after editing the embeddings of a tree)."""
        if len(node_list) >= self.LARGE_LAYER:
            distances = self._distances_via_matrix(query_embedding, node_list)
            if distances is not None:
                return distances
        key = self.context_embedding_model
        if not any(key + SEGMENTS_SUFFIX in n.embeddings for n in node_list):
            return cosine_distances(query_embedding, get_embeddings(node_list, key))
        return distances_to_nearest_segment(
            query_embedding, [n.embeddings.get(key + SEGMENTS_SUFFIX, n.embeddings[key]) for n in node_list]
        )

    def _embedding_matrix(self):
        """``(rows, starts, position)`` of the whole tree, built once: ``rows`` are the unit-length float32 embeddings (all
        windows of a node next to each other), ``starts[i]`` the first row of the i-th node (by index) and ``position`` maps
        a node index to ``i`` (-1: not in the tree)."""
        if self._matrix is None:
            with self._matrix_lock:
                if self._matrix is None:
                    key = self.context_embedding_model
                    nodes = self._nodes_of_tree()
                    parts = [np.atleast_2d(np.asarray(n.embeddings.get(key + SEGMENTS_SUFFIX, n.embeddings[key]),
                                                      dtype=np.float32)) for n in nodes]
                    lengths = np.fromiter((len(p) for p in parts), dtype=np.int64, count=len(parts))
                    rows = np.concatenate(parts)
                    norms = np.linalg.norm(rows, axis=1, keepdims=True)
                    rows /= np.where(norms > 0, norms, 1.0)
                    position = np.full(max(n.index for n in nodes) + 1, -1, dtype=np.int64)
                    position[[n.index for n in nodes]] = np.arange(len(nodes))
                    self._matrix = (rows, np.cumsum(lengths) - lengths, position, bool((lengths != 1).any()))
        return self._matrix

    def _nodes_of_tree(self) -> List[Node]:
        """Every node of the tree sorted by index (built once)."""
        if self._all_node_list is None:
            self._all_node_list = get_node_list(self.tree.all_nodes)
        return self._all_node_list

    def _distances_via_matrix(self, query_embedding, node_list: List[Node]):
        """Cosine distances (best window for a node with several) of a large layer: one matrix-vector product with every
        embedding of the tree, then the rows of the layer are picked. numpy releases the GIL in it, and it costs the
        same few milliseconds whichever layer is ranked, instead of one Python call per node. float32, so the ranking can
        differ from the float64 computation only between distances that agree to about 1e-6. ``None``: not applicable."""
        rows, starts, position, has_windows = self._embedding_matrix()
        index = np.fromiter((n.index for n in node_list), dtype=np.int64, count=len(node_list))
        if index.size == 0 or index.max() >= len(position) or (position[index] < 0).any():
            return None                                                # a node that is not part of this tree
        q = np.asarray(query_embedding, dtype=np.float32).ravel()
        q = q / (np.linalg.norm(q) or 1.0)
        sims = np.einsum("ij,j->i", rows, q)
        best = np.maximum.reduceat(sims, starts) if has_windows else sims
        return 1.0 - best[position[index]]

    def retrieve_information_collapse_tree(self, query: str, top_k: int, max_tokens: int, node_list=None) -> str:
        """
        Retrieves the most relevant information from the tree based on the query.

        Args:
            query (str): The query text.
            max_tokens (int): The maximum number of tokens.
            node_list (List[Node], optional): The nodes to rank (default: every node of the tree).

        Returns:
            str: The context created using the most relevant nodes.
        """

        query_embedding = self.create_embedding(query)

        selected_nodes = []

        if node_list is None:
            node_list = self._nodes_of_tree()

        distances = self.node_distances(query_embedding, node_list)

        indices = indices_of_nearest_neighbors_from_distances(distances)

        total_tokens = 0
        for idx in indices[:top_k]:

            node = node_list[idx]
            node_tokens = len(self.tokenizer.encode(node.text))

            if total_tokens + node_tokens > max_tokens:
                break

            selected_nodes.append(node)
            total_tokens += node_tokens

        context = get_text(selected_nodes)
        return selected_nodes, context

    def retrieve_information(
        self,
        current_nodes: List[Node],
        query: str,
        num_layers: int,
        max_tokens: int = None,
    ) -> str:
        """
        Retrieves the most relevant information from the tree based on the query.

        Args:
            current_nodes (List[Node]): A List of the current nodes.
            query (str): The query text.
            num_layers (int): The number of layers to traverse.
            max_tokens (int, optional): Token budget of the returned context. Nodes are
                kept in retrieval order (start layer first) until the budget is used up.

        Returns:
            str: The context created using the most relevant nodes.
        """

        query_embedding = self.create_embedding(query)

        selected_nodes = []

        node_list = current_nodes

        for layer in range(num_layers):

            distances = self.node_distances(query_embedding, node_list)

            indices = indices_of_nearest_neighbors_from_distances(distances)

            if self.selection_mode == "threshold":
                best_indices = [
                    index for index in indices if distances[index] > self.threshold
                ]

            elif self.selection_mode == "top_k":
                best_indices = indices[: self.top_k]

            nodes_to_add = [node_list[idx] for idx in best_indices]

            selected_nodes.extend(nodes_to_add)

            if layer != num_layers - 1:

                child_nodes = []

                for index in best_indices:
                    child_nodes.extend(node_list[index].children)

                # take the unique values
                child_nodes = list(dict.fromkeys(child_nodes))
                node_list = [self.tree.all_nodes[i] for i in child_nodes]

        if max_tokens is not None:
            kept, total_tokens = [], 0
            for node in selected_nodes:
                node_tokens = len(self.tokenizer.encode(node.text))
                if kept and total_tokens + node_tokens > max_tokens:
                    break
                kept.append(node)
                total_tokens += node_tokens
            selected_nodes = kept

        context = get_text(selected_nodes)
        return selected_nodes, context

    def retrieve(
        self,
        query: str,
        start_layer: int = None,
        num_layers: int = None,
        top_k: int = 10,
        max_tokens: int = 3500,
        collapse_tree: bool = True,
        return_layer_information: bool = False,
    ) -> str:
        """
        Queries the tree and returns the most relevant information.

        Args:
            query (str): The query text.
            start_layer (int): The layer to start from. Defaults to self.start_layer.
            num_layers (int): The number of layers to traverse. Defaults to self.num_layers.
            max_tokens (int): The maximum number of tokens. Defaults to 3500.
            collapse_tree (bool): Whether to retrieve information from all nodes. Defaults to False.

        Returns:
            str: The result of the query.
        """

        if not isinstance(query, str):
            raise ValueError("query must be a string")

        if not isinstance(max_tokens, int) or max_tokens < 1:
            raise ValueError("max_tokens must be an integer and at least 1")

        if not isinstance(collapse_tree, bool):
            raise ValueError("collapse_tree must be a boolean")

        # Set defaults
        start_layer = self.start_layer if start_layer is None else start_layer
        num_layers = self.num_layers if num_layers is None else num_layers

        if not isinstance(start_layer, int) or not (
            0 <= start_layer <= self.tree.num_layers
        ):
            raise ValueError(
                "start_layer must be an integer between 0 and tree.num_layers"
            )

        if not isinstance(num_layers, int) or num_layers < 1:
            raise ValueError("num_layers must be an integer and at least 1")

        if num_layers > (start_layer + 1):
            raise ValueError("num_layers must be less than or equal to start_layer + 1")

        if collapse_tree:
            logging.info(f"Using collapsed_tree")
            selected_nodes, context = self.retrieve_information_collapse_tree(
                query, top_k, max_tokens
            )
        else:
            layer_nodes = self.tree.layer_to_nodes[start_layer]
            selected_nodes, context = self.retrieve_information(
                layer_nodes, query, num_layers, max_tokens
            )

        if return_layer_information:

            layer_information = []

            for node in selected_nodes:
                layer_information.append(
                    {
                        "node_index": node.index,
                        "layer_number": self.tree_node_index_to_layer[node.index],
                    }
                )

            return context, layer_information

        return context
