import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

class PlayButton(Gtk.Button):
  
  def __init__(self,window):
    Gtk.Button.__init__(self,label="Play")
    self.window = window  
    self.connect("clicked",self.on_clicked)

  def attach(self,grid,iLine):
    grid.attach(self,4,iLine,1,1)
    return iLine
  
  def on_clicked(self,widget):
    self.window.dice.play()
    self.window.score_card.play()
