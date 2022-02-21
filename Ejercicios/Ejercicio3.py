import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Paleta cambio de tamaño")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        #Espaciado entre elementos
        caixaV.props.border_width = 50

        self.txtTexto = Gtk.Entry()
        self.txtTexto.set_width_chars(28)
        self.txtTexto.set_text("Hola")
        caixaV.pack_start(self.txtTexto, True, True, 0)

        self.btnMayus = Gtk.Button()
        self.btnMayus.set_label("Mayuscula")
        self.btnMayus.connect("clicked", self.cambioMayus)
        caixaH.pack_start(self.btnMayus, False, True, 8)

        self.btnMin = Gtk.Button()
        self.btnMin.set_label("Minuscula")
        self.btnMin.connect("clicked", self.cambioMin)
        caixaH.pack_start(self.btnMin, False, True, 8)

        caixaV.pack_start(caixaH, True, True, 5)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def cambioMayus(self, boton):
        texto = self.txtTexto.get_text()
        self.txtTexto.set_text(texto.upper())

    def cambioMin(self, boton):
        texto = self.txtTexto.get_text()
        self.txtTexto.set_text(texto.lower())

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()