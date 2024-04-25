def greet():
    print("Welcome to tic tac toe game ")
    print("INSTRUCTIONS TO PLAY THE GAME :")
    print(""" 
        This game can be played by two players.
        One player is assigned X and the other is assigned O.
        You have to mark the X and O in such a way that there is a diagonal or a row with the same symbols.
        The player who does that first wins the game.

        To place the symbol X or O in the respective side of the board, all the players have to enter the number written on the board.
    """)


def board(board):
    print("   |    |")
    print(board[1], " | ", board[2], " | ", board[3])
    print("-------------")
    print("   |    |")
    print(board[4], " | ", board[5], " | ", board[6])
    print("-------------")
    print("   |    |")
    print(board[7], " | ", board[8], " | ", board[9])


def check_win(board):
    # Check rows, columns, and diagonals
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return True
    if board[1] == board[5] == board[9] != ' ' or board[3] == board[5] == board[7] != ' ':
        return True
    return False


def play():
    greet()
    players = {1: {'name': input("Enter your name player 1: "), 'symbol': 'X'},
               2: {'name': input("Enter your name player 2: "), 'symbol': 'O'}}

    board = {i: ' ' for i in range(1, 10)}
    current_player = 1

    while True:
        board(current_board)
        move = int(input(f"{players[current_player]['name']}, enter your move (1-9): "))
        
        if board[move] == ' ':
            board[move] = players[current_player]['symbol']
        else:
            print("Invalid move! Choose an empty spot.")
            continue

        if check_win(board):
            print(f"{players[current_player]['name']} wins!")
            break
        elif ' ' not in board.values():
            print("It's a tie!")
            break

        current_player = 3 - current_player  # Switch players

play()
