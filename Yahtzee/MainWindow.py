import gi,sys,time
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from Dice          import Dice
from ScoreCard     import ScoreCard

class MainWindow(Gtk.ApplicationWindow):
  def __init__(self,app,**kwargs):
    kwargs.update(dict(title="Yahtzee",application=app))
    Gtk.ApplicationWindow.__init__(self,**kwargs)

    grid = Gtk.Grid()
    grid.set_column_spacing(6)
    self.add(grid)

    self.dice1 = Dice(-1)
    self.dice2 = Dice(-1)
    self.dice3 = Dice(-1)
    self.dice4 = Dice(-1)
    self.dice5 = Dice(-1)

    self._dice = (self.dice1,
                  self.dice2,
                  self.dice3,
                  self.dice4,
                  self.dice5)

    for dice in self._dice:
      dice.roll_radio_button.set_active(True)

    self.roll_button = Gtk.Button(label="Roll")
    self.score_card  = ScoreCard(self._dice)
    self.play_button = Gtk.Button(label="Play")

    self.attach_dice          (grid)
    self.attach_roll_button   (grid)
    self.attach_roll_level_bar(grid)
    self.attach_score_card    (grid)
    self.attach_play_button   (grid)

    self.roll_button.connect("clicked",self.on_roll_button_clicked)
    self.play_button.connect("clicked",self.on_play_button_clicked)

  def on_roll_button_clicked(self,widget):
    if self.score_card.n_rolls < 3 and any([dice.roll_radio_button.get_active() for dice in self._dice]): 
      if self.dice1.roll_radio_button.get_active() or self.dice1.value<1: self.dice1.roll()
      if self.dice2.roll_radio_button.get_active() or self.dice2.value<1: self.dice2.roll()
      if self.dice3.roll_radio_button.get_active() or self.dice3.value<1: self.dice3.roll()
      if self.dice4.roll_radio_button.get_active() or self.dice4.value<1: self.dice4.roll()
      if self.dice5.roll_radio_button.get_active() or self.dice5.value<1: self.dice5.roll()
      self.score_card.roll()

  def on_play_button_clicked(self,widget):
    if any( [dice.value>0 for dice in self._dice] ):
      self.score_card.clear()
      self.dice1.clear()
      self.dice2.clear()
      self.dice3.clear()
      self.dice4.clear()
      self.dice5.clear()
      self.score_card.play()

  def attach_roll_button(self,grid):
    grid.attach(self.roll_button,4,3,1,1)

  def attach_roll_level_bar(self,grid):
    grid.attach(self.score_card.roll_level_bar,4,4,1,1)

  def attach_dice(self,grid):
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

  def attach_score_card(self,grid):
    grid.attach(self.score_card.ones_radio_button,  0,5, 1,1)
    grid.attach(self.score_card.twos_radio_button,  0,6, 1,1)
    grid.attach(self.score_card.threes_radio_button,0,7, 1,1)
    grid.attach(self.score_card.fours_radio_button, 0,8, 1,1)
    grid.attach(self.score_card.fives_radio_button, 0,9, 1,1)
    grid.attach(self.score_card.sixes_radio_button, 0,10,1,1)

    grid.attach(self.score_card.ones_label,  1,5, 1,1)
    grid.attach(self.score_card.twos_label,  1,6, 1,1)
    grid.attach(self.score_card.threes_label,1,7, 1,1)
    grid.attach(self.score_card.fours_label, 1,8, 1,1)
    grid.attach(self.score_card.fives_label, 1,9, 1,1)
    grid.attach(self.score_card.sixes_label, 1,10,1,1)

    grid.attach(self.score_card.upper_subtotal_text,0,13,1,1)
    grid.attach(self.score_card.bonus_text,         0,14,1,1)
    grid.attach(self.score_card.upper_total_text,   0,15,1,1)

    grid.attach(self.score_card.upper_subtotal_label,1,13,1,1)
    grid.attach(self.score_card.bonus_label,         1,14,1,1)
    grid.attach(self.score_card.upper_total_label,   1,15,1,1)

    grid.attach(self.score_card.three_of_a_kind_radio_button,2,5, 1,1)
    grid.attach(self.score_card.four_of_a_kind_radio_button, 2,6, 1,1)
    grid.attach(self.score_card.full_house_radio_button,     2,7, 1,1)
    grid.attach(self.score_card.small_straight_radio_button, 2,8, 1,1)
    grid.attach(self.score_card.large_straight_radio_button, 2,9, 1,1)
    grid.attach(self.score_card.yahtzee_radio_button,        2,10,1,1)
    grid.attach(self.score_card.chance_radio_button,         2,11,1,1)

    grid.attach(self.score_card.three_of_a_kind_label,3,5, 1,1)
    grid.attach(self.score_card.four_of_a_kind_label, 3,6, 1,1)
    grid.attach(self.score_card.full_house_label,     3,7, 1,1)
    grid.attach(self.score_card.small_straight_label, 3,8, 1,1)
    grid.attach(self.score_card.large_straight_label, 3,9, 1,1)
    grid.attach(self.score_card.yahtzee_label,        3,10,1,1)
    grid.attach(self.score_card.chance_label,         3,11,1,1)

    grid.attach(self.score_card.lower_subtotal_text,2,13,1,1)
    grid.attach(self.score_card.bonus_yahtzee_text, 2,14,1,1)
    grid.attach(self.score_card.lower_total_text,   2,15,1,1)
    grid.attach(self.score_card.total_text,         2,16,1,1)

    grid.attach(self.score_card.lower_subtotal_label,3,13,1,1)
    grid.attach(self.score_card.bonus_yahtzee_label, 3,14,1,1)
    grid.attach(self.score_card.lower_total_label,   3,15,1,1)
    grid.attach(self.score_card.total_label,         3,16,1,1)

  def attach_play_button(self,grid):
    grid.attach(self.play_button,4,17,1,1)

  def get_dice_values(self):
    return (dice.value for dice in self._dice)
