from tkinter import *
import os

cursors = ["arrow","circle","clock","cross","dotbox","exchange","fleur",
            "heart","man","mouse","pirate", "plus", "shuttle","sizing",
            "spider","spraycan","star","target","tcross","trek", "watch"]
# http://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm
class Colors():
    def __init__(self):
        self.background = '#444444'
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

iconPath = inst.resource_paths('resources/PB.ico')
#root.iconbitmap('./resources/PB.ico')
window.iconbitmap(iconPath)
window.geometry('640x480')
window.configure(bg=colors.background)

window.title("Welcome to LikeGeeks app")

label = Label(window, text="Hello papanatas\nque te pasa??", font=("Arial Bold", 12), justify = LEFT, fg=colors.label, bg=colors.background, borderwidth=2) #RIGHT #CENTER #LEFT
#label.grid(column=0, row=0)
label.pack(fill=X)

button = Button(window, text="Click Me",font=("Arial Bold", 20), borderwidth=0, bg=colors.buttonBG, fg=colors.buttonFG, cursor='hand2', justify = CENTER)
#button.grid(column=3, row=1)
button.pack(fill=X)


window.mainloop()
