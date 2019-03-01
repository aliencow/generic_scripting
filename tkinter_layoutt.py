#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

import base64

""" Sample layout
|-------------------------------------------------------|
| LOGO                           Nombre App u otra info.|
|-------------------------------------------------------|
| COMBO BOX          | Entry    | But Open  | But New   |
|-------------------------------------------------------|
|        Label info sobre la pieza seleccionada			|
|-------------------------------------------------------|
|                   Label 1 | Entry 1                   |
|                   Label 2 | Entry 2                   |
|                   Label 3 | Entry 3                   |
|                       ... | ...                       |
|                   Label n | Entry n                   |
|-------------------------------------------------------|
|                        But SAVE                       |
|-------------------------------------------------------|
"""

class Application(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(5):
            self.master.rowconfigure(r, weight=1)

        self.header_init()
        self.info_init()
        self.resto_init()

    def header_init(self):
        """ HEADER SETUP
        """
        fr_header = tk.Frame(self.master, bg="red") #cabeecera
        fr_header.grid(row = 0, column = 0, rowspan = 1, columnspan = 2, sticky = 'WENS')

        logo = tk.PhotoImage(file="resources/flecha_close.gif") # poner el path correcot
        logo = tk.PhotoImage(data=base64.encodestring(open("./resources/mole.gif", "rb").read(  )))
        lbl_logo = tk.Label(fr_header, image=logo).grid(row=0, column=0, sticky = 'WNS')
        lbl_titulo = tk.Label(fr_header, text='ConCatenator for ffmpeg videos - AOM', justify=tk.RIGHT).grid(row=0, column=2, sticky = 'WENS', pady=5)

    def info_init(self):
        """ INFORMACION SETUP
        """
        fr_select_pieza = tk.Frame(self.master, bg="red") #zona informacion de la pieza
        fr_select_pieza.grid(row = 1, column = 0, rowspan = 1, columnspan = 2, sticky = 'WENS')
        for c in range(5):
            fr_select_pieza.columnconfigure(c, weight=1)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        combo = ttk.Combobox(fr_select_pieza, state="readonly", postcommand=self.dummy).grid(row=1, column=0, columnspan=2, sticky='WE', pady=5)
        combo["values"] = ("EP111", "EP109", "N103", "N101")
        """ Acceso al combo box
        combo["values"] = ["Python", "C", "C++", "Java"]  #hay que asignarle valores
        value = self.combo.get() # obtener valor activo
        index = self.combo.current() #obtener el índice
        self.combo.set("Python") self.combo.current(2) #  set opcion activa
        values = self.combo["values"] # get de toda la lista
        # añadir elemento
        values = list(self.combo["values"])
        self.combo["values"] = values + ["Nuevo elemento"]
        # Vaciar lista.
        self.combo["values"] = []
        """
        ent_pieza = tk.Entry(fr_select_pieza).grid(row=1, column=2, columnspan=1, sticky='WE', pady=5,padx=5)

        button = tk.Button(fr_select_pieza, text='Stop', width=25, command=self.dummy)

        but_open_pieza = tk.Button(fr_select_pieza, text='Open', command=self.dummy).grid(row=1, column=3, columnspan=1, sticky='WE', pady=5, padx=5)
        but_new_pieza = tk.Button(fr_select_pieza, text='Open', command=self.dummy).grid(row=1, column=4, columnspan=1, sticky='WE', pady=5 , padx=5)

    def resto_init(self):

        fr_labels_pieza = tk.Frame(self.master, bg="blue") #columna etiqueta
        fr_labels_pieza.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, sticky ='EWNS')

        fr_contents_pieza = tk.Frame(self.master, bg="green") #columna contenido
        fr_contents_pieza.grid(row = 2, column = 1, rowspan = 1, columnspan = 1, sticky = 'EWNS')

        fr_footer = tk.Frame(self.master, bg="red") #row para footer
        fr_footer.grid(row = 3, column = 0, rowspan = 1, columnspan = 2, sticky = 'EWNS')

    def dummy(self):
        print 'rutina dummy'




root = tk.Tk()
#root.geometry("400x200+200+200")
app = Application(master=root)
app.mainloop()
