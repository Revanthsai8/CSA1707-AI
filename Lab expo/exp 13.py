# Minimax Algorithm for Tic-Tac-Toe

board = [' ' for i in range(9)]

def display():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')

def check_winner():
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]] != ' ':
            return board[x[0]]
    return None

def minimax(is_max):
    winner = check_winner()

    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best = -100
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best:
                best = score
                move = i

    return move

# Main game
while True:
    display()
    pos = int(input("Enter your position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid move!")
        continue

    board[pos] = 'X'

    if check_winner() == 'X':
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Match Draw!")
        break

    move = best_move()
    board[move] = 'O'

    if check_winner() == 'O':
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("Match Draw!")
        break
