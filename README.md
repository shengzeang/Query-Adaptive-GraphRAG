# QA-GraphRAG: Query-Adaptive Plug-and-Play Retrieval Integration for Graph-based Retrieval-Augmented Generation

This repository contains the implementation of QA-GraphRAG based on RAPTOR in the paper *"QA-GraphRAG: Query-Adaptive Plug-and-Play Retrieval Integration for Graph-based Retrieval-Augmented Generation"*.

### Requirements

1. To install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

2. Please follow the official instruction [here](https://pytorch.org/get-started/locally/) to install PyTorch;

3. Download "hotpot_train.json" from [here](https://github.com/hotpotqa/hotpot), and put it under the "inputs" directory.

### Running

To run QA-GraphRAG (based on RAPTOR) on GraphRAG-Bench:

1. build tree for GraphRAG-Bench, the tree built will be under the root directory:

   ```bash
   python build_tree.py
   python merge_tree.py
   ```

2. generate training data for router and train the MLP-based router:

   ```bash
   python gen_train_hotpot.py
   python train_mlp.py
   ```

3. run evaluation on GraphRAG-Bench, results will be in sample_output.json:

   ```bash
   bash run_eval.sh
   ```
