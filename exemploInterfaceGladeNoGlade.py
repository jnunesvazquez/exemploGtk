import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion:

    def __init__(self):

        wndFiestra = Gtk.Window()
        wndFiestra.set_title("A segunda aplicacion")

        caixaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        print(dir (caixaV.props))
        caixaV.props.border_width = 15
        print(caixaV.get_property("border_width"))
        #caixaV.set_property("orientation", Gtk.Orientation.HORIZONTAL)
        wndFiestra.add(caixaV)

        self.txtNome = Gtk.Entry()
        self.txtNome.set_text("Escriba aqui o teu nome")
        self.txtNome.connect("activate", self.onTxtNomeActivated)
        caixaV.pack_start(self.txtNome, True, False, 6)

        self.lblEtiqueta = Gtk.Label()
        self.lblEtiqueta.set_text("Escribe o teu nome")
        caixaV.pack_start(self.lblEtiqueta, True, True, 6)

        self.btnSaudo = Gtk.Button()
        self.btnSaudo.set_label("Saudo")
        self.btnSaudo.connect("clicked", self.onBtnSaudoClicked)
        caixaV.pack_start(self.btnSaudo, False, False, 6)

        wndFiestra.connect("destroy", Gtk.main_quit)
        wndFiestra.show_all()

        '''builder = Gtk.Builder()
        builder.add_from_file("saudo.glade")

        fiestra = builder.get_object("fiestraPrincipal")

        self.txtNome = builder.get_object("txtSaudo")
        self.btnSaudo = builder.get_object("btnSaudo")
        self.lblTexto = builder.get_object("lblEtiqueta")

        sinais = {"on_fiestraPrincipal_destroy" : Gtk.main_quit,
                  "on_btnSaudo_clicked" : self.onBtnSaudoClicked,
                  "on_txtNome_activated" : self.onTxtNomeActivated
                  }

        builder.connect_signals(sinais)
        fiestra.show_all()'''

    def onBtnSaudoClicked (self, boton):
        self.nombre()

    def onTxtNomeActivated(self, nome):
        self.nombre()

    def nombre(self):
        nome = self.txtNome.get_text()
        self.lblEtiqueta.set_text("Ola " + nome.upper())

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()