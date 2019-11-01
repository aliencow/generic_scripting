# -*- coding: utf-8 -*-
"""
import base64
print "icon='''\\\n" + base64.encodestring(open("./resources/flecha_close.gif", "rb").read(  )) + "'''"
"""

try:
    import Tkinter as tk
    from Tkinter import ttk
    from Tkinter import PhotoImage, Frame, Label, Widget, messagebox
    from Tkconstants import *
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import PhotoImage, Frame, Label, Widget, messagebox
    from tkinter.constants import *

from random import randint
import os


class Colors():
    def __init__(self):
        self.background = '#444444'
        self.frameBG = '#494949'
        self.label = '#bbbbbb'
        self.buttonBG = '#5d5d5d'
        self.buttonFG = '#eeeeee'
        self.entryBG = '#2b2b2b'

    @property
    def background(self):
        return self.background
    @background.setter
    def background(self, value):
        self.background = value

    @property
    def frameBG(self):
        return self.frameBG
    @frameBG.setter
    def frameBG(self, value):
        self.frameBG = value

    @property
    def label(self):
        return self.label
    @label.setter
    def label(self, value):
        self.label = value

    @property
    def buttonBG(self):
        return self.buttonBG
    @buttonBG.setter
    def buttonBG(self, value):
        self.buttonBG = value

    @property
    def buttonFG(self):
        return self.buttonFG
    @buttonFG.setter
    def buttonFG(self, value):
        self.buttonFG = value

    @property
    def entryBG(self):
        return self.entryBG
    @entryBG.setter
    def entryBG(self, value):
        self.entryBG = value




class Installer():

    def resource_paths(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)



class EditConcat:

    def __init__(self):
        self.window = tk.Tk()
        self.inst = Installer()
        self.colors = Colors()
        self.iconPath = self.inst.resource_paths('./resources/conct_icon.ico')
        #root.iconbitmap('./resources/PB.ico')
        self.window.iconbitmap(self.iconPath)
        self.window.geometry('435x750')
        self.window.configure(bg=self.colors.background)

        self.load_frame = tk.Frame(self.window, width=435, height=150, bg='blue')
        self.load_frame.grid(row=0, column=0)
        self.data_frame = tk.Frame(self.window, width=435, height=600, bg='red')
        self.data_frame.grid(row=1, column=0)
        self.text_data_frame = tk.Frame(self.data_frame, width=100, height=450)
        self.text_data_frame.grid(row=0, column=1)
        self.entry_data_frame = tk.Frame(self.data_frame, width=335, height=450)
        self.entry_data_frame.grid(row=0, column=2)

        self.create_widgets_load()

    def create_widgets_load(self):
        self.load_label = Label(self.load_frame, text="Seleccione una pieza o crea una nueva:", font=("Arial Bold", 12), justify = LEFT, fg=self.colors.label, bg=self.colors.background) #RIGHT #CENTER #LEFT
        self.load_label.pack(fill=X)
        self.combo = ttk.Combobox(self.load_frame, state="readonly")
        #self.combo = ttk.Combobox(self.load_frame)
        self.combo.pack(fill=X)
        self.combo["values"] = ["Python", "C", "C++", "Java"]
        self.combo_label = tk.Label(self.load_frame, text="averdonde", font=('Arial',11), justify=LEFT, fg=self.colors.label, bg=self.colors.background)
        self.combo_label.pack(fill=X)
        self.combo.current(0)


        """
        self.my_counter = ttk.Label(self.window, text="0")
        self.my_counter.grid(row=0, column=0)

        increment_button = ttk.Button(self.window, text="Add 1 to counter")
        increment_button.grid(row=1, column=0)
        increment_button['command'] = self.increment_counter

        quit_button = ttk.Button(self.window, text="Quit")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy
        """
    def increment_counter(self):
        self.my_counter['text'] = str(int(self.my_counter['text']) + 1)

# Create the entire GUI program
program = EditConcat()

# Start the GUI event loop
program.window.mainloop()
