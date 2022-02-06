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



* `cat`.Muestra el contenido de fichero en el la pantalla. Puede mostrar el contenido de varios ficheros
  * option `-n` muestra el número de línea
  * option `-b` igual que -n pero no numera líneas vacias o en blanco.

* `cd`. Cambiar de directorio \ raiz ..\ baja un nivel ..\..\ baja dos . directorio actual
  * option /ruta/o/path Se cambia  de directorio a la ruta indicada que puede ser absoluta o relativa.
  * Sin opciones. Sin argumentos se cambiará al directorio HOME del usuario actual.

* `chmod`. Cambia los permisos de ficheros o directorios. La sintaxis es `chmod <permisos> <fichero/carpeta>` donde permiso puede ser octal (en número) o modo (letra). Ejemplo: `chmod 750 <filename>` o `chmod u=rwx,g=rx,g= <filename>`
  * option `-R`. Aplica los cambios de modo recursivo
  * option `-v`. Verbose
  * option `-c`. Muestra cambios realizados

* `chgroup`. Change group. Igual que `chown` pero solo para grupos.

* `chown`. Change owner. Sirve para modificar los permisos de un archivo carpeta o archivo. La sintaxis es `chown <propietario>:<grupo> <ficheros/carpetas>`. Ejemplo `chown juan:juan micarpeta`. Opciones de usuario grupo pueden ser: <usuario>, <ususario>:<grupo>, <usuario>.<grupo>, .<grupo> o :<grupo>. Solo lo puede ejecutar un usuario root.
    * option `-R`. Recursivo
    * option `-v`. Verbose
    * option `-c`. Muestra los cambios realizados

* `clear`.  o ctrl+L limpia de comandos la pantalla.

* `cp`. Copia de fuente a destino archivos se pueden especificar varios origenes y un destino.
  * option `-t` copia recursivamente el contenido de las carpetas a copiar.


* `cut`. Corta o separa por columnas el contenido de un fichero.
  * option -d indica el delimitador entre columnas. ej. si es ';' la option -d;
  * option `-f`. selecciona el número de columnas a visualizar ej. -f3 tercera columna -f3,4 tercera y cuarta, -f2-5 de la dos a la cinco, etc.
  * option `-c`. especifica los caracteres a cortar ej. -c 2 coge dos caracteres -c 9-10 coge los caracteres del 9 al 20.

* `echo`. Muestra en la salida extandar el texto o file que se indique. Se puede usar este comando para crear un fichero redireccionando la salida. ej. `echo "hello" > myfile.txt`.

* `find`. Este comando busca cualquier archivo si no se ponen parametros busca recursivamente todas las carpetetas y ficheros  a partir del directorio actual. Si se indica una carpeta concreta a continuación busca desde esa carpeta recursivamente.
  * option `<start_path>`. `<start-path>` es el nombre del directorio a partir del que queremos realizar la búsqueda.
  * option `-maxdepth <number>`. Especifica el nivel de profundidad (en cuanto a directorios) sobre el que queremos realizar la búsqueda `<number>` indica la profundidad (1 dir actual, 2 carpetas 'hijas', 3 carpetas 'nietas' y así sucesivamente). Si se especifica esta opción debe ir de primera.
  * option `-type <tipo>`. Especifica el tipo de búsqueda. `<tipo>` puede ser `f` para files o `d` para folders (directory).
  * option `-name "<pattern>"`. Busca por nombre en el arbol especificado. `<pattern>` va entrecomillado y puede ser el literal del nombre o un patron concreto ej. "*.txt". Es decir permite usar regular expressions.
  * option `-iname "<pattern>"`. Busca por nombre en el arbol especificado, en este caso no es CASE SENSITIVE (sensible a mayusculas). `<pattern>` va entrecomillado y puede ser el literal del nombre o un patron comcreto ej. "*.txt". Es decir permite usar regular expressions.
  * option `-size -<tam>k o +<tam>M`. Filtra los resultados por tamaño del fichero donde tam es un número que indica los k (kilobytes), M (megabyte) o G(gibabyte) que debe tener el fichero y `+` indica que buscará mayores que y `-` indica que buscará menores que. Puede haber mas de una opción `-size`. Ej: `file /home -type f -size -10M -size +50k` filtrará los ficheros dentro de `/home` que tengan un tamaño menor de 10M o mayor que 50k.
  * option `-exec <command> \;`. Permite ejecutar un comando con la salida de find. Es importante indicar `\;` como finalización del comando Para recoger la salida de find usaremos `{}` Ej: `find  ~ -type f -size -5M -exec cp {} ~/Escritorio/copy_here \;` copiará todos los ficheros debajo del home menores de 5M a  la carpeta `copy_here` del escritorio.
  * option `-ok <command> \;` . Exactamente igual que exec y misma funcionalidad solo que nos pide que confirmemos cada vez que se ejecute el comando.


* `history`. Muestra historial de comandos (se almacena en .bash_history oculto en el $HOME)
  * option `-c` limpia el historial pero no borra .bash_history
  * option `-w` comienza la escritura del historial en .bash_history

* `hostname`. Muestra el servidor actual

* `locate`. Este comando sirve para localizar archivos introduciendo un pattern. ejemplo `locate *.conf`. Juega en conjunto con `updatedb` para actualizar la base de datos. Ojo en algunas versiones de linux no viene instalado. Para instalarlo estas dos líneas con sudo `sudo apt install locate` y `sudo apt install mlocate`. Ver `upadatedb`
  * option `-i`. Localiza sin tener en cuenta mayusculas o minusculas.
  * option `-l` o `--limit`. Limita el muestreo de resultados al número indicado detras (`-l 3` tres resultados).
  * option `-S` obtiene la ubicación de la base de datos que usa mlocate.
  * option `-e` antes de mostrar resultados comprueba que los ficheros existan por si la base no está actualizada.

* comando `ln`. Crear enlaces simbólicos o duros. Si no se especifican opciones crea un enlace duro.
	* option `-s`. Junto con la ruta del fichero o directorio para crear enlaces simbólicos. Ejemplo: ln -s <fichero o carpeta ref> <fichero simbólico>.


* `ls`. Lista los contenidos del directorio actual o de otro si se le indica, ejemplo `ls /lib`.
  * option `-l`. Muestra una lista ordenada.
  * option `-a`. Muestra ficheros y carpetas ocultos (en linux empiezan por .)
  * option `-i`. Muestra la ubication física del archivo en la primera columna
  * opcion `-R`. Recursivo

* `man`. Manual de comandos. Sintaxis man [section] comando o dire  * ctorio. Ejemplo: man 5 passwd
  * seccion 1 - comandos generales
  * seccion 2 - llamadas al sistema
  * seccion 3 - biblioteca (funciones)
  * seccion 4 - Fiheros especiales
  * seccion 5 - Formato de ficheros
  * seccion 6 - Juegos y salvapantallas
  * seccion 7 - miscelánea
  * seccion 8 - comandos de administracion sistema

* `mkdir`. Crea una carpeta sintaxis `mkdir foldername` donde foldername puede ser un path relativo o absoluto.
  * option `-p`. Crea la carpeta aunque no exista el folder contenedor. Es decir, crea la ruta completa que especifiquemos.

* `mv`. Se utiliza para renombrar ficheroa mv oldname.txt newname.txt se aplica tambien a carpetas y no   afecta a contenidos de la carpeta. Tambien se utiliza para mover ficheros o carpetas de un sitio a otro o para mover y cambiar de nombre al mismo tiempo. Es un comando superpoderoso.

* `nl`. muestra el fichero con lineas numeradas. No numera lineas en blanco igual que `cat -b`
  * option `-ba` si se pone numera también líneas en blanco

* `pwd`. Muestra el directorio actual
  * option `-P` muestra el directorio de origen en el caso de un simbolic link.

* `rev`. Igual que cat pero pone el orden inverso los caracteres de cada línea.

* `rm`. Elimina ficheros admite opciones y multiples files. Admite paths absolutos o relativos. Admite wildcards o patterns para filtrar ficheros.
  * option `-r`. borra recursivamente directorios y todo.
  * opcion `-ri` igual que la anterior pero preguntando en interactivo si quermos eliminar cada carpeta

* `rmdir`. Elimina carpetas en lugar de ficheros en SOLAMENTE si estan vacios.

* `stat`. Nos muestra información sobre un fichero concreto. Fecha de creación de acceso propietario etc.

* `tac`. Igual que cat pero muestra las lineas del fichero en orden inverso

* `touch`. Crea un archivo sintaxis `touch filename` donde filename puede ser en path relativo o absoluto. Si el fichero ya existe cambia la fecha de creación del fichero. Usando opciones se pueden modificar las fechas de fichero.
  * option `-a`. Cambia la fecha de acceso.
  * option `-m`. Cambia la fecha de modificación.
  * option `-d` + ` <fecha>`. especifica una fecha concreta.

* `updatedb`. Funciona conjuntamente con `locate` sirve para actualizar la base de datos de búsqueda de ficheros. Solo lo puede ejecutar su.


* `umask`. Muestra o modifica la máscara utilizada cuando creamos ficheros o directorios. Cada usuario tiene una máscara para creación de ficheros. Solo `umask` muestra la máscara actual y con `umask <mascara>` cambia a la especificada. La máscara son 4 dígitos tomamos los ultimos 3 y de ellos el primero esta asociado a usuario el segundo a grupo y el tercero a otros. Esos tres dígitos se restan de 666 (máximos permisos) para ficheros y de 777 (maximos permisos) para carpetas y nos darán los permisos. Ej. si la umask es 022 los permisos para ficheros son 666-022 = 644 y para carpetas 777-022 = 755. Se aplica a los ficheros creados después de ejecutar umask.

* `uname`. Information del sistema. Por defecto opcion -s nombre del kernel (Linux)
  * option `-s` nombre del núcleo
  * option `-r` version del núcleo
  * option `-v `versión del sistema operativo
  * option `-m` muesra bits del nucleo
  * option `-a` muestra toda la information

* `wc`. Acrónimo de word count. Devuelve el número de líneas palabras o caracteres que contiene el fichero especificado o que devuelve el comando anterior si se usa con pipe (`|`). Ej: `wc <mifichero>` devolverá `17 40 239 <mifichero>` es decir, el fichero tiene 17 lineas, 40 palabras y 239 caracteres.
* option `l`. Muestra solo numero de líneas.
* option `w`. Muestra solo numero de palabras.
* option `m`. Muestra solo numero de caracteres.

* `whoami`. Muestra el usuario actual.
