# Travelling Salesman Problem (TSP)

from itertools import permutations

V = 4
INF = 99999


def tsp(graph):

    cities = [i for i in range(1, V)]

    min_cost = INF

    for route in permutations(cities):

        current_cost = 0
        current_city = 0

        for city in route:
            current_cost += graph[current_city][city]
            current_city = city

        current_cost += graph[current_city][0]

        min_cost = min(min_cost, current_cost)

    return min_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp(graph)

print("Minimum Cost of Travelling Salesman =", result)