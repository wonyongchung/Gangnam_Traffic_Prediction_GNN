import node2vec
import numpy as np
import networkx as nx
from gensim.models import Word2Vec
import time

is_directed = True
p = 2
q = 1
num_walks = 100
# walk_length = 80
walk_length = [40, 160]
dimensions = 8
window_size = 10
epochs = 1000
Adj_file = 'data/link_data.txt'
# SE_file = 'data/SE.txt'

def read_graph(edgelist):
    G = nx.read_edgelist(
        edgelist, nodetype=int, data=(('weight',float),),
        create_using=nx.DiGraph())

    return G

def learn_embeddings(walks, dimensions, output_file):
    walks = [list(map(str, walk)) for walk in walks]
    model = Word2Vec(
        walks, vector_size = dimensions, window = 10, min_count=0, sg=1,
        workers = 8, epochs = epochs)
    model.wv.save_word2vec_format(output_file)
	
    return
    
nx_G = read_graph(Adj_file)
G = node2vec.Graph(nx_G, is_directed, p, q)
G.preprocess_transition_probs()
print('simulate walks')
print(time.time())
for walk_len in walk_length:
    SE_file = f'data/SE{walk_len}.txt'
    walks = G.simulate_walks(num_walks, walk_len)
    print('learn embeddings')
    print(time.time())
    learn_embeddings(walks, dimensions, SE_file)