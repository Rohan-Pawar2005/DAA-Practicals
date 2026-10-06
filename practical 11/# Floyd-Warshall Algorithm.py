# Floyd-Warshall Algorithm

V = 4
INF = 99999


def floyd_warshall(graph):

    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):

                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    print("Shortest Distance Matrix:")

    for i in range(V):
        for j in range(V):

            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")

        print()

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

floyd_warshall(graph)