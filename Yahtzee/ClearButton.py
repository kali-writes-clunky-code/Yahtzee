import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

from ClearDialog import ClearDialog

class ClearButton(Gtk.Button):
  
  def __init__(self,window):
    Gtk.Button.__init__(self,label="Clear")
    self.window = window  
    self.connect("clicked",self.on_clicked)

  def attach(self,grid,iLine):
    grid.attach(self,0,iLine,1,1)
    return iLine
  
  def on_clicked(self,widget):
    dialog   = ClearDialog(self.window)
    response = dialog.run()
  
    if response==Gtk.ResponseType.OK:
      self.window.dice.clear()
      self.window.score_card.clear()

    dialog.destroy()
