import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf
from Dice          import Dice

class DiceEnsemble(object):

  def __init__(self):
    self._dice = [Dice(-1) for _ in range(5)]

  @property
  def values(self):
    return [d.value for d in self]

  def is_rollable(self):
    return any([d.is_rollable() for d in self])

  def clear(self):
    for d in self: d.clear()

  def roll(self):
    for d in self: d.roll()

  def play(self):
    for d in self: d.play()

  def attach(self,grid,iLine):
    for i,d in enumerate(self):
      grid.attach(d.image,            i,iLine+0,1,1)
      grid.attach(d.hold_radio_button,i,iLine+1,1,1)
      grid.attach(d.roll_radio_button,i,iLine+2,1,1)
    return iLine+2

  def __iter__(self):
    self.i = -1
    return self

  def next(self):
    self.i += 1
    if self.i == 5:
      raise StopIteration
    return self._dice[self.i]

  def __getitem__(self,key):
    return self._dice[key]

  def __setitem__(self,key,value):
    self._dice[key] = value
