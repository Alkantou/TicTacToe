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
    #print current board
    #read user input
    game.play_move()

