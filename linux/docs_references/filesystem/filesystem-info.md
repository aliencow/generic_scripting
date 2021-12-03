## Locating info about file system

https://www.cyberciti.biz/tips/understanding-unixlinux-file-system-part-i.html
https://askubuntu.com/questions/94734/what-is-the-templates-folder-in-the-home-directory-for

#### Filesystem commands:

* `pwd`. Imprime en el terminal el directorio actual
* `~`. = `$HOME` Indica la carpeta home del usuario actual
* `ls`. Lista los contenidos del directorio actual o de otro si se le indica, ejemplo `ls /lib`.
* `cd`. Cambiar de directorio \ raiz ..\ baja un nivel ..\..\ baja dos . directorio actual. Sin argumentos nos lleva al direcTorio HOME.
* Tecla `tab`. Sirve para autocompletar el nombre de las carpetas
* `file`. Comando que muestra el tipo de archivo ej. `file prueba.text`


#### File extensions:

Las extensiones en linux no determinan el tipo de archivo.
Hay que textear los ficheros con el comando `file` para ver su contenido en terminal.

A linux no le importan las extensiones, se pueden usar las que se quieran.
Sin embargo a algún programa instalado si le pueden importar: ejemplo pdf reader.

### Wildcards o comodines (regular expressions)

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

* `touch`. Crea un archivo sintaxis `touch filename` donde filename puede ser en path relativo o absoluto.
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

* `locate`. Este comando sirve para localizar archivos introduciendo un pattern. ejemplo `locate *.conf`
  * option `-i`. Localiza sin tener en cuenta mayusculas o minusculas.
  * option `-l` o `--limit`. Limita el muestreo de resultados al número indicado detras (`-l 3` tres resultados).
  * option `-S` obtiene la ubicación de la base de datos que usa mlocate.
