## Locating info about file system

https://www.cyberciti.biz/tips/understanding-unixlinux-file-system-part-i.html
https://askubuntu.com/questions/94734/what-is-the-templates-folder-in-the-home-directory-for

#### Filesystem commands:

* `pwd`. Imprime en el terminal el directorio actual
* `~`. = `$HOME` Indica la carpeta home del usuario actual
* `ls`. Lista los contenidos del directorio actual o de otro si se le indica, ejemplo `ls /lib`.
* `cd`. Cambiar de directorio \ raiz ..\ baja un nivel ..\..\ baja dos . directorio actual. Sin argumentos nos lleva al direcTorio HOME.
* Tecla `tab`. Sirve para autocompletar el nombre de las carpetas
* `file`. Comando que muestra el tipo de archivo ej. file prueba.text


#### File extensions:

Las extensiones en linux no determinan el tipo de archivo.
Hay que textear los ficheros con el comando `file` para ver su contenido en terminal.

A linux no le importan las extensiones, se pueden usar las que se quieran.
Sin embargo a algún programa instalado si le pueden importar: ejemplo pdf reader.

### Wildcards o comodines (regular expressions)
