def print_board(board_data):
    count = 1
    for row in board_data:
        row_accumulator = []
        for column in row:

            if column == " ":
                row_accumulator.append(str(count))
            else:
                row_accumulator.append(column)
            count = count+1
        print("_".join(row_accumulator))


# Input Player's choice of mark
# Input Place of mark
# Input 2nd player's mark

# while game == True
# input place of mark

number_to_ticatactoe_move= {"1": (0, 0),
     "2": (1, 0),
     "3": (2, 0),
     "4": (0, 1),
     "5": (1, 1),
     "6": (2, 1),
     "7": (0, 2),
     "8": (1, 2),
     "9": (2, 2)}

from TicTacToeClass import TicTacToeClass

# Input Player's choice of mark
while True:
    input_mark = input("Insert input mark ")
    if input_mark not in ["X", "O"]:
        continue
    game = TicTacToeClass(input_mark)
    while not game.game_over():
        print_board(game.cells)
        print("current player is :" + game.current_player)
        input_number = input("Select number ")
        input_vertical_index = number_to_ticatactoe_move[input_number][1]
        input_horizontal_index = number_to_ticatactoe_move[input_number][0]
        game.play_move(input_vertical_index, input_horizontal_index)

    print_board(game.cells)
    if game.winner is None:
        print("Unfortunately nobody won")
    else:
        print("Game winner is : "+ game.winner)
