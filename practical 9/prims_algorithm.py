import sys

V = 5


def prim(graph):

    parent = [-1] * V
    key = [sys.maxsize] * V
    mstSet = [False] * V

    key[0] = 0

    for count in range(V - 1):

        minimum = sys.maxsize
        u = -1

        for v in range(V):
            if not mstSet[v] and key[v] < minimum:
                minimum = key[v]
                u = v

        mstSet[u] = True

        for v in range(V):
            if (graph[u][v] != 0 and
                    not mstSet[v] and
                    graph[u][v] < key[v]):

                parent[v] = u
                key[v] = graph[u][v]

    print("Edges of Minimum Spanning Tree:")
    print("Edge\tWeight")

    total = 0

    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
        total += graph[i][parent[i]]

    print("Total Minimum Cost =", total)


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph)