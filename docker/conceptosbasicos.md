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
