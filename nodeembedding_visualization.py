from random import sample
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualization(sedata, nodedata, samplenum):
    SE = pd.read_csv(f'data/{sedata}', sep=' ', header=0)
    node_idx = pd.read_csv(f'data/{nodedata}', index_col=[0])

    node_randomsample = SE.sample(n = samplenum)

    pca = PCA(n_components=2)
    x = np.array(node_randomsample)
    pcanode = pca.fit_transform(x)
    pcaarray = np.hstack((np.array(node_randomsample.index).reshape(-1,1), pcanode))
    pcadataframe = pd.DataFrame(pcaarray)
    pcadataframe["name"] = ""
    for i in range(len(pcadataframe)):
        pcadataframe.iloc[i, 3] = node_idx.iloc[int(pcadataframe[0][i]), :]['0']
        
    plt.rc('font', family='Malgun Gothic')
            
    plt.figure(figsize=(20,20))
    y = np.array(pcadataframe[2])
    x = np.array(pcadataframe[1])
    # z = np.array(pcadataframe[3])
    n = np.array(pcadataframe["name"])

    fig, ax = plt.subplots()
    # ax = fig.gca(projection='3d')
    ax.scatter(x, y,s = 3)

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]), fontsize = 7)
    plt.savefig(f'data/{sedata[:-4]}_{samplenum}.png')
    plt.show()

    
sedata = "SE160.txt"
nodedata = "node_idx.csv"
samplenum = 30
visualization(sedata, nodedata, samplenum)