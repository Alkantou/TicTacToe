import pytest


from TicTacToeClass import TicTacToeClass


def test_first_player_is_X():
    game = TicTacToeClass()
    assert game.current_player == "X"


def test_switch_player():
     game = TicTacToeClass()
     game.switch_player()
     assert game.current_player == "O"
     game.switch_player()
     assert game.current_player == "X"

def test_game_next_move_switches_player():
    game = TicTacToeClass()
    game.play_move(0, 0)
    assert game.current_player == "O"


def test_game_invalid_index_raised_value_error():
    game = TicTacToeClass()
    with pytest.raises(ValueError):
        game.play_move(-1, -1)

def test_game_over_index_raised_value_error():
    game = TicTacToeClass()
    with pytest.raises(ValueError):
        game.play_move(4, -1)


def test_movez_performed():
    game = TicTacToeClass()
    game.play_move(0, 0)
    game.play_move(1, 1)
    assert game.moves == 2


def test_not_possible_to_move_to_already_used_cell():
    game = TicTacToeClass()
    game.play_move(0, 0)
    with pytest.raises(ValueError):
        game.play_move(0, 0)


def test_line_tic_tac():
    game = TicTacToeClass()
    game.play_move(0, 0)
    game.play_move(1, 0)
    game.play_move(0, 1)
    game.play_move(1, 0)
    game.play_move(0, 2)

    assert game.tictactoe() == True


def test_winner_is_X():
    game = TicTacToeClass()
    game.play_move(0, 0)
    game.play_move(1, 0)
    game.play_move(0, 1)
    game.play_move(1, 0)
    game.play_move(0, 2)

    assert game.winner == "X"


def test_not_possible_to_play_after_game_is_over():

    # write code to play a game with a winner

    # try to play a free cell should raise a value error

    pass