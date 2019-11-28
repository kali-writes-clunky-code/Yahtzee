import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

class Dice(object):

  def __init__(self,value):
    self.value             = value
    self.image             = Gtk.Image()
    self.hold_radio_button = Gtk.RadioButton(group=None,                  label="Hold")
    self.roll_radio_button = Gtk.RadioButton(group=self.hold_radio_button,label="Roll")
    self.update_image()
    self.hold_radio_button.connect("toggled",self.on_hold_radio_button_toggled)

  def update_image(self,value=None):
    value = self.value if value is None else value
    if 1 <= value <= 6:
      self.image.set_from_file("Images/dice%d.png"%value)
    else:
      self.image.set_from_file("Images/rolling.gif")

  def clear(self):
    self.value = -1
    self.update_image()

  def play(self):
    self.clear()

  def is_rollable(self):
    return self.roll_radio_button.get_active() or self.value<1

  def roll(self):
    if self.roll_radio_button.get_active() or self.value<1:
      self.value = random.randint(1,6)
      self.update_image(self.value)
      self.hold_radio_button.set_active(True)

  def on_hold_radio_button_toggled(self,radio_button):
    if radio_button.get_active():
      self.update_image()
    else:
      self.update_image(0)
