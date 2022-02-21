import sqlite3 as dbapi
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con TreeStore")
        self.set_border_width(5)

        '''
        print(dbapi.apilevel)     #para ver version de la api
        print(dbapi.threadsafety) #nos indica la facilidad de uso de hilos 0 no se sincroniza, 1 compartir modulo pero no
                                  #compartir conexiones 2 se comparten modulos y conexiones y 3 permite to-do
        print(dbapi.paramstyle)   #Utiliza el ? para evitar el injection sql
        '''

        """
        Standar Error
            warning
            Error
                Inteface Error
                DataBase Error
                    Data Error
                    Operational Error
                    Integrity Error
                    Internal Error
                    Programing Error
                    Not Supported Error
        """

        modelo = Gtk.TreeStore(str, str, str)

        try:
            bbdd = dbapi.connect("baseDatos.dat")
            cursor = bbdd.cursor()
            #cursor.execute("CREATE TABLE usuarios (dni text,nome text, direccion text)")
            #cursor.execute("INSERT INTO usuarios VALUES('54427746V','Brais Martinez Paredes','Avd Portanet')")
            #bbdd.commit()
            #cursor.execute("INSERT INTO usuarios VALUES('69696969S','Joel Nunes','Pardarilla')")
            #bbdd.commit()
            cursor.execute("SELECT * FROM usuarios")

            for rexistro in cursor.fetchall():
                print("Nombre: " + rexistro[1] + ", DNI: " + rexistro[0] + " Direccion: " + rexistro[2])
                modelo.append(None, [rexistro[1], rexistro[0], rexistro[2]])

        except dbapi.DatabaseError as e:
            print("Erro na base de datos: " + str(e))

        trvArboreXeneraloxico = Gtk.TreeView(model=modelo)

        trvColumna = Gtk.TreeViewColumn('Nombre')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)

        trvColumna = Gtk.TreeViewColumn('DNI')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        trvColumna = Gtk.TreeViewColumn('Direccion')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 2)

        self.add(trvArboreXeneraloxico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()