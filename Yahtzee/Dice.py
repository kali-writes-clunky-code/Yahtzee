import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

class Dice(object):
  def __init__(self,initial_value=-1):
    self._value = initial_value
    self._image = Gtk.Image()
    self._load_image(initial_value)
    self.hold_radio_button = Gtk.RadioButton.new_with_label_from_widget(None,"Hold")
    self.roll_radio_button = Gtk.RadioButton.new_with_label_from_widget(self.hold_radio_button,"Roll")
    self.hold_radio_button.connect("toggled",self.on_hold_radio_button_toggled)

  def on_hold_radio_button_toggled(self,widget):
    if widget.get_active():
      self.set_image(self.value)
    else:
      self.set_image(0)

  def _load_image(self,value):
    if value > 0:
      self._image.set_from_file("Images/dice%d.png"%value)
    else:
      self._image.set_from_file("Images/rolling.gif")

  def set_image(self,value):
    self._load_image(value)

  def roll(self):
    self._value = random.randint(1,6)
    self.set_image(self._value)
    self.hold_radio_button.set_active(True)

  def clear(self):
    self._value = -1
    self.roll_radio_button.set_active(True)

  @property
  def value(self): return self._value

  @property
  def image(self): return self._image
