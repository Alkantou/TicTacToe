import gi
from TicTacToeClass import TicTacToeClass
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self, game1:TicTacToeClass):
        Gtk.Window.__init__(self, title="TIC TAC TOE")
        self.game = game1

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.button1 = Gtk.Button(label="")
        self.button1.connect("clicked", self.on_button1_clicked, (0, 0))

        self.button2 = Gtk.Button(label="")
        self.button2.connect("clicked", self.on_button1_clicked, (0, 1))

        self.button3 = Gtk.Button(label="")
        self.button3.connect("clicked", self.on_button1_clicked, (0, 2))

        self.button4 = Gtk.Button(label="")
        self.button4.connect("clicked", self.on_button1_clicked, (1, 0))

        self.button5 = Gtk.Button(label="")
        self.button5.connect("clicked", self.on_button1_clicked, (1, 1))

        self.button6 = Gtk.Button(label="")
        self.button6.connect("clicked", self.on_button1_clicked, (1, 2))

        self.button7 = Gtk.Button(label="")
        self.button7.connect("clicked", self.on_button1_clicked, (2, 0))

        self.button8 = Gtk.Button(label="")
        self.button8.connect("clicked", self.on_button1_clicked, (2, 1))

        self.button9 = Gtk.Button(label="")
        self.button9.connect("clicked", self.on_button1_clicked, (2, 2))


        self.grid.add(self.button1)
        self.grid.attach(self.button2, 1, 0, 1, 1)
        self.grid.attach_next_to(self.button3, self.button2, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button4, self.button1, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button5, self.button4, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button6, self.button5, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button7, self.button4, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.button8, self.button7, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.button9, self.button8, Gtk.PositionType.RIGHT, 1, 1)

    def on_button1_clicked(self, widget, ButtonInput):
        widget.set_label(self.game.current_player)
        widget.set_sensitive(False)
        print(ButtonInput)
        self.game.play_move(row_index=ButtonInput[0],column_index=ButtonInput[1])
        self.on_info_clicked()

    def on_info_clicked(self):
        if self.game.game_over():
            winnerprint = "We have A Winner!"
            winner = self.game.winner
            if winner is None:
                winnerprint = "We have No Winner"
            else:
                winnerprint = "We have A Winner!" + winner +  " is the winner!"
            dialog = Gtk.MessageDialog(self,0,Gtk.MessageType.INFO,Gtk.ButtonsType.OK, winnerprint )
            dialog.format_secondary_text("Don't Know Who")
            dialog.run()
            print("INFO dialog closed")

            dialog.destroy()
            self.game = TicTacToeClass()
            self.button1.set_label(" ")
            self.button1.set_sensitive(True)
            self.button2.set_label(" ")
            self.button2.set_sensitive(True)
            self.button3.set_label(" ")
            self.button3.set_sensitive(True)
            self.button4.set_label(" ")
            self.button4.set_sensitive(True)
            self.button5.set_label(" ")
            self.button5.set_sensitive(True)
            self.button6.set_label(" ")
            self.button6.set_sensitive(True)
            self.button7.set_label(" ")
            self.button7.set_sensitive(True)
            self.button8.set_label(" ")
            self.button8.set_sensitive(True)
            self.button9.set_label(" ")
            self.button9.set_sensitive(True)
            #self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#Above win = GridWindow() create a TicTacToeClass object and pass it to the GridWindow constructor

game = TicTacToeClass()
win = GridWindow(game)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



