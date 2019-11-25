import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from YahtzeeBase   import Roll

class ScoreCard(object):

  def __init__(self,dice):
    self.dice             = dice
    self.n_rolls          = 0
    self.n_bonus_yahtzees = -1
    self.roll_values      = dict()

    self.ones_value   = -1
    self.twos_value   = -1
    self.threes_value = -1
    self.fours_value  = -1
    self.fives_value  = -1
    self.sixes_value  = -1

    self.three_of_a_kind_value  = -1
    self.four_of_a_kind_value   = -1
    self.full_house_value       = -1
    self.small_straight_value   = -1
    self.large_straight_value   = -1
    self.yahtzee_value          = -1
    self.chance_value           = -1

    self.upper_subtotal = 0
    self.lower_subtotal = 0
    self.bonus          = 0

    self.ones_radio_button   = Gtk.RadioButton(group=None,                   label="Ones")
    self.twos_radio_button   = Gtk.RadioButton(group=self.ones_radio_button, label="Twos")
    self.threes_radio_button = Gtk.RadioButton(group=self.ones_radio_button, label="Threes")
    self.fours_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Fours")
    self.fives_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Fives")
    self.sixes_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Sixes")

    self.three_of_a_kind_radio_button = Gtk.RadioButton(group=self.ones_radio_button, label="Three of a Kind")
    self.four_of_a_kind_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Four of a Kind")
    self.full_house_radio_button      = Gtk.RadioButton(group=self.ones_radio_button, label="Full House")
    self.small_straight_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Small Straight")
    self.large_straight_radio_button  = Gtk.RadioButton(group=self.ones_radio_button, label="Large Straight")
    self.yahtzee_radio_button         = Gtk.RadioButton(group=self.ones_radio_button, label="Yahtzee")
    self.chance_radio_button          = Gtk.RadioButton(group=self.ones_radio_button, label="Chance")

    self.ones_label   = Gtk.Label(label="(0)")
    self.twos_label   = Gtk.Label(label="(0)")
    self.threes_label = Gtk.Label(label="(0)")
    self.fours_label  = Gtk.Label(label="(0)")
    self.fives_label  = Gtk.Label(label="(0)")
    self.sixes_label  = Gtk.Label(label="(0)")

    self.upper_subtotal_text  = Gtk.Label(label="Subtotal")
    self.bonus_text           = Gtk.Label(label="Bonus")
    self.upper_total_text     = Gtk.Label(label="Upper Total")

    self.upper_subtotal_label = Gtk.Label(label="(0)")
    self.bonus_label          = Gtk.Label(label="(0)")
    self.upper_total_label    = Gtk.Label(label="(0)")

    self.three_of_a_kind_label = Gtk.Label(label="(0)")
    self.four_of_a_kind_label  = Gtk.Label(label="(0)")
    self.full_house_label      = Gtk.Label(label="(0)")
    self.small_straight_label  = Gtk.Label(label="(0)")
    self.large_straight_label  = Gtk.Label(label="(0)")
    self.yahtzee_label         = Gtk.Label(label="(0)")
    self.chance_label          = Gtk.Label(label="(0)")

    self.lower_subtotal_text  = Gtk.Label(label="Subtotal")
    self.bonus_yahtzee_text   = Gtk.Label(label="Bonus Yahtzees")
    self.lower_total_text     = Gtk.Label(label="Lower Total")
    self.total_text           = Gtk.Label(label="Total")

    self.lower_subtotal_label = Gtk.Label(label="(0)")
    self.bonus_yahtzee_label  = Gtk.Label(label="(0)")
    self.lower_total_label    = Gtk.Label(label="(0)")
    self.total_label          = Gtk.Label(label="(0)")

    self.roll_level_bar = Gtk.LevelBar(min_value=0,max_value=3)

    self.upper_subtotal_text.set_xalign(0.3)
    self.bonus_text.set_xalign(0.3)
    self.upper_total_text.set_xalign(0.3)
    self.lower_subtotal_text.set_xalign(0.3)
    self.bonus_yahtzee_text.set_xalign(0.3)
    self.lower_total_text.set_xalign(0.3)
    self.total_text.set_xalign(0.3)

    self.connect_radio_button(self.ones_radio_button,  'ones')
    self.connect_radio_button(self.twos_radio_button,  'twos')
    self.connect_radio_button(self.threes_radio_button,'threes')
    self.connect_radio_button(self.fours_radio_button, 'fours')
    self.connect_radio_button(self.fives_radio_button, 'fives')
    self.connect_radio_button(self.sixes_radio_button, 'sixes')
 
    self.connect_radio_button(self.three_of_a_kind_radio_button, 'three_of_a_kind')
    self.connect_radio_button(self.four_of_a_kind_radio_button,  'four_of_a_kind')
    self.connect_radio_button(self.full_house_radio_button,      'full_house')
    self.connect_radio_button(self.small_straight_radio_button,  'small_straight')
    self.connect_radio_button(self.large_straight_radio_button,  'large_straight')
    self.connect_radio_button(self.yahtzee_radio_button,         'yahtzee')
    self.connect_radio_button(self.chance_radio_button,          'chance')

  def connect_radio_button(self,radio_button,key):
    radio_button.connect("toggled",self._on_radio_toggled(radio_button,key))

  def _on_radio_toggled(self,radio_button,key):
    def f(widget):
      if radio_button.get_active():
        self.key = key
      else:
        pass
    return f

  def _set(self,key,value):
    setattr(self,key+"_value",value)

  def _get(self,key):
    return getattr(self,key+"_value")

  def _get_label(self,key):
    return getattr(self,key+"_label")

  def _update_label_hypo(self,label,key):
    label.set_label("("+str(self.roll_values[key])+")")

  def play(self):
    self._set(self.key,self.roll_values[self.key])  
    self._get_label(self.key).set_label(str(self._get(self.key)))

  def roll(self):
    self.n_rolls += 1
    self.roll_level_bar.set_value(self.n_rolls)
    R = Roll(*self._dice_values())
    self.roll_values['ones']            = R.ones()
    self.roll_values['twos']            = R.twos()
    self.roll_values['threes']          = R.threes()
    self.roll_values['fours']           = R.fours()
    self.roll_values['fives']           = R.fives()
    self.roll_values['sixes']           = R.sixes()
    self.roll_values['three_of_a_kind'] = R.threeOfAKind()
    self.roll_values['four_of_a_kind']  = R.fourOfAKind()
    self.roll_values['full_house']      = R.fullHouse()
    self.roll_values['small_straight']  = R.shortStraight()
    self.roll_values['large_straight']  = R.longStraight()
    self.roll_values['yahtzee']         = R.yahtzee()
    self.roll_values['chance']          = R.chance()
    for key,item in self.roll_values.iteritems():
      if self._get(key) < 0: self._update_label_hypo(self._get_label(key),key)

  def clear(self):
    self.n_rolls = -1
    self.roll()

  def _dice_values(self):
    return [d.value for d in self.dice]
