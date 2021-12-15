### Contenedor
* Virtualización a nivel de sistema operativo. (No hardware).
* Contiene todo lo necesario para ejecutar aplicaciones.
  * Codigo.
  * Runtime.
  * Herramientas del sistema.
  * Librerías del sistema.
* Puede ejecutar aplicaciones en paralelo.
* Se puede instalar distinto software.
* Ligero flexible y seguro.

### Docker
Es una forma de desplegar aplicaciones en un entorno controlado (contenedor) de forma sencilla y ligera.
#### Ventajas
* No requiere virtualización por hardware.
* Utiliza las funcionalidades del núcleo (kernel) de Linux.
* Aisla recursos (CPU, memoria, entrada/salida, etc.).
* Aisla la aplicación.
#### Requisitos.
* Kernel mayor o igual a 3.10
* Iptables >= 1.4
* cgroups
Con los contenedores eliminamos la necesidad de tener una virtualización con el sistema operativo completo.

### Instalación.
Ver las instrucciones de docker: https://docs.docker.com/engine/install/

### Primeros pasos
* `docker ps` Muestra los contenedores en ejecución.
* `docker ps -a` Muestra TODOS los contenedores.
* `docker run [options] <imagen>`. Ejecuta una imagen (centos, debian, python, etc.) si no la tiene cargada la descarga primero.
    * option `-d` run dettached.
    * option `-t` Alocate pseudo tty
    * option `-i` Keep STDIN open
    * option `-a` Attach to `STDIN`, `STDOUT` and/or `STDERR`.
    Opciones separadas:
      * option `--name` + ` <nombre_que_queremos>` pone ese nombre específico al contendor que queremos.
* `docker rm <container>`. Elimina el contendor especificaod

### Exponer puertos
Nos permite acceder a los contenedores desde fuera de docker. Opcion -p
Para comprobar los puertos expuestos de un contenedor podemos usar este comando:
`docker inspect -f "{{ .ContainerConfig.ExposedPorts }}" <contendor>`

El contendor httpd expone el puerto 80 y lo recibimos con el 8080 de nuestro local host.
`docker run -dti -p 8080:80 httpd`
Ejecutando `curl http://localhost:8080` accede al contenido del container.

### opciones comunes
* `docker start` + ` <idcontenedor>`. Arranca un contenedor
* `docker restart` + ` <idcontenedor>`. Reinicia un contenedor
* `docker rm` + ` <idcontenedor>`. Elimina un contenedor
* `docker attach` + ` <idcontenedor>`. Accede a la consola del contendor (si existe). Si ejecutamos `exit` o `Ctrl+d` salimos de la consola y del contenedor.. Si no queremos cerrar el contenedor teclearemos `Ctrl+p` y luego `Ctrl+q`, volveremos a nuestra consola pero el contenedor se sigue ejecutando.
* `docker exec` + `-ti <idcontenedor> <comando>`. Ejecuta un comando sobre un contenedor en ejecución, si queremos entrar en la consola sin interrumpir el comando que pondremos será /bin/bash (Siempre que sea un contenedor linux o similar)
* `docker rename` + ` <idcontenedor>`  `<nuevonombre>`. Cambia el nombre del contenedor al nuevo indicado.
  * Comandos informativos.
    * `docker ps [options]`. Proporciona información sobre los contenores en ejecución o ya ejecutados.
      * no options. Muestra los contenedores en ejecución.
      * option `-a`. Muestra todos los contenedores cargados.
      * option `-l`. Muestra el ultimo contenedor ejecutado.
    * `docker stats`. Muestra estadisticas de los contenedores en ejecución. (consumo de recursos).
    * `docker top` + ` <idcontenedor>`. Muestra un historial de utilización del contenedor
    * `docker logs` + ` <idcontenedor>`. Muestra los logs del contenedor
      * option `-f`. Muestra los logs en tiempo real

### Trabajar con imágenes
* `docker images`. Lista las imágenes disponibles en el servidor.
* `docker search` + ` <nombreimagen>`. Busca una imagen en el repositorio de docker. Si ponemos `<nombreimagen>|head` limita la búsqueda a las cabeceras.
* `docker pull` + ` <nombreimagen>`. Descargamos una imagen concreta del respositorio de docker.
* `docker commit` + ` <idcontenedor>` + ` <nombreimagen>`. Convierte un contenedor en una nueva imagen. Ejemplo ejecutamos un contedor debian instalamos el vim u otra cosa y sobre ese contenedor generamos nuestra propia imagen.
* `docker history` + ` <nombreimagen>`. Muestra el historial sobre esa imagen.
* `docker tag` + ` <nombreimagen>` + ` <etiqueta>`. Permite etiquetar una imagen. Crea una nueva imagen con esa etiqueta copia de la etiquetada si añadimos `<etiqueta>:<version>` añade la versión que indiquemos (por defecto `latest`).
* `docker rmi` + ` <nombreimagen>` + `[:<version]`. Elimina la imagen con la versión especificada (opcional). Fallará si hay algún contenedor con la imagen en ejecución.

### Comunicando contenedores
* `docker run`+`[<opciones>]`. Este es el comando de docker mas extenso tiene muchas opciones que nos permitirán trabajar con los contenedores de varias maneras.
  * option `--name` + ` <customname>`. Con esta opción el contenedor generado se creará con el nombre indicado
  * option `--hostname` + ` <customname>`. Con esta opcion el ID del usuario que aparecera en el bash del contenedor, y que servirá de alias si está en una rede de contenedores.
  * option `--network` + ` <customname>`. Conecta el contenedor creado a la red que se especifica.
  * option `-d` run dettached.
  * option `-t` Alocate pseudo tty
  * option `-i` Keep STDIN open

#### Redes internas docker para contectar containers entre si

Docker permite crear una red interna propia con los contenedores, dentro de la red se mantienen actulizadas las ips y los hostmane (gracias a un DNS interno) Es decir los contenedores dentro de la misma red se 'ven' entre si y pueden conectarse por ip o por hostname, de hecho docker por defecto si no se especifica network ni hostname los conecta a la red `bridge` por defecto. Los contenedores para poder conectarse entre sí tienen que estar en la misma red. Lo mejor para no perdernos con links ni con ips es crear nuestra propia red de contendores.

* `docker network ls`. Este comando lista las redes de contendores.
* `docker network inspect <red>`. Mostrará la lista de contenedores conectados en esta red (defecto `bridge`). Si es una red creada por nosotros podemos ver la subnet (rango de ips que podemos usar)
* `docker network create`. Opcion para crear redes
  * + `[-d bridge] <nombrered>`. Crea nuestra propia red de docker. la opcion `-d bridge` permite conectarse al exterior.
  * + `--help`. Muestra la ayuda para docker network create (se pueden especificar randos de ips por ejemplo)
  * `docker network connect` + ` <netname>` + ` <containername>`. Permite conectar el contenedor containername a nuestra red.
  * `docker network disconnect` + ` <netname>` + ` <containername>`. Permite desconectar el contenedor containername de nuestra red.

### Donde se almacenan los contenedores
Depende del tipo de driver que tenga la unidad de almacenamiento. El directorio principal el `/var/lib/docker`.
Para ver que driver de almacenamiento tenemos ejecutaremos el comando `docker info` y en la salida buscamos la etiqueta `Storage driver:`
En el caso de synology el almacen esta en /volume1/@docker En WSL hay que investigarlo
