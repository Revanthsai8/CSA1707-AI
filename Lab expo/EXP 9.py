from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the distance matrix:")
dist = []

for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

start = 0
cities = list(range(1, n))

min_cost = float('inf')
best_path = None

for p in permutations(cities):
    path = [start] + list(p) + [start]
    cost = 0

    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Minimum cost:", min_cost)
print("Best path:", end=" ")

for city in best_path:
    print(city, end=" ")
