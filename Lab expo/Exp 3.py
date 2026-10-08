from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque()
    visited = set()

    # Initial state
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        print(jug1, jug2)

        # Check whether target is reached
        if jug1 == target or jug2 == target:
            print("Target reached!")
            return

        # Possible operations
        states = [
            (capacity1, jug2),  # Fill Jug 1
            (jug1, capacity2),  # Fill Jug 2
            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2
            (0, jug1 + jug2) if jug1 + jug2 <= capacity2
            else (jug1 - (capacity2 - jug2), capacity2),  # Jug 1 -> Jug 2
            (jug1 + jug2, 0) if jug1 + jug2 <= capacity1
            else (capacity1, jug2 - (capacity1 - jug1))   # Jug 2 -> Jug 1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Target cannot be reached.")


# Input
capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(capacity1, capacity2, target)
