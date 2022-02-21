import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Caixa_de_Botons(Gtk.Grid):

    def __init__(self):
        super().__init__()

        boton1 = Gtk.Button.new_with_label("Boton 1")
        boton2 = Gtk.Button.new_with_label("Boton 2")
        boton3 = Gtk.Button.new_with_label("Boton 3")
        boton4 = Gtk.Button.new_with_label("Boton 4")
        boton5 = Gtk.Button.new_with_label("Boton 5")
        boton6 = Gtk.Button.new_with_label("Boton 6")

        self.add(boton1)
        self.attach(boton2, 1, 0, 2, 1)
        self.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach(boton4, 1, 1, 2, 1)
        self.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)