@echo off

REM Poner en el arranque de WINDOWS para tener actualizados todos los gits
REM Queda guardado C:\Users\JUAN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\actualizar.bat
REM lo ejecuta al arranque de windows para buscar la carpeta de inicio de windows en el ejecutor de comandos
REM Alt+R teclar shell:startup (usuario local) o shell:common startup (todos los usuarios)

REM updatear los proyectos que pueden actualizarse desde fuera

C:
cd C:\Users\juan.nouche\Documents\juan\git_projects\flask_pymongo
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\generic_scripting
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\tablapythonweb
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\tablasdir
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\aom_playblast
git pull

REM antaruxa startup

cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\startup_local
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\vbsstudiolib
git pull

REM updatear en local los proyectos antaruxa pipeline

C:
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\pipeline\pipeline
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\pipeline\nomen
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\pipeline\treelib
git pull

REM updatear en local los proyectos antaruxa ved_tools

c:
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\ved\ved_tools
rem git stash
git pull
rem git stash pop

rem cambiar nombre cuando deje windows a out_of_maya
c:
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\new_concatenator
git pull

REM custom maya plug-ins
c:
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\QA_antaruxa
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\plug-ins_maya\skin_bones
git gull

REM custom studio tools
c:
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\shotgun
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\maya_tools
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\logger
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\deadline
git pull
cd C:\Users\juan.nouche\Documents\juan\git_projects\the_gearing\sysutils
git pull
