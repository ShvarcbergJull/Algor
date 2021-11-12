import numpy as np
import time
import networkx as nx
import random

# def DA(svz, from_node, to_node):
#     print(svz)
#     visited = {}
#     unvisited = {node: np.nan for node in svz.keys()}
#     curent_node = from_node
#     cur_dist = 0
#     unvisited[curent_node] = cur_dist
#     while True:
#         print(visited)
#         for neigh, dist in svz[curent_node].items():
#             newdist = dist + cur_dist
#             if not neigh in unvisited:
#                 continue 
#             if np.isnan(unvisited[neigh]) or unvisited[neigh] > newdist:
#                 unvisited[neigh] = newdist
#         # print(unvisited)
#         visited[curent_node] = cur_dist
#         del unvisited[curent_node]
#         if not unvisited:
#             break
#         fut = [node for node in unvisited.items() if not np.isnan(node[1])]
#         if len(fut) == 0:
#             break
#         curent_node, cur_dist = sorted(fut, key = lambda x: x[1])[0]
#     return visited[to_node]

def task1(graph):
    times = [[], []]
    for i in range(10):
        tm = time.perf_counter()
        da = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(graph, 0)
        times[0].append(time.perf_counter() - tm)
        # print(da[0])

        tm = time.perf_counter()
        bf = nx.bellman_ford_predecessor_and_distance(graph, 0)
        times[1].append(time.perf_counter())
        # print(sbf[1])

    return sum(times[0]) / len(times[0]), sum(times[1]) / len(times[1])


def task2(graph):
    for i in range(5):
        source = random.randint(0, len(graph.nodes))
        target = random.randint(0, len(graph.nodes))

        astar = nx.astar_path(graph, list(graph.nodes)[source], list(graph.nodes)[target])

        print(i, list(graph.nodes)[source], list(graph.nodes)[target], astar)

