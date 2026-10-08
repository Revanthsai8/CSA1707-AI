from collections import deque

def is_valid(m, c):
    # Number of missionaries and cannibals on each side
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries should not be outnumbered
    if m > 0 and m < c:
        return False

    m_right = 3 - m
    c_right = 3 - c

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    # State = (missionaries_left, cannibals_left, boat_position)
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    # Possible boat movements
    moves = [
        (1, 0), (2, 0),
        (0, 1), (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for p in path:
                print(p)
            return

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

solve()
