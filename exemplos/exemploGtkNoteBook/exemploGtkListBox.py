import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListBoxRowConDatos (Gtk.ListBoxRow):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra
        self.add(Gtk.Label (label=palabra))


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de ListBox")
        self.set_border_width(5)

        caixaExterna = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.add(caixaExterna)

        listaBox = Gtk.ListBox()
        listaBox.set_selection_mode(Gtk.SelectionMode.NONE)
        caixaExterna.pack_start(listaBox, True, True, 0)

        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        etiqueta1 = Gtk.Label(label="Data e hora automática", xalign=0)
        etiqueta2 = Gtk.Label(label="Requiere acceso a interrede2", xalign=0)
        caixaV.pack_start(etiqueta1, True, True, 0)
        caixaV.pack_start(etiqueta2, True, True, 0)
        caixaH.pack_start(caixaV, True, True, 0)
        fila.add(caixaH)

        conmutador = Gtk.Switch()
        conmutador.props.valign = Gtk.Align.CENTER
        caixaH.pack_start(conmutador, False, True, 0)
        listaBox.add(fila)

        fila2 = Gtk.ListBoxRow()
        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(caixaH2)
        etiqueta3 = Gtk.Label(label="Permitir actualizacións automáticas", xalign=0)
        checkActualizacións = Gtk.CheckButton()
        caixaH2.pack_start(etiqueta3, True, True, 0)
        caixaH2.pack_start(checkActualizacións, False, True, 0)

        listaBox.add(fila2)

        fila3 = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila3.add(caixaH)
        lblFormatoData = Gtk.Label(label="Formato data", xalign=0)
        cmbFormatoData = Gtk.ComboBoxText()
        cmbFormatoData.insert(0, "0", "24-hour")
        cmbFormatoData.insert(1, "1", "AM/PM")
        caixaH.pack_start(lblFormatoData, True, True, 0)
        caixaH.pack_start(cmbFormatoData, False, True, 0)

        listaBox.add(fila3)

        listaBox2 = Gtk.ListBox()
        elementos = "Esta é unha ListBox ordeada para mostra".split()
        for elemento in elementos:
            listaBox2.add(ListBoxRowConDatos(elemento))

        def ordear(fila, fila2, datos, notify_destroy):
            return fila.palabra.lower() > fila2.palabra.lower()

        def filtrar(fila, datos, notify_destroy):
            return False if fila.palabra == "ListBox" else True

        listaBox2.set_sort_func(ordear, None, False)
        listaBox2.set_filter_func(filtrar, None, False)
        listaBox2.connect("row-activated", self.on_row_activated)

        caixaExterna.pack_start(listaBox2, True, True, 0)
        listaBox2.show_all()

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_row_activated(self, listBox, fila):
        print(fila.palabra)

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()