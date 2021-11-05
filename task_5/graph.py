import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import os

def generate_table(count_vert, count_edge):
    table = np.zeros((count_vert, count_vert))
    i = 0
    while i < count_edge:
        a = random.randint(0, count_vert - 1)
        b = random.randint(0, count_vert - 1)
        if a != b and table[a][b] != 1:
            table[a][b] = 1
            table[b][a] = 1
            i += 1

    return table

def dfs(points, keys, visited):
    for i in keys:
        if i in visited:
            continue
        visited.append(i)
        # keys_n = points[i]
        visited = dfs(points, points[i], visited)
    return visited

def bfs(points, a, b):
    need = [a]
    visited = []
    flag = [1]
    path = 0
    while len(need) != 0:
        node = need.pop(0)
        flag[0] -= 1
        fl = flag[0]
        if flag[0] == 0:
            flag.pop(0)
        if node in visited:
            continue
        if node == b:
            return path
        need.extend(points[node])
        flag.append(len(points[node]))
        visited.append(node)
        if fl == 0:
            path += 1
    return path - 1



if __name__ == "__main__":
    count_vert = 100
    count_edge = 200

    table = generate_table(count_vert, count_edge)

    lst = {}

    grph = nx.Graph()

    edges = []

    for i in range(len(table)):
        ik = []
        for j in range(len(table)):
            # print(i, j)
            if table[i][j] == 1:
                ik.append(j + 1)
                edges.append((i+1, j+1))
                edges.append((j+1, i+1))

        lst[i+1] = ik

    print(table[:10, :])
    n = 10
    for key in lst.keys():
        if key == n + 1:
            break
        print(key, lst[key])

    grph.add_edges_from(edges)


    pos = nx.spring_layout(grph)
    # nx.draw(grph)
    nx.draw_networkx_nodes(grph, pos)
    nx.draw_networkx_labels(grph, pos)
    nx.draw_networkx_edges(grph, pos)
    pth = os.getcwd()
    plt.savefig(pth + '\\' +'graph.png')
    plt.show()



    visited = []
    count_comp = 0
    check = False
    a = random.randint(1, count_vert)
    b = random.randint(1, count_vert)
    print("Связные компоненты")
    for i in lst.keys():
        if i in visited:
            continue
        vis = []
        vis = dfs(lst, [i], vis)
        print(vis)
        if a in vis and b in vis:
            check = True
        visited.extend(vis)
        count_comp += 1
    
    print("Кол-во связных компонент: ", count_comp)

    if check:
        pth = bfs(lst, a, b)
        print("Минимальный путь между точками", a, b, "равен", pth)
    else:
        print("Между точками", a, b, "нет пути")