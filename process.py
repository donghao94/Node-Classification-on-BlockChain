import json
import numpy as np
import pandas as pd

def preprocess(data_name):
    u_list, i_list, ts_list, label_list = [], [], [], []
    feat_l = []
    idx_list = []
    
    with open(data_name) as f:
        s = next(f)
        print(s)
        for idx, line in enumerate(f):
            e = line.strip().split(',')
            u = int(e[0])
            i = int(e[1])
            
            
            
            ts = float(e[2])
            label = int(e[3])
            
            feat = np.array([float(x) for x in e[4:]])  # feat = np.array([float(x) for x in e[4:]])
            
            u_list.append(u)
            i_list.append(i)
            ts_list.append(ts)
            label_list.append(label)
            idx_list.append(idx)
            
            feat_l.append(feat)
    return pd.DataFrame({'u': u_list, 
                         'i': i_list,
                         'ts': ts_list,
                         'label': label_list,   # label of user
                         'idx': idx_list}), np.array(feat_l)



def reindex(df):
    assert(df.u.max() - df.u.min() + 1 == len(df.u.unique()))  # 要求U，i必须是连续的可重复的整数，e.g. 1,2，2,3,4,5
    assert(df.i.max() - df.i.min() + 1 == len(df.i.unique()))  # 反例 1，2，2，3，4，6
    
    upper_u = df.u.max() + 1
    new_i = df.i + upper_u
    
    new_df = df.copy()
    print(new_df.u.max())
    print(new_df.i.max())
    
    new_df.i = new_i
    new_df.u += 1
    new_df.i += 1
    new_df.idx += 1
    
    print(new_df.u.max())
    print(new_df.i.max())
    
    return new_df



def run(data_name):
    PATH = './processed/{}.csv'.format(data_name)
    OUT_DF = './processed/ml_{}.csv'.format(data_name)
    OUT_FEAT = './processed/ml_{}.npy'.format(data_name)
    OUT_NODE_FEAT = './processed/ml_{}_node.npy'.format(data_name)
    
    df, feat = preprocess(PATH)
    new_df = reindex(df)  ############### new_df = reindex(df)
    new_df.idx += 1

    print(feat.shape)
    empty = np.zeros(feat.shape[1])[np.newaxis, :]  # shape为（1，feat.shape[1]）
    feat = np.vstack([empty, feat])  # shape为（feat.shape[0]+1， feat.shape[1]）
    
    # max_idx = max(new_df.u.max(), new_df.i.max())
    rand_feat = np.zeros((feat.shape[0], feat.shape[1]))  # rand_feat = np.zeros((max_idx + 1, feat.shape[1]))
    
    print(feat.shape)
    new_df.to_csv(OUT_DF)
    np.save(OUT_FEAT, feat)  # edge_features （不全是零）
    np.save(OUT_NODE_FEAT, rand_feat)  # node_features（零矩阵）
    
    
#run('wikipedia')
#run('graph_eg')
run('eth_graph')
#run('wikipedia_eg')
#run('reddit')
