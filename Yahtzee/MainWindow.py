import gi,sys,time
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from Dice import Dice

class MainWindow(Gtk.ApplicationWindow):
  def __init__(self,app,**kwargs):
    kwargs.update(dict(title="Yahtzee",application=app))
    Gtk.ApplicationWindow.__init__(self,**kwargs)

    grid = Gtk.Grid()
    grid.set_column_spacing(6)
    self.add(grid)

    self.dice1 = Dice(1)
    self.dice2 = Dice(6)
    self.dice3 = Dice(6)
    self.dice4 = Dice(6)
    self.dice5 = Dice(1)

    self.roll_button = Gtk.Button.new_with_label("Roll")

    grid.attach(self.dice1.image,0,0,1,1)
    grid.attach(self.dice2.image,1,0,1,1)
    grid.attach(self.dice3.image,2,0,1,1)
    grid.attach(self.dice4.image,3,0,1,1)
    grid.attach(self.dice5.image,4,0,1,1)

    grid.attach(self.dice1.hold_radio_button,0,1,1,1)
    grid.attach(self.dice2.hold_radio_button,1,1,1,1)
    grid.attach(self.dice3.hold_radio_button,2,1,1,1)
    grid.attach(self.dice4.hold_radio_button,3,1,1,1)
    grid.attach(self.dice5.hold_radio_button,4,1,1,1)

    grid.attach(self.dice1.roll_radio_button,0,2,1,1)
    grid.attach(self.dice2.roll_radio_button,1,2,1,1)
    grid.attach(self.dice3.roll_radio_button,2,2,1,1)
    grid.attach(self.dice4.roll_radio_button,3,2,1,1)
    grid.attach(self.dice5.roll_radio_button,4,2,1,1)

    grid.attach(self.roll_button,4,3,1,1)
