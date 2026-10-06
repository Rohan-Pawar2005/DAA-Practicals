# Kruskal's Algorithm
def find_parent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_set(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)

    if u != v:
        parent[v] = u

def kruskal(edges, V, E):

    # Sort edges according to weight
    edges.sort(key=lambda edge: edge[2])

    parent = [i for i in range(V)]

    total_cost = 0
    edge_count = 0

    print("Edges in Minimum Spanning Tree:")

    for i in range(E):

        if edge_count == V - 1:
            break

        u = edges[i][0]
        v = edges[i][1]
        weight = edges[i][2]

        if find_parent(parent, u) != find_parent(parent, v):

            print(u, "-", v, ":", weight)

            total_cost += weight
            edge_count += 1

            union_set(parent, u, v)

    print("Total Minimum Cost =", total_cost)

V = 5
E = 7

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

kruskal(edges, V, E)