#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

import base64


import tkFont
#from tkinter import font



class Colors():
    def __init__(self):
        self.bgtitulo ='#626262'
        self.fgtitulo ='#dcdcdc'
        self.background = '#444444'
        self.frameBG = '#494949'
        self.label = '#bbbbbb'
        self.buttonBG = '#5d5d5d'
        self.buttonFG = '#eeeeee'
        self.entryBG = '#2b2b2b'



""" Sample layout
https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid

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



class Interface(tk.Frame):

    def __init__(self, master=None, title='Concatenator v1.5'):
        tk.Frame.__init__(self, master)
        self.grid()
<<<<<<< HEAD:tkinter/tkinter_layout.py
        self.master.title("Grid Manager")
        self.master.iconbitmap('../resources/conct_icon.ico')
=======
        self.master.title(title)
        self.master.iconbitmap('resources/concatenator.ico')
>>>>>>> 80b76e22f62f363e9918bd1f783ea402ed736aab:tkinter_layout.py
        self.master.resizable(False, True)


        self.colors = Colors()
        self.normalfont = tkFont.Font(family='Helvetica', size=9)
        self.tittlefont = tkFont.Font(family='Helvetica', size=11, weight='bold')
        self.mediumfont = tkFont.Font(family='Helvetica', size=10)



        self.ent_pieza_value = tk.StringVar()
        self.valores_combo = ["EP111", "EP109", "N103", "N101"]


        self.fr_header = tk.Frame(self.master, bg=self.colors.bgtitulo) #cabeecera
        self.fr_select_pieza = tk.Frame(self.master, bg=self.colors.frameBG) #zona informacion de la pieza
        self.fr_datos_pieza = tk.Frame(self.master,bg=self.colors.frameBG) #columna etiqueta
        self.fr_footer = tk.Frame(self.master, bg=self.colors.frameBG) # footer


        for r in range(4):#Configurar numero de filas
            self.master.rowconfigure(r, weight=0)


        self.fr_header.grid(row = 0, sticky = 'WENS')
        self.fr_select_pieza.grid(row = 1, sticky = 'WENS')
        self.fr_datos_pieza.grid(row = 2, sticky ='EWNS')
        self.fr_footer.grid(row = 3, sticky ='EWNS')


        self.header_init()
        self.info_init()
        self.detalle_init()
        self.footer_init()

    def header_init(self):
        """ HEADER SETUP
            Configuración grafica de la sección Header:
            logo e imagen
        """
        self.fr_header.columnconfigure(0, weight=0, minsize=32)
        self.fr_header.columnconfigure(1, weight=0, minsize=417)


        #logo = tk.PhotoImage(file="F:/proyectos_python/generic_scriptingresources/flecha_close.gif") # poner el path correcot
<<<<<<< HEAD:tkinter/tkinter_layout.py
        logo = tk.PhotoImage(data=base64.encodestring(open("../resources/conct_iconc.gif", "rb").read()))
=======
        logo = tk.PhotoImage(data=base64.encodestring(open("resources/concatenator.gif", "rb").read()))
>>>>>>> 80b76e22f62f363e9918bd1f783ea402ed736aab:tkinter_layout.py
        #logo = logo.subsample(2,2) #la mitad
        lbl_logo = tk.Label(self.fr_header, image=logo, bg=self.colors.bgtitulo)
        lbl_logo.image = logo
        lbl_logo.grid(row=0, column=0, sticky = 'EWNS', pady=5, padx=5)

        lbl_titulo = tk.Label(self.fr_header, text='ConCatenator for ffmpeg videos - AOM', font=self.tittlefont, bg=self.colors.bgtitulo, fg=self.colors.fgtitulo)
        lbl_titulo.grid(row=0, column=1, columnspan=1, sticky = 'WS', pady=3, padx=5)

    def info_init(self):
        """ INFORMACION SETUP
        """

        for r in range(2):#Configurar numero de filas
            self.fr_select_pieza.rowconfigure(r, weight=0)
        for c in range(4):
            self.fr_select_pieza.columnconfigure(c, weight=1, minsize=50)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)


        lbl_entry = tk.Label(self.fr_select_pieza, text='Piece selected', font=self.normalfont, bg=self.colors.frameBG, fg=self.colors.fgtitulo)
        lbl_entry.grid(row=0, column=2, columnspan=1, sticky='W', pady=3)

        self.ent_pieza = tk.Entry(self.fr_select_pieza, text='', textvariable=self.ent_pieza_value, bg=self.colors.entryBG, fg=self.colors.buttonFG, relief = tk.FLAT)
        self.ent_pieza.grid(row=1, column=2, columnspan=1, sticky='WE', pady=5,padx=5)

        lbl_combo = tk.Label(self.fr_select_pieza, text='Piece list', font=self.normalfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo)
        lbl_combo.grid(row=0, column=0, columnspan=2, sticky='W', pady=3, padx=5)


        self.combo_piezas = ttk.Combobox(self.fr_select_pieza, state="readonly", postcommand=self.dummy, values=self.valores_combo)
        self.combo_piezas.grid(row=1, column=0, columnspan=2, sticky='WE', pady=5, padx=5)
        self.combo_piezas.bind("<<ComboboxSelected>>", self.get_project_from_combo)
        self.combo_piezas.current(0)

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

        lbl_buttons = tk.Label(self.fr_select_pieza, text='Operations', font=self.normalfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo)
        lbl_buttons.grid(row=0, column=3, columnspan=2, sticky='W', pady=3, padx=5)

        but_open_pieza = tk.Button(self.fr_select_pieza, text='Open', command=self.dummy, borderwidth=0, bg=self.colors.buttonBG,  fg=self.colors.buttonFG, pady=0, padx = 5)
        but_open_pieza.grid(row=1, column=3, columnspan=1, sticky='WE', pady=5, padx=5)

        but_new_pieza = tk.Button(self.fr_select_pieza, text='New', command=self.dummy, borderwidth=0, bg=self.colors.buttonBG, fg=self.colors.buttonFG, pady=0, padx = 5)
        but_new_pieza.grid(row=1, column=4, columnspan=1, sticky='WE', pady=5 , padx=5)





    def detalle_init(self):
        """ DETALLE SETUP
        """
        lbl_titulonext = tk.Label(self.fr_datos_pieza, text='Selection details:', font=self.mediumfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo)
        lbl_titulonext.grid(row=0, column=0, columnspan=5, sticky = 'W', pady=3, padx=5)


        fr_labels = tk.Frame(self.fr_datos_pieza, bg=self.colors.frameBG, width=250) #columna contenido
        fr_labels.grid(row = 1, column = 0, rowspan = 1,  sticky = 'EWNS')

        fr_labels.columnconfigure(0, weight=1, minsize = 150)

        lbl_buttons = tk.Label(fr_labels, text='Campito:', font=self.normalfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo, pady=0)
        lbl_buttons.grid(row=0, column=0, sticky='E', pady=5, padx=2)
        lbl_buttons = tk.Label(fr_labels, text='Campito:', font=self.normalfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo, pady=0)
        lbl_buttons.grid(row=1, column=0, sticky='E', pady=5, padx=2)
        lbl_buttons = tk.Label(fr_labels, text='Campito:', font=self.normalfont,  bg=self.colors.frameBG, fg=self.colors.fgtitulo, pady=0)
        lbl_buttons.grid(row=2, column=0, sticky='E', pady=5, padx=2)


        fr_contents_pieza = tk.Frame(self.fr_datos_pieza, bg=self.colors.frameBG, width=250) #columna contenido
        fr_contents_pieza.grid(row = 1, column = 1, rowspan = 1,  sticky = 'EWNS')
        fr_contents_pieza.columnconfigure(0, weight=1, minsize=300)


        ent_pieza = tk.Entry(fr_contents_pieza, text='', textvariable=self.ent_pieza_value, bg=self.colors.entryBG, fg=self.colors.buttonFG, relief = tk.FLAT)
        ent_pieza.grid(row=0, column=0, columnspan=6, sticky='EW', pady=5, padx=5)
        but_dir = tk.Button(fr_contents_pieza, text='...', command=self.dummy, borderwidth=0, bg=self.colors.buttonBG,  fg=self.colors.buttonFG, pady=0, padx = 2)
        but_dir.grid(row=0, column=1, columnspan=1, sticky='WE', pady=5, padx=5)

        ent_pieza = tk.Entry(fr_contents_pieza, text='', textvariable=self.ent_pieza_value, bg=self.colors.entryBG, fg=self.colors.buttonFG, relief = tk.FLAT)
        ent_pieza.grid(row=1, column=0, columnspan=6, sticky='EW', pady=5, padx=5)
        but_dir = tk.Button(fr_contents_pieza, text='...', command=self.dummy, borderwidth=0, bg=self.colors.buttonBG,  fg=self.colors.buttonFG, pady=0, padx = 2)
        but_dir.grid(row=1, column=1, columnspan=1, sticky='WE', pady=5, padx=5)

        ent_pieza = tk.Entry(fr_contents_pieza, text='', textvariable=self.ent_pieza_value, bg=self.colors.entryBG, fg=self.colors.buttonFG, relief = tk.FLAT)
        ent_pieza.grid(row=2, column=0, columnspan=6, sticky='EW', pady=5, padx=5)

    def footer_init(self):
        """ DETALLE SETUP
        """
        self.fr_footer.columnconfigure(0, weight=1)

        but_footer = tk.Button(self.fr_footer, text='SAVE', command=self.dummy, borderwidth=0, bg=self.colors.buttonBG,  fg=self.colors.buttonFG, font=self.tittlefont)
        but_footer.grid(row=0, column=0, columnspan=2, sticky='WE', pady=2, padx=1)


    def dummy(self):
        print 'rutina dummy'

    def get_project_from_combo(self, event):
        value = self.combo_piezas.get()
        self.ent_pieza_value.set(value)

    def get_ent_pieza_value(self):
        return self.ent_pieza_value.get()




root = tk.Tk()
#root.geometry("400x200+200+200")
app = Interface(master=root)
app.mainloop()
