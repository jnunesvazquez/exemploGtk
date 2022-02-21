import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de un Gtk.Label")
        #self.size_request(200,150)

        css_provider=Gtk.CssProvider()
        css_provider.load_from_path("estilo.css")
        contexto=Gtk.StyleContext()
        screen =Gdk.Screen.get_default()
        contexto.add_provider_for_screen(screen, css_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        caixaH=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=6)
        btnVerde=Gtk.Button(label="Verde")
        btnVerde.connect("clicked", self.accionBoton, "verde")
        caixaH.pack_start(btnVerde, False,False,2)

        btnAzul = Gtk.Button(label="Azul")
        btnAzul.connect("clicked", self.accionBoton, "azul")
        caixaH.pack_start(btnAzul, False, False, 2)

        btnRojo = Gtk.Button(label="Rojo")
        btnRojo.connect("clicked", self.accionBoton, "rojo")
        caixaH.pack_start(btnRojo, False, False, 2)

        self.add(caixaH)
        self.connect("destroy",Gtk.main_quit)
        self.show_all()

    def accionBoton(self,boton,color):
        if (color=="verde"):
            self.set_name("windFiestraPrincipal_verde")
        elif(color=="azul"):
            self.set_name("windFiestraPrincipal_azul")
        else:
            self.set_name("windFiestraPrincipal_rojo")

if __name__=="__main__":
    Aplicacion()
    Gtk.main()