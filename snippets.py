# RECOPILATORIO DE SNIPPETS PYTHON PARA COSAS

#LISTAR ATRIBUTOS DE defaultArnoldDriver
#Este snippet lista los atributos de defaultArnoldDriver en la ventana de script

from maya.cmds import *
sn = cmds.attributeInfo( inherited=False, short=True, type="aiAOVDriver" )
for s in sn:
    print "defaultArnoldDriver.%s = %s" %( s, cmds.getAttr( "defaultArnoldDriver.%s" % s ) )


""" manipulacion de AOVS """

# mas info https://stackoverflow.com/questions/23173703/arnold-custom-aovs

import mtoa.aovs as aovs

# Create AOV
aovs.AOVInterface().addAOV('cputime', aovType='float')

# List all AOVs with their names
print(aovs.AOVInterface().getAOVNodes(names=True))

# añadir los AOVs principales
aovs.AOVInterface().addAOV('beauty')
aovs.AOVInterface().addAOV('Z')
aovs.AOVInterface().addAOV('N')
aovs.AOVInterface().addAOV('ID')
aovs.AOVInterface().addAOV('Occ')
aovs.AOVInterface().addAOV('Dpt')
aovs.AOVInterface().addAOV('Light')

# cosecha propia donde estan los atributos de los lightGroups en los AOVs

import pymel.core as pm
pm.select('aiAOV_*', r=True, ne=True) # sleccionar todos los AOVS

print pm.getAttr('aiAOV_specular.lightGroupsList',type=True) # tipo de dato para lightGroupsList
print pm.getAttr('aiAOV_specular.lightGroupsList') # contenido de la cadena

print pm.getAttr('aiAOV_diffuse.lightGroupsList',type=True)
print pm.getAttr('aiAOV_diffuse.lightGroupsList')


# donde se obtiene y como se asigna el lightGroup a las luces
print pm.getAttr('lst_set:lgt_key_farol02_03Shape.aiAov',type=True)  #Atributo del lightGroup es string
print pm.getAttr('lst_set:lgt_key_farol02_03Shape.aiAov')

pm.setAttr( 'lst_set:lgt_key_farol02_03Shape.aiAov', 'oquemedeagana' )


# OBTENER EL NOMBRE DEL FICHERO de la referencesInSceneArray

import maya.cmds as cmds

print cmds.file(query=True, sceneName=True, shortName=True)


# SRIPT EN PYMEL PARA OBTENER LAS VARIABLES DE ENTORNO DE MAYA
# info about http://www.jason-parks.com/artoftech/?p=164
# replace the ";" with ":" for OSX
# or better yet determine your system and
# automatically do it. I'll leave that up to you.
# (hint: try os.name)

import sys
from pymel.all import *

def getEnvironment():
    scriptPaths = mel.getenv("MAYA_SCRIPT_PATH")
    plugInPaths = mel.getenv("MAYA_PLUG_IN_PATH")
    pythonPaths = mel.getenv("PYTHONPATH")
    iconPaths = mel.getenv("XBMLANGPATH")
    pathPaths = mel.getenv("PATH")
    sysPaths = sys.path

    allScriptPaths = scriptPaths.split(";")
    print "\nMAYA_SCRIPT_PATHs are:"
    for scriptPath in allScriptPaths:
        print scriptPath

    allPlugInPaths = plugInPaths.split(";")
    print "\nMAYA_PLUG_IN_PATHs are:"
    for plugInPath in allPlugInPaths:
        print plugInPath

    allPythonPaths = pythonPaths.split(";")
    print "\nPYTHONPATHs are:"
    for pythonPath in allPythonPaths:
        print pythonPath

    allIconPaths = iconPaths.split(";")
    print "\nXBMLANGPATHs are:"
    for iconPath in allIconPaths:
        print iconPath

    allPathPaths = pathPaths.split(";")
    print "\nPATHs are:"
    for pathPath in allPathPaths:
        print pathPath

    print "\nsys.paths are:"
    for sysPath in sysPaths:
        print sysPath


# distintos querys (texturas y referencias)
# info about https://groups.google.com/forum/#!msg/python_inside_maya/KYgnHkc1xvk/ADZ4USknEAAJ

# So if you want the texture file nodes in the scene, you can get them from pymel with:
import pymel.core as pm
file_nodes = pm.ls(type=pm.nt.File)
file_paths = [fyle.fileTextureName.get() for fyle in file_nodes]

# with cmds:
import maya.cmds as cmds
file_nodes = cmds.ls(type='file')
file_paths = [cmds.getAttr(fyle + '.fileTextureName') for fyle in file_nodes]

# Unresolved reference paths can be gotten pretty easy in pymel :
unresolved_paths = [ref.unresolvedPath() for ref in pm.listReferences()]

# with cmds:
[cmds.referenceQuery(pth, unresolvedName=True, filename=True) for pth in  cmds.file(q=True, reference=True)]

# ejemplo en pymel de fileReference y su uso
#  info about https://forums.cgsociety.org/t/edit-reference-file-attributes/1702955

import pymel.core as pm
FR = pm.FileReference(namespace='myNamespace')
current_path = FR.path
FR.replaceWith(new_path)



"""

Info about como seleccionar nodos por tipos.

I think you need to do it in 2 commands. You can list objects of a certain type and then you can select the objects in that list. In the case of a locator the shapeNode type is “locator”, but you probably want to select the transform above that locator, which requires another command.

You could put them all together in mel like this





{string $locs[] = eval("listRelatives -p `ls -type locator \"loc*\"`"); select $locs;}



Its a bit neater in python

"""



import pymel.core as pm

pm.select(pm.listRelatives(pm.ls('loc*',type='locator'),parent=True))



# more about listrelatives http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/PyMel/generated/functions/pymel.core.general/pymel.core.general.listRelatives.html



"""

Here is the code i used to retrive the global XYZ. Feel free to reply if you need to understand something (i’ll comment it)

Note that “mc” is my mayaCmds variable.

"""



# Select the Joint i want to get the information from, with the Replace flag on

cmds.select( "jnt_Spn_HeadTop", r=True )



# Use XForm, with Query set to true, Translation set to true, and Worldspace set to true.

# This seems to tell it that, because its a query, you want Translation information, and ontop of that, you want it to be worldspace information.

myVal = cmds.xform( query=True, translation=True, worldSpace=True )



#Now simply use the 3 element array (tupple/dict/whatever, im an oldschool C++ Array guy). In this case i am moving the pivot of a rig control, with absolute coordinates.

cmds.move( myVal[0],myVal[1],myVal[2], "Ctrl_Head.scalePivot", "Ctrl_Head.rotatePivot", absolute=True )



"""

deberia funcionar igual con pymel

more about select http://download.autodesk.com/global/docs/maya2012/zh_cn/PyMel/generated/functions/pymel.core.general/pymel.core.general.select.html

more about xform buscar

"""


# script for automatically loading reference files from different destinations in Maya
#info about https://stackoverflow.com/questions/19677109/script-for-automatically-loading-reference-files-from-different-destinations-in

import maya.cmds as cmds
import os

def openFileAndRemapRefs():
    multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"

    # Choose file to open
    filename = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2, fileMode=1)

    # Open file with no reference loaded
    cmds.file( filename[0], open=True, force=True );

    # Dir containing the references
    refDir = 'C:/References'

    # A list of any references found in the scene
    references = cmds.ls(type='reference')

    # For each reference found in scene, load it with the path leading up to it replaced
    for ref in references:
        refFilepath = cmds.referenceQuery(ref, f=True)
        refFilename = os.path.basename( refFilepath )
        print 'Reference ' + ref + ' found at: ' + cmds.referenceQuery(ref, f=True)
        cmds.file( os.path.join(refDir, refFilename), loadReference=ref, options='v=0;')

openFileAndRemapRefs()

# PARA REEMPLAZAR CONTENIDOS DENTRO DE UNA FICHERO MEL  POR EJEMPLO
# info about https://stackoverflow.com/questions/49859115/maya-ascii-filepath-replace

import os

# Adjust these paths to existing maya scene files.
scnPath = "/path/to/file/to/open.ma"
oldPath = "/path/to/old/file.ma"
newPath = "/path/to/new/file.ma"
aborrar_en_ficheros='fileInfo "license" "student"'
with open(scnPath, "r") as fp:
    # Get all file contents in a list.
    fileLines = fp.readlines()

    # Use enumerate to keep track of what index we're at.
    for i, line in enumerate(previsReadlines):
        # Check if the line has the old path in it.
        if oldPath in line:
            # Replace with the new path and assign the change.
            # Before you were assigning this to a new variable that goes nowhere.
            # Instead it needs to re-assign the line from the list we first read from.
            fileLines[i] = line.replace(oldPath, newPath)

# Completely replace the file with our changes.
with open(scnPath, 'w') as fw:
    # You must pass the contents in here to write it.
    fw.writelines(fileLines)



## STRING STRING STRING functions
# rawString para anular las secuencias de escape en los nombre
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

## Funciones para escribir leer y tratar ficheros JSON
# la primera es pasar el path a un fichero JSON
# more about in https://stackoverflow.com/questions/25226208/represent-directory-tree-as-json
""" Represent directory tree as JSON
como en este ejemplo:

{
  "type": "directory",
  "name": "hello",
  "children": [
    {
      "type": "directory",
      "name": "world",
      "children": [
        {
          "type": "file",
          "name": "one.txt"
        },
        {
          "type": "file",
          "name": "two.txt"
        }
      ]
    },
    {
      "type": "file",
      "name": "README"
    }
  ]
}

"""
import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print json.dumps(path_to_dict('.'))

decoded = json.loads(data_string)


""" Volcar una varible json a fichero

Writing JSON to a File
"""
#more about in https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


""" Ejemplo con JSON identado
"""
import json

d = {'one': 1, 'group': [4,9,7]}
print json.dumps(d, indent=4, sort_keys=True)

"""
will output:

   {
        "one": 1,
            "group": [
            4,
            9,
            7
        ]
    }
"""


"""
         _      _               _                 
        (_)    | |             | |                
  __   ___ _ __| |_ _   _  __ _| | ___ _ ____   __
  \ \ / / | '__| __| | | |/ _` | |/ _ \ '_ \ \ / /
   \ V /| | |  | |_| |_| | (_| | |  __/ | | \ V / 
    \_/ |_|_|   \__|\__,_|\__,_|_|\___|_| |_|\_/  
                                                  
                                                  
TIPOGRAFIAS GRANDES COMO ESTAS Y OTRAS PARA COMENTARIOS: Doom

 _____ _                      _         _   _                              __ _          ___   _____ _____ _____ _____ 
|  ___(_)                    | |       | | (_)                            / _(_)        / _ \ /  ___/  __ \_   _|_   _|
| |__  _  ___ _ __ ___  _ __ | | ___   | |_ _ _ __   ___   __ _ _ __ __ _| |_ _  __ _  / /_\ \\ `--.| /  \/ | |   | |  
|  __|| |/ _ \ '_ ` _ \| '_ \| |/ _ \  | __| | '_ \ / _ \ / _` | '__/ _` |  _| |/ _` | |  _  | `--. \ |     | |   | |  
| |___| |  __/ | | | | | |_) | | (_) | | |_| | |_) | (_) | (_| | | | (_| | | | | (_| | | | | |/\__/ / \__/\_| |_ _| |_ 
\____/| |\___|_| |_| |_| .__/|_|\___/   \__|_| .__/ \___/ \__, |_|  \__,_|_| |_|\__,_| \_| |_/\____/ \____/\___/ \___/ 
     _/ |              | |                   | |           __/ |                                                       
    |__/               |_|                   |_|          |___/                                                        
	
more about	http://patorjk.com/software/taag/#p=display&f=Doom&t=Ejemplo%20tipografia%20ASCII

OTRO EJEMPLO: Big (tiene acentos)
  ______ _                      _         _   _                              __ __                  _____  _____ _____ _____ 
 |  ____(_)                    | |       | | (_)                            / _/_/           /\    / ____|/ ____|_   _|_   _|
 | |__   _  ___ _ __ ___  _ __ | | ___   | |_ _ _ __   ___   __ _ _ __ __ _| |_ _  __ _     /  \  | (___ | |      | |   | |  
 |  __| | |/ _ \ '_ ` _ \| '_ \| |/ _ \  | __| | '_ \ / _ \ / _` | '__/ _` |  _| |/ _` |   / /\ \  \___ \| |      | |   | |  
 | |____| |  __/ | | | | | |_) | | (_) | | |_| | |_) | (_) | (_| | | | (_| | | | | (_| |  / ____ \ ____) | |____ _| |_ _| |_ 
 |______| |\___|_| |_| |_| .__/|_|\___/   \__|_| .__/ \___/ \__, |_|  \__,_|_| |_|\__,_| /_/    \_\_____/ \_____|_____|_____|
       _/ |              | |                   | |           __/ |                                                           
      |__/               |_|                   |_|          |___/                                                            

Y OTRO: Small (tiene acentos)

  ___  _                _       _   _                           __ __         _   ___  ___ ___ ___ 
 | __|(_)___ _ __  _ __| |___  | |_(_)_ __  ___  __ _ _ _ __ _ / _/_/__ _    /_\ / __|/ __|_ _|_ _|
 | _| | / -_) '  \| '_ \ / _ \ |  _| | '_ \/ _ \/ _` | '_/ _` |  _| / _` |  / _ \\__ \ (__ | | | | 
 |___|/ \___|_|_|_| .__/_\___/  \__|_| .__/\___/\__, |_| \__,_|_| |_\__,_| /_/ \_\___/\___|___|___|
    |__/          |_|                |_|        |___/                                              


"""
