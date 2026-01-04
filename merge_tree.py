from typing import List
from raptor.tree_structures import Tree
from raptor.tree_builder import merge_trees
import os
import pickle

def load_trees_from_dir(dir_path: str) -> List[Tree]:
    """
    Load all tree files from the specified directory.
    """
    trees = []
    for fname in os.listdir(dir_path):
        if fname.startswith('graphrag'):
            with open(os.path.join(dir_path, fname), 'rb') as f:
                tree = pickle.load(f)
                trees.append(tree)
    return trees


def save_tree(tree: Tree, out_path: str):
    """
    Save the merged large tree to the specified path.
    """
    with open(out_path, 'wb') as f:
        pickle.dump(tree, f)


def merge_trees_in_dir(dir_path: str, out_path: str):
    """
    Load all trees in the directory, merge them, and save to out_path.
    """
    trees = load_trees_from_dir(dir_path)
    if not trees:
        raise ValueError('No file under the directory.')
    merged_tree = merge_trees(trees)
    save_tree(merged_tree, out_path)
    print(f"Merge completed, saved to {out_path}")

if __name__ == "__main__":
    dir_path = "./trees/"
    out_path = "./sum_tree.pkl"
    merge_trees_in_dir(dir_path, out_path)
