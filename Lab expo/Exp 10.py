import heapq

def a_star(graph, heuristic, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], cost[goal]

        for neighbor, distance in graph[current]:
            new_cost = cost[current] + distance

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                f = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (f, neighbor))
                parent[neighbor] = current

    return None, -1


# Input
n = int(input("Enter number of nodes: "))

graph = {}

for i in range(n):
    node = input("Enter node: ")
    graph[node] = []

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v, w = input("Enter edge (from to cost): ").split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))

heuristic = {}

print("Enter heuristic values:")
for node in graph:
    heuristic[node] = int(input("h(" + node + ") = "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Best path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found")
