import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Window")
        self.set_border_width(5)

        main = Gtk.Notebook()

        menu = Gtk.Box()
        menu.set_border_width(2)
        main.append_page(menu, Gtk.Label(label="MenuWidget1"))

        menu2 = Gtk.Box()
        menu2.set_border_width(2)
        main.append_page(menu2, Gtk.Label(label="MenuWidget2"))

        vBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        hBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        toolbarButton = Gtk.Button.new_with_label("ToolbarButton")
        toolbarChekBox = Gtk.CheckButton(label="ToolbarCheckBox")
        toolbarChekBox.set_active(True)

        hBox.add(toolbarButton)
        hBox.add(toolbarChekBox)
        vBox.add(hBox)

        #Grid
        panelCaption = Gtk.Grid(column_spacing=20, row_spacing=20)
        hBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        #Panel
        panel = Gtk.Box()
        panel.set_border_width(10)
        #Lista
        listBox = Gtk.ListBox()
        for i in range(4):
            label = Gtk.Label(label="Item %s" % (i + 1))
            label.set_hexpand(10)
            label.set_halign(2)
            listBox.add(label)

        hBox.add(listBox)

        #Botones Radio
        vBox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        vBox2.set_halign(1)
        radio = Gtk.RadioButton(label="Radio Button 1")
        vBox2.add(radio)
        for i in range(2):
            radio = Gtk.RadioButton(label="Radio Button %s" % (i + 2))
            radio.props.xalign = 1
            vBox2.add(radio)

        radio = Gtk.RadioButton(label="Inactive Button")
        radio.set_sensitive(False)
        vBox2.add(radio)

        button = Gtk.Button.new_with_label("Button")
        vBox2.add(button)

        hBox.add(vBox2)
        vBox.add(hBox)
        panel.add(vBox)
        panelCaption.attach(panel, 0, 0, 1, 2)

        #Panel 2
        panel2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        panel2.set_border_width(10)

        texto = Gtk.Entry()
        texto.set_text("TextField")
        panel2.add(texto)

        texto = Gtk.Entry()
        texto.set_text("TextField")
        texto.set_visibility(False)
        panel2.add(texto)

        items = Gtk.ComboBoxText()
        for i in range(4):
            items.insert(i, "%s" % i, "Item %s" % (i + 1))

        items.set_active(0)
        panel2.add(items)

        panelCaption.attach_next_to(panel2, panel, Gtk.PositionType.BOTTOM, 1, 2)

        #Panel 4
        panel4 = Gtk.Frame()
        panel4.set_border_width(10)
        scroll = Gtk.ScrolledWindow()
        scroll.set_hexpand(True)
        scroll.set_vexpand(True)
        textview = Gtk.TextView()
        scroll.add(textview)
        panel4.add(scroll)
        panelCaption.attach_next_to(panel4, panel2, Gtk.PositionType.RIGHT, 2, 1)

        # Panel 3
        panel3 = Gtk.Notebook()
        panel3.set_border_width(10)

        tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        checkBox = Gtk.CheckButton(label="UncheckedCheckBox")
        checkBox.set_margin_top(8)
        checkBox.set_margin_left(8)
        checkBox2 = Gtk.CheckButton(label="CheckedCheckBox")
        checkBox2.set_active(True)
        checkBox2.set_margin_top(2)
        checkBox2.set_margin_left(8)
        checkBox3 = Gtk.CheckButton(label="InactiveBox")
        checkBox3.set_sensitive(False)
        checkBox3.set_margin_top(2)
        checkBox3.set_margin_left(8)
        tab.add(checkBox)
        tab.add(checkBox2)
        tab.add(checkBox3)
        panel3.append_page(tab, Gtk.Label(label="Selected Tab"))

        tab2 = Gtk.Box()
        panel3.append_page(tab2, Gtk.Label(label="Other Tab"))

        panelCaption.attach_next_to(panel3, panel4, Gtk.PositionType.TOP, 1, 1)

        menu.add(vBox)
        menu.add(panelCaption)

        self.add(main)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()