import gi

gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gdk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Paleta cambio de color")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        caixaV.props.border_width = 30

        self.txtColor = Gtk.Entry()
        self.txtColor.set_editable(False)
        self.txtColor.set_name("txtColor")
        caixaV.pack_start(self.txtColor, True, True, 6)

        self.btnRed = Gtk.Button.new_with_label(label="Red")
        self.btnRed.connect("clicked", self.cambioColor, "red")
        caixaH.pack_start(self.btnRed, False, True, 6)

        self.btnYellow = Gtk.Button.new_with_label(label="Yellow")
        self.btnYellow.connect("clicked", self.cambioColor, "yellow")
        caixaH.pack_start(self.btnYellow, False, True, 6)

        self.btnBlue = Gtk.Button.new_with_label(label="Blue")
        self.btnBlue.connect("clicked", self.cambioColor, "blue")
        caixaH.pack_start(self.btnBlue, False, True, 6)
        caixaV.pack_start(caixaH, True, True, 5)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def cambioColor(self, boton, color):
        provider = Gtk.CssProvider()
        if color == "blue":
            css = '#txtColor { background: blue; }'
            provider.load_from_data((css.encode()))
            Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        elif color == "red":
            css = '#txtColor { background: red; }'
            provider.load_from_data((css.encode()))
            Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        else:
            css = '#txtColor { background: yellow; }'
            provider.load_from_data((css.encode()))
            Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()