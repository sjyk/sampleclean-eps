import numpy as np
import scipy as sp
import matplotlib as mplot
import networkx as nx
import random

import logging

def cc(input_graph):
    """
    It does correlation clustering
    """
    G = input_graph.copy()
    clusters = []
    while G.nodes():
        v = random.choice(G.nodes())
        v_cluster = [v]
        for u in G.neighbors_iter(v):
            if G[u][v]['weight'] == 1:
                v_cluster.append(u)
        G.remove_nodes_from(v_cluster)
        clusters.append(v_cluster)
    return clusters

if __name__=="__main__":
    G = nx.Graph()
    G.add_edges_from([(1,2), (2,3), (4,5), ("hi", "there")], weight=1)
    G.add_edges_from([(1,4), (4,"hi"), ("hi", "there")], weight=-1)
    clusters = cc(G)
    print clusters
