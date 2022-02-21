import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GdkPixbuf


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de ListBox")
        self.set_border_width(5)
        self.set_default_size(1000, 600)

        flowBox = Gtk.FlowBox()
        flowBox.set_selection_mode(Gtk.SelectionMode.NONE)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="folder.jpg",
            width=80,
            height=80,
            preserve_aspect_ratio=True)

        pixbuf2 = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="file.png",
            width=80,
            height=80,
            preserve_aspect_ratio=True)


        ejemplo_dir = '/home/oracle/'
        with os.scandir(ejemplo_dir) as ficheros:
            for fichero in ficheros:
                etiqueta = Gtk.Label(label=fichero.name)
                etiqueta.set_line_wrap(True)
                etiqueta.set_max_width_chars(10)
                folder = Gtk.Image.new_from_pixbuf(pixbuf)
                file = Gtk.Image.new_from_pixbuf(pixbuf2)
                cuadricula = Gtk.Grid()

                if (fichero.is_dir()):
                    cuadricula.attach(folder, 0, 0, 1, 1)
                    cuadricula.attach(etiqueta, 0, 1, 1, 1)
                elif (fichero.is_file()):
                    cuadricula.attach(file, 0, 0, 1, 1)
                    cuadricula.attach(etiqueta, 0, 1, 1, 1)
                cuadricula.show_all()
                flowBox.add(cuadricula)

        barras = Gtk.ScrolledWindow()
        barras.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        barras.add(flowBox)
        self.add(barras)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()