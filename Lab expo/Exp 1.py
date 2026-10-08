import heapq

def heuristic(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    pos = state.index(0)
    row = pos // 3
    col = pos % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)

            new_state[pos], new_state[new_pos] = \
                new_state[new_pos], new_state[pos]

            neighbors.append(tuple(new_state))

    return neighbors


def solve(start, goal):
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), 0, start, []))

    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [state])
                )

    return None


# Input
print("Enter the initial state (use 0 for blank):")
start = tuple(map(int, input().split()))

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = solve(start, goal)

if solution:
    print("\nSolution:")
    for state in solution:
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()
else:
    print("No solution found.")
