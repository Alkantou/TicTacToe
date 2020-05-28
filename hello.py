import gi
import TicTacToeClass
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self, game):
        Gtk.Window.__init__(self, title="TIC TAC TOE")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button1.connect("clicked", self.on_button1_clicked)
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        button7 = Gtk.Button(label="Button 7")
        button8 = Gtk.Button(label="Button 8")
        button9 = Gtk.Button(label="Button 9")

        grid.add(button1)
        grid.attach(button2, 1, 0, 1, 1)
        grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button4, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5, button4, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button7, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button9, button8, Gtk.PositionType.RIGHT, 1, 1)

    def on_button1_clicked(self, widget):
        #widget.set_label("Foo")
        widget.set_sensitive(False)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



