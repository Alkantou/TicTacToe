def print_board(board_data):
    for row in board_data:
        print("_".join(row))

# Input Player's choice of mark
# Input Place of mark
# Input 2nd player's mark

#while game == True
    # input place of mark

from TicTacToeClass import TicTacToeClass
# Input Player's choice of mark
input_mark = input("Insert input mark ")
game = TicTacToeClass(input_mark)
while not game.game_over():
    print_board(game.cells)
    print("current player is :"+game.current_player)
    input_horizontal_index = int(input("Insert column index"))
    input_vertical_index = int(input("Insert row index "))

    game.play_move(input_vertical_index, input_horizontal_index)

