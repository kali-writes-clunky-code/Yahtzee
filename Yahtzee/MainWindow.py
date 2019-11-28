import gi,sys,time
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from DiceEnsemble  import DiceEnsemble
from RollButton    import RollButton
from PlayButton    import PlayButton
from ScoreCard     import ScoreCard

class MainWindow(Gtk.ApplicationWindow):
  def __init__(self,app,**kwargs):
    kwargs.update(dict(title="Yahtzee",application=app))
    Gtk.ApplicationWindow.__init__(self,**kwargs)

    #####
    # Setup grid
    #####

    grid = Gtk.Grid()
    grid.set_column_spacing(6)
    self.add(grid)

    #####
    # Setup dice ensemble
    #####

    self.dice = DiceEnsemble()

    #####
    # Setup score card
    #####

    self.score_card = ScoreCard(self)

    #####
    # Setup buttons
    #####

    self.roll_button = RollButton(self)
    self.play_button = PlayButton(self)

    #####
    # Attach widgets to window
    #####

    iLine = self.dice.attach            (grid,0)
    iLine = self.roll_button.attach     (grid,iLine+1)
    iLine = self.score_card.attach      (grid,iLine+1)
    iLine = self.play_button.attach     (grid,iLine+1)
