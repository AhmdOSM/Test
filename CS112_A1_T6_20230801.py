"""
# Program: This is tic-tac-toe with numbers program, it is a game played with 3x3 board and player1 takes odd numbers and
           player2 takes the evens, the first player to complete a line that adds up to 15 is the winner.
# Author: Ahmed Osman Ali Osman, section: not registered, id: 20230801
# Version: 1.2
# Date: 28/2/2024
"""


def display_board(board):
    # a function to display the board
    print(f"|  {board[0]}  |  {board[1]}  |  {board[2]}  |\n"
          "-------------------\n"
          f"|  {board[3]}  |  {board[4]}  |  {board[5]}  |\n"
          "-------------------\n"
          f"|  {board[6]}  |  {board[7]}  |  {board[8]}  |")


def inputs_to_board(board, position, move):
    # update the board with players input
    board[position] = move


def check_win(board):
    # check rows
    if board[0] + board[1] + board[2] == 15 or board[3] + board[4] + board[5] == 15 or board[6] + board[7] + board[8] == 15:
        return True
    # check columns
    elif board[0] + board[3] + board[6] == 15 or board[1] + board[4] + board[7] == 15 or board[2] + board[5] + board[8] == 15:
        return True
    # check diagonals
    elif board[0] + board[4] + board[8] == 15 or board[2] + board[4] + board[6] == 15:
        return True
    else:
        return False


def check_draw(board):
    if 11 not in board and check_win(board) is False:
        # 11 is an arbitrary number used in the background board
        return True
    else:
        return False


def switch_turn():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


positions_board = ['a', 'b', 'c',  # a board to display positions
                   'd', 'e', 'f',
                   'g', 'h', 'i']

background_board = [11, 11, 11,    # a board with arbitrary integer elements to apply check_win()
                    11, 11, 11,    # and check_draw() functions because it is easy to work with integers
                    11, 11, 11]

player1_numbers = [1, 3, 5, 7, 9]
player2_numbers = [0, 2, 4, 6, 8]
current_player = 1

print("Welcome to tic tac toe with numbers!\n")
while True:
    try:
        # get inputs, and if an error occurred the interpreter whill execute the except block and start the loop again
        display_board(positions_board)
        position = input(f"\n<player{current_player}> specify the position: \n").lower()
        move = int(input(f"enter your number: {player1_numbers if current_player == 1 else player2_numbers}\n"))

        if move in player1_numbers and current_player == 1 or move in player2_numbers and current_player == 2:
            inputs_to_board(background_board, positions_board.index(position), move)
            inputs_to_board(positions_board, positions_board.index(position), move)

        # remove selected numbers after each turn:
        if current_player == 1:
            player1_numbers.remove(move)
        else:
            player2_numbers.remove(move)

        # check winning and draw after each turn
        if check_win(background_board):
            display_board(positions_board)
            print(f"\nplayer {current_player} wins!")
            break
        elif check_draw(background_board):
            display_board(positions_board)
            print("\nit`s a draw, the game is over!")
            break

        switch_turn()
        print("==================================\n")

    except ValueError:
        print("==================================\n"
              "Please enter a valid selections!\n")
        continue
