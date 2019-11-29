import gi,sys,time,random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio,GdkPixbuf

class ClearDialog(Gtk.Dialog):
  
  def __init__(self,window):
    Gtk.Dialog.__init__(self,"Clear Game",window,0,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
         Gtk.STOCK_OK,     Gtk.ResponseType.OK))

    self.set_default_size(150,100)

    label = Gtk.Label("Are you sure you want to clear the game?")
    box   = self.get_content_area()
    box.add(label)
    self.show_all()
