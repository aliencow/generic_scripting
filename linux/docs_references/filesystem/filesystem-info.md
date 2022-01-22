## Locating info about file system

https://www.cyberciti.biz/tips/understanding-unixlinux-file-system-part-i.html
https://askubuntu.com/questions/94734/what-is-the-templates-folder-in-the-home-directory-for

### Filesystem commands:

* `pwd`. Imprime en el terminal el directorio actual
* `~`. = `$HOME` Indica la carpeta home del usuario actual
* `ls`. Lista los contenidos del directorio actual o de otro si se le indica, ejemplo `ls /lib`.
  * option `-l`. Muestra una lista ordenada.
  * option `-a`. Muestra ficheros y carpetas ocultos (en linux empiezan por .)
  * option `-i`. Muestra la ubicación física del archivo en la primera columna
  * option `-R`. Recursivo
* `cd`. Cambiar de directorio \ raiz ..\ baja un nivel ..\..\ baja dos . directorio actual. Sin argumentos nos lleva al direcTorio HOME.
* Tecla `tab`. Sirve para autocompletar el nombre de las carpetas
* `file`. Comando que muestra el tipo de archivo ej. `file prueba.text`


### File extensions:

Las extensiones en linux no determinan el tipo de archivo.
Hay que textear los ficheros con el comando `file` para ver su contenido en terminal.

A linux no le importan las extensiones, se pueden usar las que se quieran.
Sin embargo a algún programa instalado si le pueden importar: ejemplo pdf reader.

#### Wildcards o comodines (regular expressions)

Las regular expressions trabajan contra el código ascii  y ordenan por ese orden
https://www.asciitable.com/

Info genérica sobre wildcards
http://www.linfo.org/wildcard.html
https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm
Visualizer gratuito de regular expressions https://regex101.com/

* `*`. Sustituye nombres completos ej: `ls *`  mostraría todos los directorios files, subdirectorios y files dentro de los mismos. ej: `ls D*` mostraría contenido de directorios que comiencen por la letra D.
* `?`. Sustituye caracteres individuales ej: `ls ????` devolverá todo lo que encuentre que tenga exactamente 4 caracteres. ej: `ls ?it??.txt` devolverá todos los ficheros que con cinco dígitos que terminen en .txt y que contenga de segundo caracter la `i` y de tercero la `t`.
* `[]`. Indicar rangos de búsqueda ej `[aeiou]` buscará las vocales en minúscula `[AEIOU]` en mayúscula. Si se incluye el signo `-` se puede especificar desde hasta ej `[a-z]` buscará todas las letras del alfabeto minúsculas, `[A-Za-z]` buscará tanto mayúscusculas como minúsculas o `[0-9a-z]` caracteres numéricos y alfabeto minúscula. Si añadimos `^` dentro del rango sirve para negar la condición. Ejemplo `[^a-z]` buscaría las letras del alfabeto excepto las minúsculas. Para incluir el signo `-` en la búsqueda como caracter lo pondremos precedido del carater de escape `\` `[\-a-z]` o bien al final del rango `[a-z-]`. Ej: `ls file[0-9].txt` listará todos los ficheros que se llamen file y tengan un dígito en el 5ª caracter ('file1.txt, file9,txt, etc.').
* `{}`. Permite añadir una lista separada por comas a la hora de ejecutar creación de fichoeros etc. ej: `mkdir {uno,dos,tres}` crearia 3 directorios uno dos y tres.

### Creating files and folders

* `touch`. Crea un archivo sintaxis `touch filename` donde filename puede ser en path relativo o absoluto. Si el fichero ya existe cambia la fecha de creación del fichero. Usando opciones se pueden modificar las fechas de fichero.
  * option `-a`. Cambia la fecha de acceso.
  * option `-m`. Cambia la fecha de modificación.
  * option `-d` + ` <fecha>`. especifica una fecha concreta.
* `stat`. Nos muestra información sobre un fichero concreto. Fecha de creación de acceso propietario etc.
* `echo`. Se puede usar este comando para crear un fichero redireccionando la salida. ej. `echo "hello" > myfile.txt`.
* `mkdir`. Crea una carpeta sintaxis `mkdir foldername` donde foldername puede ser un path relativo o absoluto.
  * option `-p`. Crea la carpeta aunque no exista el folder contenedor. Es decir, crea la ruta completa que especifiquemos.

* `{}`. Permite añadir una lista separada por comas a la hora de ejecutar creación de fichoeros etc. ej: `mkdir {uno,dos,tres}` crearia 3 directorios uno dos y tres. Acepta rangos como `{2..20}` o `{a..z}` Se puede combinar con touch y mkdir.

### Deleting files and folders

* `rm`. Elimina ficheros admite opciones y multiples files. Admite paths absolutos o relativos. Admite wildcards o patterns para filtrar ficheros.
  * option `-r` borra recursivamente directorios y todo y con
  * option `-ri` hace lo mismo que la anterior pero preguntando si queremos eliminar cada directorio.

* `rmdir`. Elimina carpetas en lugar de ficheros en SOLAMENTE si estan vacios.

### Copy and paste files and and folders

* `cp`. Copia de fuente a destino archivos se pueden especificar varios origenes y un destino.
  * option `-t`. copia recursivamente el contenido de las carpetas a copiar

### Moving and renaming files and and folders

* `mv`. Se utiliza para renombrar ficheroa mv oldname.txt newname.txt se aplica tambien a carpetas y no afecta a contenidos de la carpeta. Tambien se utiliza para mover ficheros o carpetas de un sitio a otro o para mover y cambiar de nombre al mismo tiempo. Es un comando superpoderoso.

### Info about nano text editor

El fichero de configuración de nano esta en `/etc/nanorc`

Nota: la combinación de teclas para reemplazar `^\` (`Ctrl+\`) no se encuentra en teclado español. En su defecto usaremos el atajo de teclado `Alt+r` que hace la misma función.
Lo mismo (parecido) pasa con buscar línea columna `^_` (`Ctrl+_`)para la que hay que seleccionar `Ctrl+Shift+_` o bien simplemente `Alt+g`

los simbolos de teclas son:
 `^` Se refiere a `Ctrl`
 `M-` Se refiere a `Alt`, `Esc` o `Cmd` segun el sstema operativo y teclado en nuestro caso es `Alt`.

### The locate comand

NOTA RESPECTO A LOCATE:
Depending on what distribution you are running the locate command may not come pre-installed. Ubuntu 20.04 appears to have this issue, for example, but Ubuntu 18.04 does not.

If you find you are having issues, try installing the locate  and mlocate packages from your repositories.

`sudo apt install locate`
`sudo apt install mlocate`

* `locate`. Este comando sirve para localizar archivos introduciendo un pattern. ejemplo `locate *.conf`. Juega en conjunto con `updatedb` para actualizar la base de datos. Ver `su `
  * option `-i`. Localiza sin tener en cuenta mayusculas o minusculas.
  * option `-l` o `--limit`. Limita el muestreo de resultados al número indicado detras (`-l 3` tres resultados).
  * option `-S` obtiene la ubicación de la base de datos que usa mlocate.
  * option `-e` antes de mostrar resultados comprueba que los ficheros existan por si la base no está actualizada.
* `updatedb`. Funciona conjuntamente con `locate` sirve para actualizar la base de datos de búsqueda de ficheros. Solo lo puede ejecutar su. Ver `locate`


### Busquedas en ficheros comando find.
Find es uno de los mas importantes comandos de linux. Permite busquedas de ficheros entre otras cosas y es un poco más lento que locate ya que realiza una búsqueda REAL por el filesystem.

* `find`. Este comando busca cualquier archivo si no se ponen parametros busca recursivamente todas las carpetetas y ficheros  a partir del directorio actual. Si se indica una carpeta concreta a continuación busca desde esa carpeta recursivamente.
  * option `<start_path>`. `<start-path>` es el nombre del directorio a partir del que queremos realizar la búsqueda.
  * option `-maxdepth <number>`. Especifica el nivel de profundidad (en cuanto a directorios) sobre el que queremos realizar la búsqueda `<number>` indica la profundidad (1 dir actual, 2 carpetas 'hijas', 3 carpetas 'nietas' y así sucesivamente). Si se especifica esta opción debe ir de primera.
  * option `-type <tipo>`. Especifica el tipo de búsqueda. `<tipo>` puede ser `f` para files o `d` para folders (directory).
  * option `-name "<pattern>"`. Busca por nombre en el arbol especificado. `<pattern>` va entrecomillado y puede ser el literal del nombre o un patron concreto ej. "*.txt". Es decir permite usar regular expressions.
  * option `-iname "<pattern>"`. Busca por nombre en el arbol especificado, en este caso no es CASE SENSITIVE (sensible a mayusculas). `<pattern>` va entrecomillado y puede ser el literal del nombre o un patron comcreto ej. "*.txt". Es decir permite usar regular expressions.
  * option `-size -<tam>k o +<tam>M`. Filtra los resultados por tamaño del fichero donde tam es un número que indica los k (kilobytes), M (megabyte) o G(gibabyte) que debe tener el fichero y `+` indica que buscará mayores que y `-` indica que buscará menores que. Puede haber mas de una opción `-size`. Ej: `file /home -type f -size -10M -size +50k` filtrará los ficheros dentro de `/home` que tengan un tamaño menor de 10M o mayor que 50k.
  * option `-exec <command> \;`. Permite ejecutar un comando con la salida de find. Es importante indicar `\;` como finalización del comando Para recoger la salida de find usaremos `{}` Ej: `find  ~ -type f -size -5M -exec cp {} ~/Escritorio/copy_here \;` copiará todos los ficheros debajo del home menores de 5M a  la carpeta `copy_here` del escritorio.
  * option `-ok <command> \;` . Exactamente igual que exec y misma funcionalidad solo que nos pide que confirmemos cada vez que se ejecute el comando.
