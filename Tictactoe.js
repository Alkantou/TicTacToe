class TicTacToeClass{
    constructor(inputmark="X"){
        if (inputmark  != "X" && inputmark != "O")
            throw "X or O"
        this.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        this.current_player = inputmark
        this.moves = 0
        this.winner = null
        }

     play_move( row_index, column_index ){
        if (this.game_over())
             throw "Value Error"
        if (row_index < 0 || row_index > 2)
            throw "invalid row index" + (row_index)
        if (column_index < 0 || column_index > 2)
            throw "invalid row index" + (column_index)
        if (this.cells[row_index][column_index]!= " ")
            throw    ("Space not Blank")
        this.cells[row_index][column_index] = this.current_player
        if (this.tictactoe() == true)
            this.winner = this.current_player
        this.switch_player()
        this.moves = this.moves + 1
     }


      
     switch_player(){
        if (this.current_player == 'X')
            this.current_player = 'O'
        else
            this.current_player = 'X'
     }

     
     game_over(){
        return this.tictactoe()||this.nomovesleft()}

     nomovesleft(){
        return this.moves == 9}

     tictactoe(){
        var column_index = 0
        for (row_index = 0 ; row_index<3; row_index++)
           { if (this.cells[row_index][column_index] == this.cells[row_index][column_index + 1]&&this.cells[row_index][
                column_index + 1] == this.cells[row_index][column_index + 2]&&this.cells[row_index][
                column_index]!= " ")
                return true}
        var row_index = 0
        for (column_index = 0; column_index<3; column_index++)
           { if (this.cells[row_index][column_index] == this.cells[row_index + 1][column_index]&&this.cells[row_index][
                column_index]!= " " 
                   &&this.cells[row_index + 1][column_index] == this.cells[row_index + 2][column_index])
                return true}

        if (this.cells[1][1]!= " "&&this.cells[0][0] == this.cells[1][1]&&this.cells[1][1] == this.cells[2][2])
            return true
        if (this.cells[1][1]!= " "&&this.cells[0][2] == this.cells[1][1]&&this.cells[1][1] == this.cells[2][0])
            return true
        return false

        }}
