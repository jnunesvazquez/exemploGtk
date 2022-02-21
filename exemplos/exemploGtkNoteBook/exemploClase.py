import gi
import os
import gridConBotons

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de Clase panel del Glade")
        self.set_border_width(5)

        noteBook = Gtk.Notebook()
        self.add(noteBook)

        cajav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(cajav, Gtk.Label(label="Xeral"))
        cajav1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(cajav1, Gtk.Label(label="Empaquetado"))
        cajav2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(cajav2, Gtk.Label(label="Común"))
        cajav3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(cajav3, Gtk.Label(label="Sinais"))

        cajah = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        lblId= Gtk.Label(label="ID:")
        lblId.props.xalign=0

        self.entradaTexto= Gtk.Entry()
        cajah.pack_start(lblId, True, True, 2)
        cajah.pack_start(self.entradaTexto, True, True, 2)
        cajav.pack_start(cajah,True,True,0)
        lblApariencia = Gtk.Label()
        lblApariencia.set_markup("<b>Apariencia</b>")
        lblApariencia.props.xalign=0
        cajav.pack_start(lblApariencia,True,True,2)
        rede=Gtk.Grid()
        cajav.pack_start(rede,True,True,0)
        lblEtiqueta=Gtk.Label(label="Etiqueta:")
        lblEtiqueta.set_markup("<i>Etiqueta:</i>")
        rede.add(lblEtiqueta)
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        txvEtiqueta=Gtk.TextView()
        self.buferTxvEtiqueta = txvEtiqueta.get_buffer()
        txvEtiqueta.set_size_request(300,50)
        caixa.pack_start(txvEtiqueta,True,True,0)
        btnEditarEtiqueta = Gtk.Button()
        btnEditarEtiqueta.connect("clicked", self.on_btn_EditarEtiqueta_clicked)
        #icono = Gio.ThemedIcon("preferences-other")
        imaxe= Gtk.Image.new_from_icon_name("preferences-other",Gtk.IconSize.BUTTON)
        btnEditarEtiqueta.set_image(imaxe)
        caixa.pack_start(btnEditarEtiqueta,True,False,0)
        rede.attach_next_to(caixa,lblEtiqueta,Gtk.PositionType.RIGHT,3,2)
        rbtAtributos=Gtk.RadioButton(label="Atributos:")
        rede.attach(rbtAtributos,0,2,1,1)
        btnEditarAtributos=Gtk.Button(label="Editar Atributos")
        rede.attach_next_to(btnEditarAtributos,rbtAtributos,Gtk.PositionType.RIGHT,3,1)
        rbtUsarMarcado= Gtk.RadioButton(label="Usar marcado")
        rede.attach(rbtUsarMarcado,0,3,2,1)
        rbtPatron=Gtk.RadioButton(label="Patron")
        rede.attach(rbtPatron,0,4,1,1)
        txtPatron=Gtk.Entry()
        rede.attach(txtPatron,2,4,2,1)
        lblComportamiento= Gtk.Label()
        lblComportamiento.set_markup("<b>Comportamiento da etiqueta</b>")
        lblComportamiento.props.xalign = 1
        cajav.pack_start(lblComportamiento, True, True, 2)
        rede = Gtk.Grid()
        cajav.pack_start(rede, True, True, 0)
        cBox=Gtk.CheckButton(label="Seleccionable")
        rede.add(cBox)
        cBox2 = Gtk.CheckButton(label="Rexistrar as ligazons visitadas")
        rede.attach_next_to(cBox2,cBox,Gtk.PositionType.RIGHT,1,1)
        cBox3 = Gtk.CheckButton(label="Usar subliñado")
        rede.attach(cBox3, 0, 1, 1, 1)
        txtComportamento = Gtk.Entry()
        rede.attach_next_to(txtComportamento,cBox3,Gtk.PositionType.RIGHT,1,1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroGlade.glade")
        caixaGlade = builder.get_object ("caixaGlade")
        cmdElipsis = builder.get_object("cmdElipsis")
        sinais = {"on_cmdElipsis_changed":self.on_cmdElipsis_changed}
        builder.connect_signals(sinais)
        cajav.pack_start(caixaGlade,True,True,0)
        cmdElipsis.append_text("Start")
        cmdElipsis.append_text("Midle")
        cmdElipsis.append_text("End")
        self.connect("destroy",Gtk.main_quit)
        self.show_all()

    def on_cmdElipsis_changed(self,control):
        self.entradaTexto.set_text(control.get_active_text())
        punteiro = self.buferTxvEtiqueta.get_end_iter()
        self.buferTxvEtiqueta.insert(punteiro, control.get_active_text() + "\n")

    def on_btn_EditarEtiqueta_clicked(self,boton):
        self.entradaTexto.set_text("Boton pulsado")

if __name__=="__main__":
    Aplicacion()
    Gtk.main()