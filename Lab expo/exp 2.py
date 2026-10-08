def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i in range(row):
        if board[i] - i == col - row:
            return False

    # Check right diagonal
    for i in range(row):
        if board[i] + i == col + row:
            return False

    return True


def solve(board, row):
    # All queens are placed
    if row == 8:
        return True

    # Try each column
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


# Create board
board = [-1] * 8

# Solve the problem
if solve(board, 0):
    print("Solution:")
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")
