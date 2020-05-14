class TicTacToeClass:

    def __init__(self,inputmark):
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = inputmark
        self.moves = 0
        self.winner = None

    def next_move(self,row_index:int,column_index:int) -> None:
        self.cells[row_index][column_index]= self.current_player
        self.moves = self.moves + 1

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def game_over(self):
        return self.tictactoe() or self.nomovesleft()

    def nomovesleft(self):
        return self.moves == 9

    def tictactoe(self):
        column_index = 0
        for row_index in range(3):
             if self.cells[row_index][column_index] == self.cells[row_index][column_index + 1] and self.cells[row_index][column_index + 1] == self.cells[row_index][column_index + 2]:
                 return True
        row_index = 0
        for column_index in range(3):
            if self.cells[row_index][column_index] == self.cells[row_index+1][column_index] and self.cells[row_index+1][column_index] == self.cells[row_index + 2][column_index]:
                 return True

        if self.cells[0][0] == self.cells[1][1] and self.cells[1][1] == self.cells[2][2]:
            return True







