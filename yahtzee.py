import gi,sys,time
gi.require_version("Gtk","3.0")
from gi.repository  import Gtk,Gio,GdkPixbuf
from Yahtzee.App    import YahtzeeApp

app = YahtzeeApp()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
