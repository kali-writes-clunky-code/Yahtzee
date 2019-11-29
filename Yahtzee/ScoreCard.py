import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from DiceEnsemble  import DiceEnsemble
from YahtzeeBase   import Roll

UPPER_KEYS = ("Ones",
              "Twos",
              "Threes",
              "Fours",
              "Fives",
              "Sixes")

LOWER_KEYS = ("Three of a Kind",
              "Four of a Kind",
              "Full House",
              "Small Straight",
              "Large Straight",
              "Yahtzee",
              "Chance")

UPPER_SPECIAL_KEYS = ("Upper Subtotal",
                      "Bonus",
                      "Upper Total")

LOWER_SPECIAL_KEYS = ("Lower Subtotal",
                      "Bonus Yahtzee",
                      "Lower Total",
                      "Total")

class ScoreCard(object):

  def __init__(self,window):

    self.window = window

    self.n_rolls          = 0
    self.n_bonus_yahtzees = -1
    self.key              = UPPER_KEYS[0]

    self.dice_values    = {}
    self.values         = {}
    self.radio_buttons  = {}
    self.score_labels   = {}
    self.special_labels = {}
    
    self.dice = DiceEnsemble()

    for key in UPPER_KEYS+LOWER_KEYS:
      self.values     [key] = -1
      self.dice_values[key] = -1
      if key == UPPER_KEYS[0]:
        self.radio_buttons[key] = Gtk.RadioButton(group=None,label=key)
      else:
        self.radio_buttons[key] = Gtk.RadioButton(group=self.radio_buttons[UPPER_KEYS[0]],label=key)
      self.connect_radio_button(key)
      self.score_labels[key] = Gtk.Label("(0)")

    for key in UPPER_SPECIAL_KEYS+LOWER_SPECIAL_KEYS:
      self.special_labels[key] = Gtk.Label(key)
      self.score_labels  [key] = Gtk.Label("0")

  @property
  def upper_subtotal(self):
    return sum([self.values[key] for key in UPPER_KEYS if self.values[key]>0])

  @property
  def bonus(self):
    return 0 if self.upper_subtotal < 63 else 35

  @property
  def upper_total(self):
    return self.upper_subtotal + self.bonus

  @property
  def lower_subtotal(self):
    return sum([self.values[key] for key in LOWER_KEYS if self.values[key]>0])

  @property
  def bonus_yahtzee(self):
    return 100*self.n_bonus_yahtzees if self.n_bonus_yahtzees > 0 else 0

  @property
  def lower_total(self):
    return self.lower_subtotal + self.bonus_yahtzee

  @property
  def total(self):
    return self.upper_total + self.lower_total

  def get_special(self,key):
    key = key.lower().replace(" ","_")
    return getattr(self,key)

  def connect_radio_button(self,key):
    self.radio_buttons[key].connect("toggled",self._on_radio_toggled(key))

  def _on_radio_toggled(self,key):
    def f(widget):
      if self.radio_buttons[key].get_active():
        self.key = key
      else:
        pass
    return f

  def attach(self,grid,iLine):
    for i,key in enumerate(UPPER_KEYS):
      grid.attach(self.radio_buttons[key],0,iLine+i,1,1)
      grid.attach(self.score_labels [key],1,iLine+i,1,1)
    for i,key in enumerate(LOWER_KEYS):
      grid.attach(self.radio_buttons[key],2,iLine+i,1,1)
      grid.attach(self.score_labels [key],3,iLine+i,1,1)
    jLine = iLine+max(len(LOWER_KEYS),len(UPPER_KEYS))+1
    for i,key in enumerate(UPPER_SPECIAL_KEYS):
      grid.attach(self.special_labels[key],0,jLine+i,1,1)
      grid.attach(self.score_labels  [key],1,jLine+i,1,1)
    for i,key in enumerate(LOWER_SPECIAL_KEYS):
      grid.attach(self.special_labels[key],2,jLine+i,1,1)
      grid.attach(self.score_labels  [key],3,jLine+i,1,1)
    return jLine+max(len(LOWER_SPECIAL_KEYS),len(UPPER_SPECIAL_KEYS))

  def roll(self):
    self.n_rolls += 1
    self.window.roll_button.set_n_rolls(self.n_rolls)
    R = Roll(*self.window.dice.values)
    for key in UPPER_KEYS+LOWER_KEYS:
      if self.values[key] < 0:
        self.score_labels[key].set_label("(%d)"%R[key])
      self.dice_values[key] = R[key]

  def play(self):
    for key in LOWER_KEYS+UPPER_KEYS:
      if self.values[key] < 0:
        self.score_labels[key].set_label("(0)")
      if self.radio_buttons[key].get_active() and self.n_rolls > 0:
        self.values[key] = self.dice_values[key]
        self.score_labels[key].set_label(str(self.values[key]))
        if key=="Yahtzee":
          self.n_bonus_yahtzees += 1
    for key in UPPER_SPECIAL_KEYS+LOWER_SPECIAL_KEYS:
        self.score_labels[key].set_label(str(self.get_special(key)))
    self.n_rolls = 0
    self.window.roll_button.level_bar.set_value(self.n_rolls)
    

  def clear(self):
    pass
