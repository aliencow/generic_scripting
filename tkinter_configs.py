# -*- coding: utf-8 -*-

try:
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    from tkinter import *

import os
import base64

class CollapsibleFrame(Frame):
    def __init__(self, master, text=None, borderwidth=2, width=0, height=1, interior_padx=5, interior_pady=5, background=None, caption_separation=1, caption_font=None, caption_builder=None, icon_x=0):
        Frame.__init__(self, master)
        if background is None:
            background = self.cget("background")

        self.configure(background='#5d5d5d', relief = SUNKEN)

        self._is_opened = False

        self._interior_padx = interior_padx
        self._interior_pady = interior_pady

        self._iconOpen = PhotoImage(data= base64.encodestring(open("./resources/flecha_open.gif", "rb").read(  )))
        self._iconClose = PhotoImage(data=base64.encodestring(open("./resources/flecha_close.gif", "rb").read(  )))
        #self._iconOpen = PhotoImage(data="R0lGODlhEAAQAKIAAP///9TQyICAgEBAQAAAAAAAAAAAAAAAACwAAAAAEAAQAAADNhi63BMgyinFAy0HC3Xj2EJoIEOM32WeaSeeqFK+say+2azUi+5ttx/QJeQIjshkcsBsOp/MBAA7")
        #self._iconClose = PhotoImage(data="R0lGODlhEAAQAKIAAP///9TQyICAgEBAQAAAAAAAAAAAAAAAACwAAAAAEAAQAAADMxi63BMgyinFAy0HC3XjmLeA4ngpRKoSZoeuDLmo38mwtVvKu93rIo5gSCwWB8ikcolMAAA7")

        height_of_icon = max(self._iconOpen.height(), self._iconClose.height())
        width_of_icon = max(self._iconOpen.width(), self._iconClose.width())

        containerFrame_pady = (height_of_icon) +1

        self._height = height
        self._width = width

        self._containerFrame = Frame(self, borderwidth=borderwidth, width=width*2, height=height, relief=None, background='#494949')
        self._containerFrame.pack(expand=True, fill=X, pady=(containerFrame_pady,0))

        self.interior = Frame(self._containerFrame, background='#494949')

        self._collapseButton = Label(self, borderwidth=0, image=self._iconOpen, relief=RAISED, background='#5d5d5d')
        self._collapseButton.place(in_= self._containerFrame, x=icon_x, y=-(height_of_icon+1), anchor=N+W, bordermode="ignore")
        self._collapseButton.bind("<Button-1>", lambda event: self.toggle())

        if caption_builder is None:
            self._captionLabel = Label(self, anchor=N, borderwidth=1, text=text, background='#5d5d5d', fg='#bbbbbb')
            if caption_font is not None:
                self._captionLabel.configure(font=caption_font)
        else:
            self._captionLabel = caption_builder(self)

            if not isinstance(self._captionLabel, Widget):
                raise Exception("'caption_builder' doesn't return a tkinter widget")

        self.after(0, lambda: self._place_caption(caption_separation, icon_x, width_of_icon))

    def update_width(self, width=None):
        # Update could be devil
        # http://wiki.tcl.tk/1255
        self.after(0, lambda width=width:self._update_width(width))

    def _place_caption(self, caption_separation, icon_x, width_of_icon):
        self.update()
        x = caption_separation + icon_x + width_of_icon
        y = -(self._captionLabel.winfo_reqheight()+2)

        self._captionLabel.place(in_= self._containerFrame, x=x, y=y, anchor=N+W, bordermode="ignore")

    def _update_width(self, width):
        self.update()
        if width is None:
            width=self.interior.winfo_reqwidth()

        if isinstance(self._interior_pady, (list, tuple)):
            width += self._interior_pady[0] + self._interior_pady[1]
        else:
            width += 2*self._interior_pady

        width = max(self._width, width)

        self._containerFrame.configure(width=width)

    def open(self):
        self._collapseButton.configure(image=self._iconClose)

        self._containerFrame.configure(height=self.interior.winfo_reqheight())
        self.interior.pack(expand=True, fill=X, padx=self._interior_padx, pady =self._interior_pady)

        self._is_opened = True

    def close(self):
        self.interior.pack_forget()
        self._containerFrame.configure(height=self._height)
        self._collapseButton.configure(image=self._iconOpen)

        self._is_opened = False

    def toggle(self):
        if self._is_opened:
            self.close()
        else:
            self.open()


cursors = ["arrow","circle","clock","cross","dotbox","exchange","fleur",
            "heart","man","mouse","pirate", "plus", "shuttle","sizing",
            "spider","spraycan","star","target","tcross","trek", "watch"]
# http://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm

reliefs = [FLAT,RAISED,SUNKEN,GROOVE,RIDGE]

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



colors = Colors()
inst = Installer()

window = Tk()

iconPath = inst.resource_paths('./resources/conct_icon.ico')
#root.iconbitmap('./resources/PB.ico')
window.iconbitmap(iconPath)
window.geometry('640x480')
window.configure(bg=colors.background)

window.title("Welcome to LikeGeeks app")

label = Label(window, text="Hello papanatas\nque te pasa??", font=("Arial Bold", 12), justify = LEFT, fg=colors.label, bg=colors.background, borderwidth=2) #RIGHT #CENTER #LEFT
#label.grid(column=0, row=0)
label.pack(fill=X)

button = Button(window, text="Click Me",font=("Arial Bold", 20), borderwidth=0, bg='DarkGray', fg=colors.buttonFG, cursor='hand2', pady=5, justify = CENTER)
#button.grid(column=3, row=1)
button.pack(fill=X, padx=2, pady=1)




cf1 = CollapsibleFrame(window, text ="Esta es una prueba", interior_padx=5)
cf1.pack(fill=X,padx=2, pady=1)
for i in range(3):
    #Button(cf1.interior, text="button %s"%i).pack(fill=X, padx=5)
    Button(cf1.interior, text="Click Me", borderwidth=0, bg='DarkGray', font=("Arial Bold", 9), fg=colors.buttonFG, cursor='hand2',  pady=5, justify = CENTER).pack(fill=X, padx=2, pady=1)

window.mainloop()
