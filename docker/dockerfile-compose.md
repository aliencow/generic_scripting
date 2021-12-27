## Fichero Dockerfile

Fichero que se usa como punto de partida para crear imagenes en docker
Funciona como un makefile de linux.
Necesita extender una imagen base.
Genera una nueva imagen
### Instrucciones (ver código de ejemplo)
* `FROM <imagename>`. Indica la imagen de partida sobre la que se trabaja.
* `MAINTAINER <name>`. Indica el nombre del que mantiene la imagen
* `RUN <command>`. Indica que comando/s se van a utilizar cuando se genere la imagen.
* `ENV <key>=<value>`. Permite ingresar variables de entorno
* `CMD [<command>]`. Va a ser el comando que se ejecute cuando ejecutemos un contenedor con esta imagen.
* `LABEL <key>=<value>`. Permite añadir etiquetas a la imagen.
* `EXPOSE <port> [<port>]`. Indica que puerto o puertos vamos a exponer al exterior.
* `ADD <localfile> <imagefile>`. Añade ficheros a la imagen
* `COPY <localfile> <imagefile>`. Copia fichero a la imagen
* `ENTRYPOINT [<cmd>, <args>, ..]`. Comando que se ejecuta cada vez que se ejecute la imagen.
* `VOLUME <folder>`. Crea un volumen en la imagen
* `WORKDIR <folder>`. Directorio de trabajo.

Ejemplo sacado de aquí: https://github.com/bylexus/docker-apache-php55/blob/master/Dockerfile


      FROM ubuntu:14.04
      MAINTAINER Alexander Schenkel <alex@alexi.ch>

      VOLUME ["/var/www"]

      RUN apt-get update && \
          apt-get install -y \
            apache2 \
            php5 \
            php5-cli \
            libapache2-mod-php5 \
            php5-gd \
            php5-json \
            php5-ldap \
            php5-mysql \
            php5-pgsql

      COPY apache_default /etc/apache2/sites-available/000-default.conf
      COPY run /usr/local/bin/run
      RUN chmod +x /usr/local/bin/run
      RUN a2enmod rewrite

      EXPOSE 80
      CMD ["/usr/local/bin/run"]

### Docker build
Este comando genera una imagen a partir de un Dockerfile
la sintaxis es `docker build [options] <folder>`
* `docker build [<options>] <folderfrom>`. La carpeta `<folderfrom>` indica donde buscará los ficheros docker para generar la imagen. Si es en el dicrecorio actual poner `.`.
  * option `-t, --tag` + ` <nombre>`. Permite customizar el nombre de la imagen.
  * option `-f, --file` + ` <Dockerilename>`. Permite usar un custom docker file ubicado en otra parte, o que no se llame con el nombre por defecto (`Dockerfile`).
  * option `--no-cache`. Do not use cache when building the image. Construye desde 0

## Docker compose
Docker compose es una herramienta para definir y ejecutar multiples contenedores.
Funciona en 3 pasos:
* Definir el Dockerfile para cada aplicación.
* Definir docker-compose.yml
* Ejecutar `docker-compose up [-d]`
* `docker compose`.
  * `build`       Build or rebuild services
  * `convert`     Converts the compose file to platform's canonical format
  * `cp`          Copy files/folders between a service container and the local filesystem
  * `create`      Creates containers for a service.
  * `down`        Stop and remove containers, networks. Comando de parada. IMPORTANT!
  * `events`      Receive real time events from containers.
  * `exec`        Execute a command in a running container.
  * `images`      List images used by the created containers
  * `kill`        Force stop service containers.
  * `logs`        View output from containers
  * `ls`          List running compose projects
  * `pause`       Pause services
  * `port`        Print the public port for a port binding.
  * `ps`          List containers
  * `pull`        Pull service images
  * `push`        Push service images
  * `restart`     Restart containers
  * `rm`          Removes stopped service containers
  * `run`         Run a one-off command on a service.
  * `start`       Start services
  * `stop`        Stop services
  * `top`         Display the running processes
  * `unpause`     Unpause services
  * `up`          Create and start containers. Comando de arranque. IMPORTANT!
  * `version`     Show the Docker Compose version information
