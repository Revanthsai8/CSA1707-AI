# Tic-Tac-Toe Game

board = [' ' for i in range(9)]

def display():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner():
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]] != ' ':
            return True
    return False

def play():
    player = 'X'

    for turn in range(9):
        display()
        pos = int(input("Player " + player + ", enter position (1-9): ")) - 1

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid position! Try again.")
            return play()

        board[pos] = player

        if check_winner():
            display()
            print("Player", player, "wins!")
            return

        player = 'O' if player == 'X' else 'X'

    display()
    print("Match Draw!")

play()
