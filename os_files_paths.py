

""" Excelente tutorial de python https://www.programiz.com/python-programming/keywords-identifier
La parte de ficheros aquí https://www.programiz.com/python-programming/file-operation
Los directorios aquí https://www.programiz.com/python-programming/directory
"""
""" Tutorial de pyjamas un interface visual
https://www.ibm.com/developerworks/library/wa-aj-pyjamas/index.html
"""


""" get current directory """

# import the os module
import os
# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

""" dc change directory """

import os
path = "Un path cualquiera en cualquier unidad"
os.chdir(path)


""" dir o ls en python """
import os
os.listdir()


""" Eliminar un fichero concreto """

import os
os.remove("demofile.txt")

# Comprobando si existe
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


""" copy file con shutil """

from shutil import copyfile
src = "Un path en string con su extensión"  # Un nombre de fichero con toda la ruta
dst = "Otro path en string con su extensión"
copyfile(src, dst)

""" codigos posibles de error al trabajar con makedir """
## lista de errores de fichero para testear https://docs.python.org/2/library/errno.html#module-errno

""" CREAR CARPETAS CREAR CARPETAS """
""" CREAR CARPETAS CREAR CARPETAS """


""" Creating a Directory"""
import os

# define the name of the directory to be created
path = "/tmp/year"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


""" Creating a Directory with Subdirectories """
import os

# define the name of the directory to be created
path = "/tmp/year/month/week/day"

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)


""" Función para crear directorios ejemplo """
import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


# Example
createFolder('./data/')
# Creates a folder in the current directory called data

""" BORRAR CARPETAS BORRAR CARPETAS """
""" BORRAR CARPETAS BORRAR CARPETAS """

""" Borrar un directorio """
import os

# define the name of the directory to be deleted
path = "/tmp/year"

try:
    os.rmdir(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)

""" Borrar a not empty folder """
import shutil
shutil.rmtree(path)

""" COPIAR CARPETAS COPIAR CARPETAS """
""" COPIAR CARPETAS COPIAR CARPETAS """


""" Copiar un directorio con todos sus contenidos """
import os
import shutil

src = "Directorio a copiar"
dst = "Directorio donde se va a copiar"
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

""" Comprobar si existe directorio o path """

#this is arguably the easiest way to check if both a file exists and if it is a file.

import os
os.path.isfile('./file.txt')    # True
os.path.isfile('./dir')    # False

os.path.isdir('./file.txt')    # False
os.path.isdir('./dir')    # True


"""
Funciones para localizar el user path..

"""
#You want to use os.path.expanduser. This will ensure it works on all platforms

from os.path import expanduser
home = expanduser("~")

#If you're on Python 3.5+ you can use pathlib.Path.home():

from pathlib import Path
home = str(Path.home())

"""
Funciones propias AUXILIARES
"""


def pathExists(path):
    """ Autoexplicativo
    devuelve true si el path existe
    """
    if os.path.exists(path):
        return True
    else:
        return False


def createFolder(path):
    """ Autoexplicativo
    crea el folder previa comprobación de su existencia
    """
    try:
        if not os.path.exists(path):
            print ('hola hola')
            os.makedirs(path)
    except OSError:
        print ('Error: Creating the directory ' +  path)
    else:
        print ('Successfully created the directory ' + path)
