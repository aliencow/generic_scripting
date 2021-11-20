## Info sobre comandos linux

1. Listar comandos disponibles. You can use compgen:

  compgen -c # will list all the commands you could run.


  FYI:

  compgen -a # will list all the aliases you could run.
  compgen -b # will list all the built-ins you could run.
  compgen -k # will list all the keywords you could run.
  compgen -A function # will list all the functions you could run.
  compgen -A function -abck # will list all the above in one go.

comandos synology
https://forum.synology.com/enu/viewtopic.php?t=126516#p464447

2. version instalada de linux
uname -r
uname -a
cat /proc/version

<<<<<<< Updated upstream
\* any text
-r recursive
-v verbose
pueden usarse acumuladas. ej -rv (recursive and verbose)


man command devuelve la ayuda para el comando concreto
find -name 'k*.txt' Busqueda de ficheros.
find /home -name 't*.py' Busqueda a partir de un directorio concreto (home)

mv mover o renombrar icheros
cd cambiar de directorio
ls listar (DIR)
ls -l lista en formato largo.
cp copiar
rm eliminar
du disk usage (indica el especio en k en el disco)
clear o ctrl+L limpia de comandos la pantalla.

mkdir name crea un directorio
rmdir name elimina el directorio (solo si esta vacio)
rm -rf dir-name elimina el direcotrio y todo su contednido
=======

solo ubuntu o debian
====================
sudo apt update
updates the list of available packages and their versions.
sudo apt upgrade
installs newer versions of the packages you already have installed
>>>>>>> Stashed changes

prompt terminado en $ usuario # root
patron de comando linux:
prompt$ comando opciones argumentos   ej. ls -l /etc/



cat       muestra el contenido de fichero en el la pantalla. Puede mostrar el contenido de varios ficheros
              opción -n muestra el número de línea
              opción -b igual que -n pero no numera líneas vacias o en blanco.

cd          cambiar de directorio \ raiz ..\ baja un nivel ..\..\ baja dos . directorio actual
              opción /ruta/o/path Se cambia  de directorio a la ruta indicada que puede ser absoluta o relativa.
              sin opciones. Sin argumentos se cambiará al directorio HOME del usuario actual.


clear       o ctrl+L limpia de comandos la pantalla.

cut       corta o separa por columnas el contenido de un fichero
              opción -d indica el delimitador entre columnas. ej. si es ';' la opción -d;
              opción -f selecciona el número de columnas a visualizar ej. -f3 tercera columna -f3,4 tercera y cuarta, -f2-5 de la dos a la cinco, etc.
              opción -c especifica los caracteres a cortar ej. -c 2 coge dos caracteres -c 9-10 coge los caracteres del 9 al 20.

echo        Muestra en la salida extandar el texto o file que se indique. Se puede usar este comando para crear un fichero redireccionando la salida. ej. `echo "hello" > myfile.txt`.


history     muestra historial de comandos (se almacena en .bash_history oculto en el $HOME)
              opción -c limpia el historial pero no borra .bash_history
              opción -w comienza la escritura del historial en .bash_history

hostname    muestra el servidor actual

man         manual de comando. Sintaxis man [sección] comando o directorio. Ejemplo: man 5 passwd
              seccion 1 - comandos generales
              seccion 2 - llamadas al sistema
              seccion 3 - biblioteca (funciones)
              seccion 4 - Fiheros especiales
              seccion 5 - Formato de ficheros
              seccion 6 - Juegos y salvapantallas
              seccion 7 - miscelánea
              seccion 8 - comandos de administracion sistema

mkdir       Crea una carpeta sintaxis `mkdir foldername` donde foldername puede ser un path relativo o absoluto.
              option `-p`. Crea la carpeta aunque no exista el folder contenedor. Es decir, crea la ruta completa que especifiquemos.


nl          muestra el fichero con lineas numeradas. No numera lineas en blanco igual que cat -b
              opción -ba si se pone numera también líneas en blanco

pwd         muestra el directorio actual

rm          Elimina ficheros admite opciones y multiples files. Admite paths absolutos o relativos.
            Admite wildcards o patterns para filtrar ficheros.
                opción -r borra recursivamente directorios y todo.
                opcion -ri igual que la anterior pero preguntando en interactivo si quermos eliminar cada carpeta


tac         igual que cat pero muestra las lineas del fichero en orden inverso

touch       Crea un archivo sintaxis `touch filename` donde filename puede ser en path relativo o absoluto.

uname       información del sistema. Por defecto opcion -s nombre del kernel (Linux)
              opción -s nombre del núcleo
              opción -r version del núcleo
              opción -v versión del sistema operativo
              opción -m muesra bits del nucleo
              opcion -a muestra toda la información

whoami      muestra el usuario actual
