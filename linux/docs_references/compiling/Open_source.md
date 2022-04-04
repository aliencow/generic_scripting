## HOW TO COMPILE code
de GNU.org descargamos en el menu software `coreutils`. Descargamos la ultima estable. En la lista cogemos el tar.xz con la versión más actual.
Una vez descargado, se desempaqueta con el comando tar usando las opciones `x` (extraer) `J` (compresion XZ file) y `f` (especificar fichero):
```
tar -xJf coreutils-9.0.tar.xz
```
dentro de la carpeta descomprimida buscamos la carpeta `src` que contiene los fuentes.
Vamos a modificar el comando  `ls` cuyo fichero fuente esta en `ls.c`.
Editamos el fichero y en la  función main le añadimos un `printf("Hello World");` o similar.

Descargamos el compilador de c (`gcc`) con esta instrucción:
```
sudo apt-get install gcc
```
Luego desde el raiz de coreutils ejecutar configure
```
bash configure
```
para que nos genere el makefile.

Para ejecutar el makefile necesitaremos la utilidad `make` la instalamos:
```
sudo apt-get install make
```
El comando make se ejecuta desde la misma carpeta donde esté instalado el makefile.

Una vez ejecutado make la instalacion se hace con
```
sudo make install
```
Se puede hacer en un solo paso
```
make && sudo make install

```
Este mismo ejemplo puede aplicarse a cualquier parte o core del GNU code.

### SOFTWARE REPOSITORIES

Los repositorios de software son almacenes deutilidades y software de los que se dispone para compilar y ejecutar en linux. Como una librería de software
https://help.ubuntu.com/community/Repositories/Ubuntu
Hay cuatro tipos de repositorios en ubuntu:
* Main. Lo mantienen los desarrolladores de ubuntu (free, open source)
* Universe. Lo mantiene la comunidad (free, open source)
* Restricted. Lo mantienen los propietarios de drivers (privado, puede ser open source)
* Multiverse. Limitado por copyright o temas legales (privado, puede ser open source)
Los paquetes de estos repositorios se pueden encontrar en este sitio:
https://packages.ubuntu.com/
`lsb_release -a` nos permite ver la version de ubuntu activa
Cada package contiene información respecto a:
* required - otros packages que son necesarios para que el que consultemos funcione.
* Recommended - No son obligatorios pero  se necesitan para el uso  normal.
* Suggested - Sugeridos para funcionar.
* Enhances - Mejoran el paquete de alguna manera.

Para gestionar todas estas dependencias o relaciones se utilizan los 'Package Managers'. `apt` (advanced package tool) es el manejador de paquetes de ubuntu

### Package management Using apt

* Comando `apt-cache`. Sirve para realizar busquedas y obtener informacion de los paquetes
  * Option `search`. permite buscar paquetes disponibles.
  En el siguiente ejemplo nos mostrará una linea de texto por cada paquete que encuentre referido al texto docx
  ```
  apt-cache search docx
  ```
  Si queremos acotar mas la busqueda con otro término podemos usar un grep a la salida
  Por ejemplo aquí se mostraran solamente las líneas que contenga los  paquetes referidos a docx si se ecnuentra la palabra text en ellas
  ```
  apt-cache search docx | grep text
  ```
  * Option `show`. Muestra la información sobre un paquete concreto.
  En el siguiente ejemplo mostraremos la información del paquete `docx2txt`:
  ```
  apt-cache show docx2txt
  ```
  Si la información es demasiado extensa podemos usar `less` al final para navegar
  ```
  apt-cache show docx2txt | less
  ```
