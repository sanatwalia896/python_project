# I am making tictactoe game using python


def greet():
    print("Welcome to tic tac toe game ")

    print("INSTRUCTIONS TO PLAY THE GAME :")
    print(
        """ This game can be played by two players .
          
          One player is assigned X nad the other is assigned O 

          you have to mark the X and O in such a way that thir is a diagonal or a row with the same symbols 

          the player who does that first wins the game 


          to place the symbol X or O in the respective side of the board 

          all the players have to enter the number written on the board 
"""
    )


def board():
    board = list(range(10))

    print("   |", "    |")
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print("   |", "    |")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print("   |", "    |")
    print(board[6], " | ", board[7], " | ", board[8])


board()
