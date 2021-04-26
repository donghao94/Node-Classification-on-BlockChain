import pandas as pd
import networkx as nx
import pickle
import numpy as np

# read address_label.txt
addresses_label = []
address_label = pd.read_csv('./dataset/address_label.txt', header=None, sep=' ')
address_label.columns = ['address', 'label']

# read eth_graph.txt
graph = []
graph = pd.read_csv('./dataset/eth_graph.txt', header=None, sep=' ')
graph.columns = ['from', 'to', 'value', 'timestamp']

# encode from_address
from_addr = graph.drop(columns=['to', 'value', 'timestamp']).drop_duplicates('from')
from_addrID = np.array(range(len(from_addr))).reshape(len(from_addr),1)
from_addr.insert(0, 'from_addrID', from_addrID)
from_addr.columns = ['from_addrID', 'address']

# encode to_address
to_addr = graph.drop(columns=['from', 'value', 'timestamp']).drop_duplicates('to')
to_addrID = np.array(range(len(to_addr))).reshape(len(to_addr),1)
to_addr.insert(0, 'to_addrID', to_addrID)
to_addr.columns = ['to_addrID', 'address']

# labeled from_address
graph.columns = ['address', 'to', 'value', 'timestamp']
from_labeled_graph = pd.merge(graph, address_label, how='inner', on=['address'])

# merge addressID
from_addrID_labeled = pd.merge(from_labeled_graph, from_addr, how='inner', on=['address']).drop(columns=['address'])
from_addrID_labeled.columns = ['address', 'value', 'timestamp', 'label', 'from_addrID']
to_addrID_labeled = pd.merge(from_addrID_labeled, to_addr, how='inner', on=['address'])
labeled_graph = to_addrID_labeled.drop(columns=['address'])
labeled_graph = labeled_graph[['from_addrID', 'to_addrID', 'timestamp', 'label', 'value']]
labeled_graph.columns = ['from', 'to', 'timestamp', 'label', 'value']

labeled_graph.to_csv('./processed/eth_graph.csv', index=False)
print('csv saved')
