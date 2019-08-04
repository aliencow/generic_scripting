@echo off
REM Poner en el arranque de WINDOWS para tener actualizados todos los gits
REM Queda guardado en /Users/juan.nouche/desktop/actualizar.sh
REM Para ejecutar source /Users/juan.nouche/desktop/actualizar.sh
REM El comando esta puesto en ./bash_profile en el $HOME

F:
cd F:\ALMACEN1TB\proyectos_python\flask_pymongo
git pull
cd F:\ALMACEN1TB\proyectos_python\generic_scripting
git pull
cd F:\ALMACEN1TB\proyectos_python\tablapythonweb
git pull
cd F:\ALMACEN1TB\proyectos_python\tablesdir
git pull
cd F:\ALMACEN1TB\proyectos_python\the_gearing\aom_playblast
git pull
cd F:\ALMACEN1TB\proyectos_python\the_gearing\concatenator
git pull
