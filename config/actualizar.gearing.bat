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

REM Para el setup de las librerias y startup en vbs  solo para el estudio
Y:
cd Y:\config\lib\vbs\studio
git pull
cd Y:\config\lib\vbs\tools\vbsjson
git pull
cd Y:\config\setup\startup
git pull
