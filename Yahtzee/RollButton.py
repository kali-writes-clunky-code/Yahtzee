import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

class RollButton(Gtk.Button):
  
  def __init__(self,window):
    Gtk.Button.__init__(self,label="Roll")
    self.window = window  
    self.level_bar = Gtk.LevelBar()
    self.level_bar.set_min_value(0)
    self.level_bar.set_max_value(3)
    self.connect("clicked",self.on_clicked)

  def attach(self,grid,iLine):
    grid.attach(self,          4,iLine,  1,1)
    grid.attach(self.level_bar,4,iLine+1,1,1)
    return iLine+1
  
  def on_clicked(self,widget):
    if self.window.score_card.n_rolls < 3 and self.window.dice.is_rollable():
      self.set_n_rolls(self.window.score_card.n_rolls)
      self.window.dice.roll()
      self.window.score_card.roll()

  def set_n_rolls(self,n):
    self.level_bar.set_value(n)
