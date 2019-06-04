# -*- coding: utf-8 -*-
import sys
import os
import time
import json
import shutil

"""
info para hacer el batch
https://stackoverflow.com/questions/4571244/creating-a-bat-file-for-python-script
"""
"""
Bloque de funciones de entrada
"""

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n')./n")



## STRING STRING STRING functions
# rawString para anular las secuencias de escape en los nombres
# more about in http://code.activestate.com/recipes/65211-convert-a-string-into-a-raw-string/

escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def rawString(text):
    """Returns a raw string representation of text"""
    escape_dict={'\a':r'\a',
               '\b':r'\b',
               '\c':r'\c',
               '\f':r'\f',
               '\n':r'\n',
               '\r':r'\r',
               '\t':r'\t',
               '\v':r'\v',
               '\'':r'\'',
               '\"':r'\"',
               '\0':r'\0',
               '\1':r'\1',
               '\2':r'\2',
               '\3':r'\3',
               '\4':r'\4',
               '\5':r'\5',
               '\6':r'\6',
               '\7':r'\7',
               '\8':r'\8',
               '\9':r'\9'}

    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string



# define our clear function
def clear_output():
    """
    """
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = ps.system('clear')

"""
funciones de conversion de frames a codigo de tiempo en formato ffmpeg
info https://stackoverflow.com/questions/34606045/convert-timecode-to-frames-with-set-start-timecode
"""

def ffmpeg_seconds(value, framerate):
    return float(value) / float(framerate)

def ffmpeg_timecode(seconds):
    s = abs(seconds)-abs(int(seconds))
    return '{h:02d}:{m:02d}:{s:02d}.{f:03d}' \
            .format(h=int(seconds/3600),
                    m=int(seconds/60%60),
                    s=int(seconds%60),
                    f=int(s*1000))

def ffmpeg_timecode_b(seconds):
    s = abs(seconds)-abs(int(seconds)) # de parte proporcional
    s = int(s*10000) # a 10milisegundos
    div = int(s/417) #cogemos el resultado
    mod = s%417      #cogemos el módulo
    if mod > 417/2: # si el módulo es mayor que el valor entre 2 redondeo up
        div = div + 1
    s = int(div * 417)
    s = int(s/10)
    return '{h:02d}:{m:02d}:{s:02d}.{f:03d}' \
            .format(h=int(seconds/3600),
                    m=int(seconds/60%60),
                    s=int(seconds%60),
                    f=int(s))


def ffmpeg_frames(seconds, framerate):
    return seconds * framerate

#def timecode_to_frames(timecode, start=None):
    #return _frames(_seconds(timecode) - _seconds(start))

def ffmpeg_frames_to_timecode(frames, framerate):
    return ffmpeg_timecode_b(ffmpeg_seconds(frames, framerate))


"""
    Función para guardar un fichero de texto desde una lista de strings
"""

def save_file_from_list(path, filename, list):
    """
    Escribe un fichero de texto a partir de  una lista de líneas
    """
    outpathname = os.path.join( path, filename)
    with open(outpathname, 'wb') as file:
        for row in list:
            file.write(row)
            file.write('\r\n')
        print 'writing completed!'
        file.close()

def check_if_file_exits(filename):
    """
    Comprueba si existe un fichero o directorio..
    """
    return os.path.exists(filename)

def copy_tree_structure(src, dest):
    """
    copia el subdiretorio indicado en src con todo su contenido a un nuevo
    subdirectorio dest
    https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python
    """
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


"""
    Bloque de funciones auxiliares para manejo de version
"""

def increaseversion(version, incletra=False, incnumber=True):
    """
    Incrementa en numero y/o letra la versión de edición.
    incletra=True se incrementa la letra de la versión por ejemplo 'a' pasa a 'b'
    incnumber = True se incrementa el número de la versión por ejemplo '001' pasa a '002'
    devuelve la nueva version concatenando letra y numero
    """
    letra = version[:1]
    numero = int(version[-3:])

    if incletra:
        ch = letra
        letra = chr(ord(ch) + 1) # siguiente caracter ojo con las versiones de letra muy altas
    if incnumber:
        numero += 1

    return letra+'{:03d}'.format(numero)

"""
Bloque de funciones relacionadas con escribir leer JSON
"""

def readJSONfile(filename):
    """
    Devuelve una variable dictionary (content)
    cargada con el contenido del JSON referenciado en filename
    """
    content = {}
    with open(filename) as json_file:
        content = json.load(json_file)
        json_file.close()
    return content


def writeJSONfile(filename, content):
    with open(filename, 'w') as json_file:
        json.dump(content , json_file, indent=4)
        json_file.close()

"""
    Bloque de funciones con Tkinter
"""

def get_path_and_filename(titulo, initialdir):
    """
    Abre un cuadro de dialogo de selección de ficheros
    initialdir es el directorio de partida.
    devuelve una lista de dos elementos:
        lista[0] nombre del directorio.
        lista[1] nombre del fichero seleccionado.
    Si no ha tenido exito devuelve una lista con dos nulos
    mas info:
    ver https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
    ver http://interactivepython.org/runestone/static/CS152f17/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html
    """
    import Tkinter, tkFileDialog

# Ask the user to select a single file name.
    root = Tkinter.Tk()
    root.iconbitmap('Z:/config/ffmpeg/editor/resources/ffmpeg.ico')
    root.withdraw() #otulta la ventana de tkinter

    #file_path = tkFileDialog.askopenfilename()
    file_path = tkFileDialog.askopenfilename( parent=root, initialdir=initialdir, title=titulo)
    #directorio = tkFileDialog.askdirectory()

    if file_path:
        splitdir = file_path.split("/")
        filename = splitdir[-1]
        solopath= splitdir[:(len(splitdir) - 1)]
        dirname =""
        for path in solopath:
            if dirname:
                dirname +=  '/' + path
            else:
                dirname = path
        return [dirname, filename]
    else:
        return ['','']

def set_path_and_filename(titulo, initialdir):
    """
    Abre un cuadro de dialogo de selección de ficheros
    para hacer un save y poder teclear el fichero.
    devuelve una lista de dos elementos:
        lista[0] nombre del directorio.
        lista[1] nombre del fichero seleccionado.
    Si no ha tenido exito devuelve una lista con dos nulos
    mas info:
    ver https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
    ver http://interactivepython.org/runestone/static/CS152f17/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html
    """
    import Tkinter, tkFileDialog

# Ask the user to select a single file name.
    root = Tkinter.Tk()
    root.iconbitmap('Z:/config/ffmpeg/editor/resources/ffmpeg.ico')
    root.withdraw() #otulta la ventana de tkinter

    #file_path = tkFileDialog.askopenfilename()
    file_path = tkFileDialog.asksaveasfilename( parent=root, initialdir=initialdir, title=titulo, filetypes = (("mov files","*.mov"),("all files","*.*")))
    #directorio = tkFileDialog.askdirectory()

    if file_path:
        splitdir = file_path.split("/")
        filename = splitdir[-1]
        solopath= splitdir[:(len(splitdir) - 1)]
        dirname =""
        for path in solopath:
            if dirname:
                dirname +=  '/' + path
            else:
                dirname = path
        return [dirname, filename]
    else:
        return ['','']

def get_cmdialog_value(title, message):
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

def confirmdialog(title, message):
    """
    Abre un cuadro de dialogo de para pedir confirmar con si o no..
    message es el mensaje de la ventana, title es el título del dialogo
    devuelve un boolean:
     True si se ha pulsado yes:
    mas info:
    ver https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
    ver http://interactivepython.org/runestone/static/CS152f17/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html
    """
    import Tkinter, tkMessageBox

# Ask the user to select a single file name.
    root = Tkinter.Tk()
    root.iconbitmap('Z:/config/ffmpeg/editor/resources/ffmpeg.ico')
    root.withdraw() #otulta la ventana de tkinter
    root.geometry('500x500')

    value = tkMessageBox.askyesno(title, message, parent = root)

    return value
