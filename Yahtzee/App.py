import gi,sys,time
gi.require_version("Gtk","3.0")
from gi.repository  import Gtk,Gio,GdkPixbuf
from MainWindow     import MainWindow

_test = True

class YahtzeeApp(Gtk.Application):

  def __init__(self):
    Gtk.Application.__init__(self)
    self.win = None

  def do_activate(self):
    if not self.win:
      self.win = MainWindow(self)
      self.win.show_all()

  def on_quit(self, action, parameter):
    self.quit()

  def do_startup(self):
    Gtk.Application.do_startup(self)
    menu = Gio.Menu()
    menu.append("About","app.about")
    menu.append("Quit","app.quit")
    self.set_app_menu(menu)

    quit_action = Gio.SimpleAction.new("quit",None)
    quit_action.connect("activate",self.on_quit)
    self.add_action(quit_action)
    
    about_action = Gio.SimpleAction.new("about",None)
    about_action.connect("activate",self.on_about_dialog)
    app.add_action(about_action)

  def on_about_dialog(self, action, parameter):
    aboutdialog = Gtk.AboutDialog()
    authors     = ("Empress Kali","Elli Harido")
    artists     = ("Empress Kali",)
    logo        = GdkPixbuf.Pixbuf.new_from_file("Images/creep_with_dice.png")
    aboutdialog.set_program_name("Yahtzee")
    aboutdialog.set_version("0.1")
    aboutdialog.set_copyright("kx (c) 2019")
    aboutdialog.set_comments("Yahtzee Game for Elli and Kali")
    aboutdialog.set_authors(authors)
    aboutdialog.set_artists(artists)
    aboutdialog.set_title("Yahtzee")
    aboutdialog.set_logo(logo)

    aboutdialog.connect("response",self.on_close_about_dialog)
    aboutdialog.show()

  def on_close_about_dialog(self, action, parameter):
    action.destroy()

if _test:
  app = YahtzeeApp()
  exit_status = app.run(sys.argv)
  sys.exit(exit_status)
