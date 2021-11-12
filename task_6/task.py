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

def generate_grid(n, m, count_walls):
    table = np.ones((n, m))
    i = 0
    while i <= count_walls:
        gor = random.randint(0, n - 1)
        vert =  random.randint(0, m - 1)
        if table[gor][vert] != 0:
            table[gor][vert] = 0
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


    grid = generate_grid(10, 20, 40)
    nodes = {}
    edgs = []

    a = 0
    b = 0
    i = 0

    for a in range(10):
        for b in range(20):
            if grid[a][b] == 0:
                continue
            if a == 0 and b == 19:
                source = i
            if a == 9 and b == 0:
                target = i
            nodes[i] = (a, b)
            i += 1

    for nd1 in nodes.keys():
        for nd2 in nodes.keys():
            if nd1 == nd2:
                continue
            if nodes[nd1][0] == nodes[nd1][0] and abs(nodes[nd1][1] - nodes[nd2][1]) == 1:
                edgs.append((nd1, nd2))
            if nodes[nd1][1] == nodes[nd1][1] and abs(nodes[nd1][0] - nodes[nd2][0]) == 1:
                edgs.append((nd1, nd2))

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
