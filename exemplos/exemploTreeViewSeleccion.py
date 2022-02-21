import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con seleccion")
        self.set_border_width(5)
        self.set_default_size(300, 300)

        self.filtro_actual_linguaxe = "None"

        programas = Gtk.ListStore (str, int, str)
        programas.append(["FireFox", 2002, "C++"])
        programas.append(["Eclipse", 2004, "Java"])
        programas.append(["Netbeans", 1996, "Java"])
        programas.append(["Bazaar", 2005, "Python"])
        programas.append(["GCC", 1987, "C"])
        programas.append(["Git", 2012, "C++"])
        programas.append(["Kernel Linux", 1991, "C"])
        programas.append(["Sphinx", 2003, "Python"])

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)

        self.filtroLinguaxe = programas.filter_new()
        self.filtroLinguaxe.set_visible_func(self.filtro_lenguaxe)

        # Con este filtro, al pulsar un boton del lenguaje puedes mostrar solo los programas con el lenguaje seleccionado
        #trvVistaProgramas = Gtk.TreeView(model=self.filtroLinguaxe)
        # Con este filtro, al pulsar el texto de ano puedes filtrar los programas por año
        trvVistaProgramas = Gtk.TreeView(model=programas)

        for i, tituloColumna in enumerate (["Software", "Ano", "Linguaxe de programacion"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text = i)
            trvVistaProgramas.append_column(columna)
            if i == 1:
                columna.set_sort_column_id(1)

        programas.set_sort_func(1, self.ordear_por_ano, None)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 3, 8)
        scroll.add(trvVistaProgramas)

        filtroJava = Gtk.Button(label="Java")
        filtroC = Gtk.Button(label="C")
        filtroCMM = Gtk.Button(label="C++")
        filtroPython = Gtk.Button(label="Python")
        senfiltro = Gtk.Button(label="None")

        filtroJava.connect("clicked", self.on_botonSeleccion_clicked)
        filtroC.connect("clicked", self.on_botonSeleccion_clicked)
        filtroCMM.connect("clicked", self.on_botonSeleccion_clicked)
        filtroPython.connect("clicked", self.on_botonSeleccion_clicked)
        senfiltro.connect("clicked", self.on_botonSeleccion_clicked)

        self.software = Gtk.Entry()
        softwareLabel = Gtk.Label(label="Software")
        self.ano = Gtk.Entry()
        anoLabel = Gtk.Label(label="Ano")
        self.linguaxe = Gtk.Entry()
        linguaxeLabel = Gtk.Label(label="Linguaxe de programacion")
        self.btnModificar = Gtk.Button(label="Modificar")


        seleccion = trvVistaProgramas.get_selection()
        seleccion.connect("changed", self.on_trvVistaProgramas_changed, self.software, self.ano, self.linguaxe)

        grid.attach_next_to(softwareLabel, scroll, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(anoLabel, softwareLabel, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(linguaxeLabel, anoLabel, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(self.software, softwareLabel, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(self.ano, anoLabel, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(self.linguaxe, linguaxeLabel, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(self.btnModificar, self.software, Gtk.PositionType.RIGHT, 1, 2)

        grid.attach_next_to(filtroJava, linguaxeLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(filtroC, filtroJava, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroCMM, filtroC, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroPython, filtroCMM, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(senfiltro, filtroPython, Gtk.PositionType.RIGHT, 1, 1)

        self.btnModificar.connect("clicked", self.on_button_clicked, seleccion)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_trvVistaProgramas_changed(self, selec, label, label2, label3):
        modelo, punteiro = selec.get_selected()
        if punteiro is not None:
            self.software.set_text(modelo [punteiro][0])
            self.ano.set_text(str(modelo [punteiro][1]))
            self.linguaxe.set_text(modelo [punteiro][2])
            self.btnModificar.set_sensitive(True)

    def on_button_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        modelo [fila][0] = self.software.get_text()
        modelo[fila][1] = int(self.ano.get_text())
        modelo[fila][2] = self.linguaxe.get_text()
        self.btnModificar.set_sensitive(False)

    def on_botonSeleccion_clicked(self, boton):
        self.filtro_actual_linguaxe = boton.get_label()
        self.filtroLinguaxe.refilter()


    def filtro_lenguaxe(self, modelo, fila, datos):
        if self.filtro_actual_linguaxe == "None":
            return True
        else:
            return modelo[fila][2] == self.filtro_actual_linguaxe

    def ordear_por_ano(self, modelo, fila1, fila2, datos_usuario):
        columna, _ = modelo.get_sort_column_id()
        ano1 = modelo.get_value(fila1, columna)
        ano2 = modelo[fila2][columna]
        if ano1 < ano2:
            return -1
        elif ano1 == ano2:
            return 0
        else:
            return 1


if __name__=="__main__":
    Aplicacion()
    Gtk.main()