# Node-Classification-on-ChainBlock

## Running the experiments ##

### Dataset and preprocessing ###

#### Download and preprocess the BlockChain data ####

```{bash}
python download_dataset.py 
```

```{bash}
python txt_to_csv.py 
```

```{bash}
python process.py 
```

### Requirements

* python >= 3.7

* Dependency

```{bash}
pandas==0.24.2
torch==1.1.0
tqdm==4.41.1
numpy==1.16.4
scikit_learn==0.22.1
networkx==2.5.1
wget==3.2
```

### Command and configurations

#### Sample commend

* Learning the network using link prediction tasks
```{bash}
# t-gat learning on MulDiGraph data
python -u learn_edge.py -d eth_graph --bs 200 --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 2 --prefix hello_world
```

* Learning node-classification(you have to 'learn link prediction tasks' before this command)


```{bash}
# on MulDiGraph
python -u learn_node.py -d eth_graph --bs 100 --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 2 --prefix hello_world
```

