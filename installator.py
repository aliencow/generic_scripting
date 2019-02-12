import glob
import os
import socket
import getpass

from aux_tools import *

"""
    for filename in glob.iglob('src/**/*.c', recursive=True):
        print(filename)
    1 - get user name
    2 - get maya 2018 base path
    3 - Check if mayabase path exists - if not exit with message
    4 - Check if plug-ins path exists - if not create
    5 - Check if scripts exists - if not create
    6 - Copy each file to each place. Check errors

"""


class Installator():
    """ Clase para realizar la instalación de plug-ins o scripts en
        Maya2018
    """
    def __init__(self, installationList):
        """
        Inicializamos el instalador
        Leemos la configuración del la lista installationList
        """
        self.installList = installtionList
        self.userName = getpass.getuser()
        self.baseMayaPath = 'C:/Users/' + self.userName + '/documents/maya/2018'
        pluginsPath = self.baseMayaPath + 'plug-ins'
        scriptsPath = self.baseMayaPath + 'scripts'
        if not self.pathExists(self.baseMayaPath):
            self.get_cmdialog_value("Installator alert!!", "No encuentro el directorio de maya 2018: " + self.baseMayaPath)
            return
        else:
            print ('Encontrado maya en: ' + self.baseMayaPath)
        self.pluginsPath = self.baseMayaPath + '/plug-ins'
        self.scriptsPath = self.baseMayaPath + '/scripts'
        if not self.pathExists(self.pluginsPath):
            self.createFolder(self.pluginsPath)
        if not self.pathExists(self.pluginsPath):
            self.createFolder(self.pluginsPath)


    def processList(self):
        self.get_cmdialog_value("Installator alert!!", "Estoy preparado para instalar " + self.baseMayaPath)


    def pathExists(self, path):
        """ Autoexplicativo
        devuelve true si el path existe
        """
        if os.path.exists(path):
            return True
        else:
            return False


    def createFolder(self, path):
        """ Autoexplicativo
        crea el folder previa comprobaciOn de su existencia
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print ('Error: Creating the directory ' +  path)
        else:
            print ('Successfully created the directory ' + path)


    def get_cmdialog_value(self, title, message):
        """
        Abre un cuadro de dialogo de para pedir un número entero
        message es el mensaje de la ventana.
        devuelve el numero entero:
        Si no ha tenido exito devuelve None
        mas info:
        ver https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
        ver http://interactivepython.org/runestone/static/CS152f17/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html
        """
        import Tkinter, tkSimpleDialog, tkMessageBox

    # Ask the user to select a single file name.
        root = Tkinter.Tk()
        root.iconbitmap('Z:/config/ffmpeg/editor/resources/ffmpeg.ico')
        root.withdraw() #otulta la ventana de tkinter
        value = tkSimpleDialog.askinteger( title, message, parent = root,
            initialvalue=0,
            minvalue=0,
            maxvalue=999)
        return value


install = Installator([{'a':123, 'b': 132},{'a':123, 'b': 132},{'a':123, 'b': 132}])


"""
plugs = glob.glob("c:/users/*/documents/maya/2018/plug-ins")
scripts =  glob.glob("c:/users/*/documents/maya/2018/scripts")
"""
