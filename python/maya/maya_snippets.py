## ayuda programadores MAYA
# https://www.maya-dev.com/index.php/category/maya-api/maya-api-c/maya-api-c-comandos/

"""
___  ___                                           _      ______                     _
|  \/  |                                          | |     | ___ \                   | |
| .  . | __ _ _   _  __ _        ___ _ __ ___   __| |     | |_/ /   _ _ __ ___   ___| |
| |\/| |/ _` | | | |/ _` |      / __| '_ ` _ \ / _` |     |  __/ | | | '_ ` _ \ / _ \ |
| |  | | (_| | |_| | (_| |  _  | (__| | | | | | (_| |  _  | |  | |_| | | | | | |  __/ |
\_|  |_/\__,_|\__, |\__,_| (_)  \___|_| |_| |_|\__,_| (_) \_|   \__, |_| |_| |_|\___|_|
               __/ |                                             __/ |
              |___/                                             |___/
los fonts estan aquí:	http://patorjk.com/software/taag/#p=display&f=Doom&t=Ejemplo%20tipografia%20ASCII


"""

#pymel info: https://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/PyMel/generated/functions/pymel.core.system/pymel.core.system.loadPlugin.html

# RECOPILATORIO DE SNIPPETS PYTHON PARA COSAS
# Creación de shelves dese python
#https://bindpose.com/scripting-custom-shelf-in-maya-python/

""" Deleting unused nodes (por ejemplo mental ray u otro plugin que venga en el fichero)
"""
# con cmds
import maya.cmds as cmds
unknownNodes=cmds.ls(type = "unknown")
unknownNodes+=cmds.ls(type = "unknownDag")
for item in unknownNodes:
    if cmds.objExists(item):
        print item
        cmds.lockNode(item, lock=False)
        cmds.delete(item)

# con pymel
import pymel.core as pm
unknownNodes=pm.ls(type = "unknown")
unknownNodes+=pm.ls(type = "unknownDag")
for item in unknownNodes:
    if pm.objExists(item):
        print item
        pm.lockNode(item, lock=False)
        pm.delete(item)

""" Load and Unload Plugins
"""
plugin = 'lookdevKit'
QALoadPlugin (plugin, True)
QAUnloadPlugin (plugin)
def QALoadPlugin(plugin, auto=True):
    if pm.pluginInfo(plugin, q=True, r = True):
        if not pm.pluginInfo(plugin, q=True, loaded=True): # si no está cargado
            pm.loadPlugin( plugin) # cargarlo
        if auto: # si se llama con autoload ponerlo
            pm.pluginInfo( plugin, q=True, autoload=True ) # pone el autoload
    else: # no esta registrado
        print 'ANTARUXA WARNING!!! No existe el plugin: ' + plugin

def QAUnloadPlugin(plugin):
    if pm.pluginInfo(plugin, q=True, r = True):
        if pm.pluginInfo(plugin, q=True, loaded=True): # si está cargado
            pm.pluginInfo( plugin, edit=True, autoload=False ) # quitarle el autoload primero
            pm.unloadPlugin( plugin )
    else: # no esta registrado
        print 'ANTARUXA WARNING!!! No existe el plugin: ' + plugin

""" Listar plugins instalados
"""
pm.pluginInfo( query=True, listPlugins=True )


"""
 _____ _               _                            _            _                           _         ___  ___  _____   _____
/  ___| |             | |                  ___     | |          | |                         (_)        |  \/  | / _ \ \ / / _ \
\ `--.| |__   __ _  __| | ___ _ __ ___    ( _ )    | |_ _____  _| |_ _   _ _ __ ___  ___     _ _ __    | .  . |/ /_\ \ V / /_\ \
 `--. \ '_ \ / _` |/ _` |/ _ \ '__/ __|   / _ \/\  | __/ _ \ \/ / __| | | | '__/ _ \/ __|   | | '_ \   | |\/| ||  _  |\ /|  _  |
/\__/ / | | | (_| | (_| |  __/ |  \__ \  | (_>  <  | ||  __/>  <| |_| |_| | | |  __/\__ \   | | | | |  | |  | || | | || || | | |
\____/|_| |_|\__,_|\__,_|\___|_|  |___/   \___/\/   \__\___/_/\_\\__|\__,_|_|  \___||___/   |_|_| |_|  \_|  |_/\_| |_/\_/\_| |_/

"""


""" Crear u asignar un shader a un objeto en mayaA
"""

import maya.cmds as mc

def applyMaterial(node, material):
    if mc.objExists(node):
        shd = mc.shadingNode('lambert', name="%s_lambert" % node, asShader=True)
        shdSG = mc.sets(name='%sSG' % shd, empty=True, renderable=True, noSurfaceShader=True)
        mc.connectAttr('%s.outColor' % shd, '%s.surfaceShader' % shdSG)
        mc.sets(node, e=True, forceElement=shdSG)

applyMaterial("pSphere1")


    def remove_simple_lambert_material(self):
        """ remove_simple_lambert_material antagónica de create_simple_lambert_material
        elimina el meterial creado previamente guardado en self.shd y self.shdSG
        Returns
        -------
        shdSG contiene el nombre del shadinggroup para asignar

        Parameters
        ----------
        none
        """
        shd = self.shd
        shdSG = self.shdSG
        pm.select(shdSG, ne=True)
        pm.select(shd, add=True)
        pm.delete()
        self.shd = self.shdSG = None

    def get_asigned_material(self, object):
        """ get_asigned_material es auxiliar de guardar_material_antiguo_y_asignar_nuevo
        devuelve esl material y shading group que tiene un objeto asignado
        Returns
        -------
        shd, shdSG contienen el material y shading groups asignados

        Parameters
        ----------
        object objeto del que se extrae el material
        """
        shd=None
        shdSG = pm.listConnections(object, type='shadingEngine')
        if shdSG:
            shd = pm.listConnections(shdSG[0] + '.surfaceShader')
            #print 'OBJECT: ' + object + ' | ' + 'MAYA SHADER: ' + shd[0] + ' | ' + 'MAYA SG: ' + shdSG[0]
        return shd, shdSG


    def asign_material_to_node(self, node, materialSG):
        """ asign_material_to_node es auxiliar de guardar_material_antiguo_y_asignar_nuevo
        asigna el shading group al nodo que se quiera
        Returns
        -------
        none

        Parameters
        ----------
        node, materialSG nodo al que se asigna y shading group que se asigna
        """
        pm.sets(materialSG, e=True, forceElement=node)


    def create_simple_lambert_material(self):
        """ create_simple_lambert_material
        crea y configura un material simple (lambert) para utilizar con
        el ambient occlussion utiliza el nombre de material self.material_name
        y almacena el material en self.shd y el shadign group en self.shdSG
        Returns
        -------
        none

        Parameters
        ----------
        none
        """
        self.shd = pm.shadingNode('lambert', name="%s_lambert" % self.material_name, asShader=True)
        self.shdSG = pm.sets(name='%sSG' % self.shd , empty=True, renderable=True, noSurfaceShader=True)
        pm.connectAttr('%s.outColor' % self.shd, '%s.surfaceShader' % self.shdSG)



"""
 _____                      _   _     _                      _                 _       ___                   _     _             ___  ___  _____   _____
/  ___|                    | | | |   (_)                    | |               | |     / _ \                 | |   | |            |  \/  | / _ \ \ / / _ \
\ `--.  ___  _ __ ___   ___| |_| |__  _ _ __   __ _     __ _| |__   ___  _   _| |_   / /_\ \_ __ _ __   ___ | | __| |   ______   | .  . |/ /_\ \ V / /_\ \
 `--. \/ _ \| '_ ` _ \ / _ \ __| '_ \| | '_ \ / _` |   / _` | '_ \ / _ \| | | | __|  |  _  | '__| '_ \ / _ \| |/ _` |  |______|  | |\/| ||  _  |\ /|  _  |
/\__/ / (_) | | | | | |  __/ |_| | | | | | | | (_| |  | (_| | |_) | (_) | |_| | |_   | | | | |  | | | | (_) | | (_| |            | |  | || | | || || | | |
\____/ \___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, |   \__,_|_.__/ \___/ \__,_|\__|  \_| |_/_|  |_| |_|\___/|_|\__,_|            \_|  |_/\_| |_/\_/\_| |_/
                                               __/ |
                                              |___/
"""

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



"""
______      __                                       _____                              _____                 _                         ___  ___  _____   _____
| ___ \    / _|                                     |  ___|                   ___      |  _  |               (_)                        |  \/  | / _ \ \ / / _ \
| |_/ /___| |_ ___ _ __ ___ _ __   ___ ___  ___     | |__ _ ____   _____     ( _ )     | | | |_   _  ___ _ __ _  ___  ___     ______    | .  . |/ /_\ \ V / /_\ \
|    // _ \  _/ _ \ '__/ _ \ '_ \ / __/ _ \/ __|    |  __| '_ \ \ / / __|    / _ \/\   | | | | | | |/ _ \ '__| |/ _ \/ __|   |______|   | |\/| ||  _  |\ /|  _  |
| |\ \  __/ ||  __/ | |  __/ | | | (_|  __/\__ \    | |__| | | \ V /\__ \   | (_>  <   \ \/' / |_| |  __/ |  | |  __/\__ \              | |  | || | | || || | | |
\_| \_\___|_| \___|_|  \___|_| |_|\___\___||___/    \____/_| |_|\_/ |___/    \___/\/    \_/\_\\__,_|\___|_|  |_|\___||___/              \_|  |_/\_| |_/\_/\_| |_/

                                                                                                                                                                                                               |___/
"""

# Poner el undo infinite
import pymel.core as pm

# Turn undo on, with an infinite queue length
pm.undoInfo( state=True, infinity=True )


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



# Query para leer todas las referencias de la escena y guardarlas en una lista de listas

refs_in = leer_referencias_escena()
for ref_in in refs_in:
    NameSpaceRef = ref_in[0]
    FileRef = ref_in[1]
    print NameSpaceRef, FileRef

def leer_referencias_escena():
    """
    Localiza las referencias que existen en la escena y las devuelve en un array de arrays
    en el elemento 0 del array devuelve el namespace y en el 1 un objeto de tipo FileReference
    """
    return pm.listReferences(namespaces = True)

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
# https://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/PyMel/generated/classes/pymel.core.system/pymel.core.system.FileReference.html
import pymel.core as pm
FR = pm.FileReference(namespace='myNamespace')
current_path = FR.path
FR.replaceWith(new_path)


# bloquear desbloquear nodes en maya
import pymel.core as pm
pm.lockNode(l=True) #True bloquea, False desbloquea


"""
 _____      _           _                 _   _                _           _                 ___  ___  _____   _____
/  ___|    | |         | |               | | | |              | |         | |                |  \/  | / _ \ \ / / _ \
\ `--.  ___| | ___  ___| |_    ______    | | | |_ __  ___  ___| | ___  ___| |_     ______    | .  . |/ /_\ \ V / /_\ \
 `--. \/ _ \ |/ _ \/ __| __|  |______|   | | | | '_ \/ __|/ _ \ |/ _ \/ __| __|   |______|   | |\/| ||  _  |\ /|  _  |
/\__/ /  __/ |  __/ (__| |_              | |_| | | | \__ \  __/ |  __/ (__| |_               | |  | || | | || || | | |
\____/ \___|_|\___|\___|\__|              \___/|_| |_|___/\___|_|\___|\___|\__|              \_|  |_/\_| |_/\_/\_| |_/

"""


"""

Info about como seleccionar nodos por tipos.

I think you need to do it in 2 commands. You can list objects of a certain type and then you can select the objects in that list. In the case of a locator the shapeNode type is “locator”, but you probably want to select the transform above that locator, which requires another command.

You could put them all together in mel like this

{string $locs[] = eval("listRelatives -p `ls -type locator \"loc*\"`"); select $locs;}



Its a bit neater in python

"""



import pymel.core as pm

#desactivar la seleccióón activa
pm.select( clear=True ) #desactivar selección


#seleccion por tipos (locator en el ejemplo)
pm.select(pm.listRelatives(pm.ls('loc*',type='locator'),parent=True))



# seleccion de todos los descendientes de un grupo de objetos
import pymel.core as pm
pm.select("Environment_GRP")
nodes = pm.ls(sl=True)

nodes += pm.listRelatives(nodes, allDescendents=True) #seleccionar toda la jerarquia
pm.select(nodes)


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


"""
 _____                      _   _     _                      _                 _     ______ _____ _      _____ _____    _                  ___  ___  _____   _____
/  ___|                    | | | |   (_)                    | |               | |    |  ___|_   _| |    |  ___/  ___|  (_)                 |  \/  | / _ \ \ / / _ \
\ `--.  ___  _ __ ___   ___| |_| |__  _ _ __   __ _     __ _| |__   ___  _   _| |_   | |_    | | | |    | |__ \ `--.    _ _ __    ______   | .  . |/ /_\ \ V / /_\ \
 `--. \/ _ \| '_ ` _ \ / _ \ __| '_ \| | '_ \ / _` |   / _` | '_ \ / _ \| | | | __|  |  _|   | | | |    |  __| `--. \  | | '_ \  |______|  | |\/| ||  _  |\ /|  _  |
/\__/ / (_) | | | | | |  __/ |_| | | | | | | | (_| |  | (_| | |_) | (_) | |_| | |_   | |    _| |_| |____| |___/\__/ /  | | | | |           | |  | || | | || || | | |
\____/ \___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, |   \__,_|_.__/ \___/ \__,_|\__|  \_|    \___/\_____/\____/\____/   |_|_| |_|           \_|  |_/\_| |_/\_/\_| |_/
                                               __/ |
                                              |___/
"""


def seleccionarNombre():
    """ Funcion seleccionarNombre obtiene el nombre de la escena (sin path)
    menos la extensiOn .ma
    Returns
    -------
    sceneName nombre del archivo excepto extension .ma
    Parameters
    ----------
    mone
    """
    ruta =  pm.sceneName()
    ruta = 	ruta[:-3] #quitar el .ma
    pathSplitter = ruta.split('/')
    sceneName = pathSplitter[-1]
    return sceneName



def seleccionarRuta():
    """ Funcion seleccionarRuta obtiene el path completo de la escena
    activa menos la extensiOn .ma
    Returns
    -------
    ruta ruta completa de la escena activa excepto la extensiOn .ma
    Parameters
    ----------
    """
    ruta =  pm.sceneName()
    ruta = 	ruta[:-3] #quitar el .ma
    return ruta


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
