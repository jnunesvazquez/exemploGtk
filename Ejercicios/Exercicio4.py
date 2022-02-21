import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de NoteBook")
        self.set_border_width(5)

        cartafol = Gtk.Notebook()
        self.entry = Gtk.Entry()

        paxinaXeral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        paxinaXeral.set_border_width(5)
        paxinaXeral.add(Gtk.Label(label=""))
        cartafol.append_page(paxinaXeral, Gtk.Label(label="General"))

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        text = Gtk.Label(label="ID: ")
        text.props.xalign = 0
        caixaH.pack_start(text, True, True, 2)
        caixaH.pack_start(self.entry, True, True, 2)

        paxinaXeral.add(caixaH)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        titulo = Gtk.Label()
        titulo.set_markup("<b>Appearance</b>")
        caixaH.add(titulo)

        paxinaXeral.add(caixaH)

        rede = Gtk.Grid()
        paxinaXeral.pack_start(rede, True, True, 0)
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<i>Etiqueta:</i>")
        rede.add(lblEtiqueta)
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        txvEtiqueta = Gtk.TextView()
        txvEtiqueta.set_size_request(300, 50)
        caixa.pack_start(txvEtiqueta, True, True, 0)
        btnEditarEiqueta = Gtk.Button()
        imaxe = Gtk.Image.new_from_icon_name("preferences-other", Gtk.IconSize.BUTTON)
        btnEditarEiqueta.set_image(imaxe)
        caixa.pack_start(btnEditarEiqueta, True, False, 0)
        rede.attach_next_to(caixa, lblEtiqueta, Gtk.PositionType.RIGHT, 3, 2)

        rbtAtributos = Gtk.RadioButton(label="Atributos:")
        rede.attach(rbtAtributos, 0, 2, 1, 1)
        btnEditarAtributos = Gtk.Button(label="Editar atributos")
        rede.attach_next_to(btnEditarAtributos, rbtAtributos, Gtk.PositionType.RIGHT, 3, 1)

        rbtUsarMArcado = Gtk.RadioButton(label="Usar marcado")
        rede.attach(rbtUsarMArcado, 0, 3, 2, 1)
        rbtPatron = Gtk.RadioButton(label="Patrón")
        rede.attach(rbtPatron, 0, 4, 1, 1)
        txtPatron = Gtk.Entry()
        rede.attach(txtPatron, 2, 4, 2, 1)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        titulo = Gtk.Label()
        titulo.set_markup("<b>Label behaviour</b>")
        caixaH.add(titulo)
        paxinaXeral.add(caixaH)

        rede2 = Gtk.Grid()
        paxinaXeral.pack_start(rede2, True, True, 0)
        btnSelect = Gtk.CheckButton(label="Seleccionable")
        rede2.add(btnSelect)
        btnSub = Gtk.CheckButton(label="Utilizar subrayado")
        rede2.attach(btnSub, 0, 1, 2, 1)
        btnExtra = Gtk.CheckButton(label="Utilizar")
        rede2.attach(btnExtra, 2, 0, 2, 1)
        txtEntry = Gtk.Entry()
        txtEntry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "preferences-other")
        rede2.attach(txtEntry, 2, 1, 2, 1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroGlade.glade")
        caixaGlade = builder.get_object("caixaGlade")
        cmdElipsis = builder.get_object("cmdElipsis")
        paxinaXeral.pack_start(caixaGlade, True, True, 0)

        cmdElipsis.append_text("Start")
        cmdElipsis.append_text("Middle")
        cmdElipsis.append_text("End")

        self.add(cartafol)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()