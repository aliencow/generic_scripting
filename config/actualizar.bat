@echo off

REM Poner en el arranque de WINDOWS para tener actualizados todos los gits
REM Queda guardado C:\Users\JUAN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\actualizar.bat
REM lo ejecuta al arranque de windows para buscar la carpeta de inicio de windows en el ejecutor de comandos
REM Alt+R teclar shell:startup (usuario local) o shell:common startup (todos los usuarios)

F:
cd F:\proyectos_python\flask_pymongo
git pull
cd F:\proyectos_python\generic_scripting
git pull
cd F:\proyectos_python\tablapythonweb
git pull
cd F:\proyectos_python\tablesdir
git pull
cd F:\proyectos_python\the_gearing\aom_playblast
git pull
cd F:\proyectos_python\the_gearing\concatenator
git pull
