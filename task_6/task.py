import numpy as np
import random
from algorithms import *
import networkx as nx
import time
import matplotlib.pyplot as plt


def generate_table(count_vert, count_edge):
    table = np.zeros((count_vert, count_vert))
    i = 0
    while i <= count_edge:
        a = random.randint(0, count_vert - 1)
        b = random.randint(0, count_vert - 1)
        if a != b and table[a][b] != 1:
            len_pth = random.randint(0, 100)
            table[a][b] = len_pth
            table[b][a] = len_pth
            i += 1
    return table

if __name__ == "__main__":
    count_vert = 100
    count_edge = 500

    tbl = generate_table(count_vert, count_edge)

    edges = {vert: {} for vert in list(range(count_vert))}
    cons = []
    

    for i in range(len(tbl)):
        for j in range(len(tbl)):
            if tbl[i][j] != 0:
                edges[i][j] = tbl[i][j]
                # edges[j][i] = tbl[i][j]
                cons.append((i, j, tbl[i][j]))
                cons.append((j, i, tbl[i][j]))

    # res = DA(edges, 0, 3)
    # print(res)

    graph = nx.Graph()
    graph.add_nodes_from(list(range(count_vert)))
    graph.add_weighted_edges_from(cons)

    task1_result = task1(graph)
    print(task1_result)

    grph2 =  nx.generators.lattice.grid_graph([20,10])
    i = 0
    while i <= 40:
        idx = random.randint(0, len(grph2.edges) - 1)
        if len(list(grph2.edges(data=True))[idx][-1]) == 0:
            list(grph2.edges(data=True))[idx][-1]['weight'] = 10000000
            i += 1

    for edge in range(len(grph2.edges)):
        if len(list(grph2.edges(data=True))[edge][-1]) == 0:
            list(grph2.edges(data=True))[edge][-1]['weight'] = 1    

    task2(grph2)  
