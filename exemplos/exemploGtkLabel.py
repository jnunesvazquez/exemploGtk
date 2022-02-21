import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo de uso de Gtk.label")
        self.contador = 0
        #self.set_title("Exemplo de uso de Gtk.Label")
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV_dereita = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        caixaV_esquerda= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        caixaH.pack_start(caixaV_esquerda, True, True, 200)
        caixaH.pack_start(caixaV_dereita, True, True, 200)

        self.etiqueta = Gtk.Label(label="Etiqueta normal")
        caixaV_esquerda.pack_start(self.etiqueta, True, True, 0)

        etiqueta2 = Gtk.Label(label="Etiqueta con texto xustificado a esquerda. \nCon multiples liñas.")
        etiqueta2.set_justify(Gtk.Justification.RIGHT)
        caixaV_dereita.pack_start(etiqueta2, True, True, 0)

        etiqueta3 = Gtk.Label(label="Etiqueta line-wraped "
                             "No coge el ancho "
                             "Puedes poner varios Strings "
                             "Y pueden estar unidos.\n"
                             "Isto permite múltiples paragrafos e engade "
                             "bastantes       expazos extra")
        etiqueta3.set_line_wrap(True)
        etiqueta3.set_max_width_chars(20)
        caixaV_esquerda.pack_start(etiqueta3, True, True, 0)

        etiqueta4 = Gtk.Label(label="Etiqueta line-wraped "
                                    "No coge el ancho "
                                    "Puedes poner varios Strings "
                                    "Y pueden estar unidos.\n"
                                    "Isto permite múltiples paragrafos e engade " 
                                    "bastantes       expazos extra.\n"
                                    "Parragrafo extra longo para facer mais"
                                    "Texto")
        etiqueta4.set_line_wrap(True)
        etiqueta4.set_max_width_chars(20)
        etiqueta4.set_justify(Gtk.Justification.FILL)
        caixaV_dereita.pack_start(etiqueta4, True, True, 0)

        etiqueta5 = Gtk.Label()
        etiqueta5.set_markup(
            "O texto poder ter <small>pequeno</small>, <big>grande</big>, <b>negriña</b>, <i>incursiva</i>, e apuntar cara a"
            '<a href="https://www.gtk.org"'
            'title="Pulsa para saber mais">interrede</a>')
        etiqueta5.set_line_wrap(True)
        etiqueta5.set_max_width_chars(48)
        caixaV_dereita.pack_start(etiqueta5, True, True, 0)
                                #No entiendo
        etiqueta6 = Gtk.Label.new_with_mnemonic("_P_ress Alt + p para seleccionar o boton dereito")
        etiqueta6.set_selectable(True)
        caixaV_dereita.pack_start(etiqueta6, True, True, 0)

        boton = Gtk.Button(label="Pulsa...")
        etiqueta6.set_mnemonic_widget(boton)
        caixaV_dereita.pack_start(boton, True, True, 0)
        boton.connect("clicked", self.accionBoton)

        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def accionBoton(self, boton):
        self.contador += 1
        self.etiqueta.set_text("Numero de pulsaciones " + str(self.contador))


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()