import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con TreeStore")
        self.set_border_width(5)
        # Creo el modelo
        modelo = Gtk.TreeStore(str, int, str, bool)
        for avo in range(5):
            punteiroAvo = modelo.append(None, ['Avó', avo, "Sen datos", False])
            for pai in range(4):
                punteiroPai = modelo.append(punteiroAvo, ['Pai', pai, "Lexítimo", False])
                for fillo in range(6):
                    punteiroFillo = modelo.append(punteiroPai, ['Fillo', fillo, "Lexitimo", True])

        trvArboreXeneraloxico = Gtk.TreeView(model=modelo)

        # Columna 1
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_cell_changed, modelo)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)

        # Columna 2
        trvColumna = Gtk.TreeViewColumn("Orde")
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        # Columna 3
        tipoParentesco = Gtk.ListStore(str)
        tipoParentesco.append(["Sen datos"])
        tipoParentesco.append(["Lexítimo"])
        tipoParentesco.append(["Bastardo"])

        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)
        celdaCombo.set_property("model", tipoParentesco)
        celdaCombo.set_property("text-column", 0)
        celdaCombo.set_property("has-entry", False)
        celdaCombo.connect("edited", self.on_combo_changed, modelo)
        trvColumnaCombo = Gtk.TreeViewColumn("Combo", celdaCombo, text=2)
        trvArboreXeneraloxico.append_column(trvColumnaCombo)

        #Columna 4

        celdaCheck = Gtk.CellRendererToggle()
        celdaCheck.set_property("activatable", True)
        trvColumnaCheck = Gtk.TreeViewColumn("Vida")
        trvArboreXeneraloxico.append_column(trvColumnaCheck)
        celdaCheck.connect("toggled", self.on_cell_toggled, modelo)
        trvColumnaCheck.pack_start(celdaCheck, True)
        trvColumnaCheck.add_attribute(celdaCheck, "active", 3)

        self.add(trvArboreXeneraloxico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_combo_changed(self, control, fila, texto, modelo):
        modelo[fila][2] = texto

    def on_cell_changed(self, control, fila, texto, modelo):
        modelo[fila][0] = texto

    def on_cell_toggled(self, control, fila, modelo):
        modelo[fila][3] = not modelo[fila][3]

if __name__=="__main__":
    Aplicacion()
    Gtk.main()