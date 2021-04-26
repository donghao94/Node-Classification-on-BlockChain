import pandas as pd
import networkx as nx


rawdata = pd.read_pickle('./dataset/MulDiGraph.pkl')

with open('./dataset/address_label.txt', 'w') as f:
    for idx, nd in enumerate(nx.nodes(rawdata)):
        data = str(nd)+' '+str(rawdata.nodes[nd]['isp']) + '\n'
        f.writelines(data)

with open('./dataset/eth_graph.txt', 'w') as f:
    for ind, edge in enumerate(nx.edges(rawdata)):
        (u, v) = edge
        eg = rawdata[u][v][0]
        amo, tim = eg['amount'], eg['timestamp']
        data = str(u)+' '+str(v)+' '+str(amo)+' '+str(int(tim))+'\n'
        f.writelines(data)
