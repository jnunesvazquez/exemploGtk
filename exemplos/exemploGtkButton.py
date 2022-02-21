import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de uso de Gtk.label")
        #self.set_title("Exemplo de uso de Gtk.Label")
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.boton = Gtk.Button.new_with_label("Etiqueta")
        self.boton = Gtk.Button.new_with_mnemonic("_Abrir")


        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def accionBoton(self, boton):
        self.contador += 1
        self.etiqueta.set_text("Numero de pulsaciones " + str(self.contador))


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()