import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de un Gtk.Label")
        self.set_size_request(200,150)

        self.temporizador = None

        caixaV=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(caixaV)

        self.txtTexto=Gtk.Entry()
        self.txtTexto.set_width_chars(30)
        self.txtTexto.set_text("Benvidos")
        caixaV.pack_start(self.txtTexto,True,True,0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        caixaV.pack_start(caixaH, True, True, 0)

        self.chkEditable=Gtk.CheckButton(label="Editable")
        self.chkEditable.connect("toggled", self.on_chkEditable_toggled)
        self.chkEditable.set_active(True)
        caixaH.pack_start(self.chkEditable, True, True, 0)

        self.chkVisible = Gtk.CheckButton(label="Visible")
        self.chkVisible.connect("toggled", self.on_chkVisible_toggled)
        self.chkVisible.set_active(True)
        caixaH.pack_start(self.chkVisible, True, True, 0)

        self.chkPulso = Gtk.CheckButton(label="Pulso")
        self.chkPulso.connect("toggled", self.on_chkPulso_toggled)
        self.chkPulso.set_active(True)
        caixaH.pack_start(self.chkPulso, True, True, 0)

        self.chkIcono = Gtk.CheckButton(label="Icono")
        self.chkIcono.connect("toggled", self.on_chkIcono_toggled)
        self.chkIcono.set_active(True)
        caixaH.pack_start(self.chkIcono, True, True, 0)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

    def on_chkEditable_toggled(self,control):
        estado=control.get_active()
        self.txtTexto.set_editable(estado)

    def on_chkVisible_toggled(self,control):
        estado=control.get_active()
        self.txtTexto.set_visibility(estado)

    def on_chkPulso_toggled(self,control):
        if control.get_active():
            self.txtTexto.set_progress_pulse_step(0.2)
            self.temporizador = GLib.timeout_add(200, self.facer_pulso, None)
        else:
            GLib.source_remove(self.facer_pulso)
            self.temporizador = None
            self.txtTexto.set_progress_pulse_step(0)

    def facer_pulso(self, datos_usuario):
        self.txtTexto.progress_pulse()
        return True

    def on_chkIcono_toggled(self, control):
        if control.get_active():
            nome_icono = "system-search-symbolic"
        else:
            nome_icono = None
        self.txtTexto.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, nome_icono)



if __name__=="__main__":
    Aplicacion()
    Gtk.main()