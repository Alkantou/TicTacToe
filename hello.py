import gi
from TicTacToeClass import TicTacToeClass

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self, game1: TicTacToeClass):
        Gtk.Window.__init__(self, title="TIC TAC TOE")
        self.game = game1

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label=" ")
        button1.connect("clicked", self.on_button1_clicked, (0, 0))
        button2 = Gtk.Button(label=" ")
        button2.connect("clicked", self.on_button1_clicked, (1, 0))
        button3 = Gtk.Button(label=" ")
        button3.connect("clicked", self.on_button1_clicked, (2, 0))
        button4 = Gtk.Button(label=" ")
        button4.connect("clicked", self.on_button1_clicked, (0, 1))
        button5 = Gtk.Button(label=" ")
        button5.connect("clicked", self.on_button1_clicked, (1, 1))
        button6 = Gtk.Button(label=" ")
        button6.connect("clicked", self.on_button1_clicked, (2, 1))
        button7 = Gtk.Button(label=" ")
        button7.connect("clicked", self.on_button1_clicked, (0, 2))
        button8 = Gtk.Button(label=" ")
        button8.connect("clicked", self.on_button1_clicked, (1, 2))
        button9 = Gtk.Button(label=" ")
        button9.connect("clicked", self.on_button1_clicked, (2, 2))

        grid.add(button1)
        grid.attach(button2, 1, 0, 1, 1)
        grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button4, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5, button4, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button7, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button9, button8, Gtk.PositionType.RIGHT, 1, 1)

    def on_button1_clicked(self, widget, ButtonInput):
        widget.set_label(self.game.current_player)
        widget.set_sensitive(False)
        print(ButtonInput)
        self.game.play_move(row_index=ButtonInput[0],column_index=ButtonInput[1])
        if self.game.game_over():
            self.on_info_clicked()

    def on_info_clicked(self):
        dialog = Gtk.MessageDialog(
            self,
            0,
            Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK,
            "This is an INFO MessageDialog",
        )
        dialog.format_secondary_text(
            "GAME OVER"
        )
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()


# Above win = GridWindow() create a TicTacToeClass object and pass it to the GridWindow constructor

game = TicTacToeClass()
win = GridWindow(game)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
