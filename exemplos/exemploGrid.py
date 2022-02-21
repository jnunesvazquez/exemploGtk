import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de uso de Grid")
        super().set_border_width(15)

        cuadricula = Gtk.Grid()

        boton1 = Gtk.Button.new_with_label("Boton 1")
        boton2 = Gtk.Button.new_with_label("Boton 2")
        boton3 = Gtk.Button.new_with_label("Boton 3")
        boton4 = Gtk.Button.new_with_label("Boton 4")
        boton5 = Gtk.Button.new_with_label("Boton 5")
        boton6 = Gtk.Button.new_with_label("Boton 6")

        cuadricula.add(boton1)
        cuadricula.attach(boton2, 1, 0, 2, 1)
        cuadricula.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        cuadricula.attach(boton4, 1, 1, 2, 1)
        cuadricula.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        cuadricula.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        self.add(cuadricula)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()