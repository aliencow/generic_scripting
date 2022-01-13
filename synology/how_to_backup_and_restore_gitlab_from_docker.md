# COMO HACER LA COPIA DE SEGURIDAD DE GITLAB Y RESTAURARLA

## HACER LA COPIA DE SEGURIDAD

### Tutoriales �tiles e info �tiles para esta tarea.

#### Tutorial para hacer la copia de seguridad de gitlab.
https://copdips.com/2018/09/backup-and-restore-gitlab-in-docker.html

#### Readme de imagen de docker que utilizamos.
https://github.com/sameersbn/docker-gitlab

#### Readme para hacer el backup desde el contenedor de docker de gitlab:
tutorial del comando rake: https://github.com/sameersbn/docker-gitlab#rake-tasks

#### Nota para acceder al contenedor de gitlab mientras se ejecuta
para acceder al contenedor ejecutar:
sudo docker exec -it synology_gitlab bash

#### Informaci�n respecto a los contendores implicados
La aplicaci�n se ejecuta usando tres contenedores docker vinculados entre s�, estos contendores se generan a partir de las siguientes im�genes docker:

* `sameersbn/gitlab:13.12.2`. Contiene la aplicaci�n de gitlab. Est� vinculado con los otros dos y se le nombra en el sistema como `synology_gitlab`. 
* `sameersbn/postgresql:12-20200524`. Contiene la base de datos (`postgresql`). El primer contenedor obtiene los datos de aqu�. Se nombra en el sistema como `synology_gitlab_postgresql`. Alias interno `db`.
* `sameersbn/redis:4.0.9-1`. Contiene la aplicaci�n redis (Almac�n de datos en memoria, se usa como cach�). El primer contenedor lo usa como cach�. Se nombra en el sistema como `synology_gitlab_redis`. Alias interno `redisio`          

NOTA: para acceder a cualquiers de los contenedores desde un terminal (ssh) se usa el comando: `sudo docker exec -it <contenedorID> bash`, donde `contenedorID` es el nombre del contenedor indicado arriba. Por ejemplo acceder a gitlab:

	sudo docker exec -it synology_gitlab bash

#### Estructura de volumenes de las contenedores docker implicados.
El docker de gitlab tiene mapeados los datos a un volumen (folder) local `/volume1/docker/gitlab/gitlab:/home/git/data`
esto significa que la carpeta dentro del contenedor `/home/git/data` guarda sus contenidos en la carpeta local `/volume1/docker/gitlab/gitlab`.
Asimismo la base de datos(`postgresql`) que esta en un contenedor vinculado a su vez almacena la base de datos en un  volumen local `/volume1/docker/gitlab/postgresql:/var/lib/postgresql`
Es decir la carpeta dentro del contenedor `/var/lib/postgresql` guarda un reflejo de sus contenidos en la carpeta local   `/volume1/docker/gitlab/postgresql`.


### Pasos para ejecutar realizar el backup

1 Ejecutar el backup sin cerrar el contenedor (desde el host) para ello abriremos una terminal contra argonte y ejecutamos el siguiente comando(Ejecutar como sudo).

	sudo docker exec --user git -it <contenedorID> bundle exec rake gitlab:backup:create RAILS_ENV=production
	
El contenedorID es `synology_gitlab`. Esta instrucci�n realizara unbackup de TODOS (los tres) contenedores. Ya que ejecuta un comando Ruby incluido en el contenedor de gitlab para tal efecto.
Lo que hace es generar un fichero tar autonombrado que contiene la copia de seguridad y lo guarda en la carpeta interna (dentro del contenedor gitlab) `/home/git/data/backups`.
Como la carpeta `/home/git/data` esta mapeada mediante un volumen docker a la carpeta local `/volume1/docker/gitlab/gitlab` tendremos tambien en local dicho fichero tar en la carpeta `/volume1/docker/gitlab/gitlab/backups`
	
2 Copiar la configuraci�n y secretos (claves) aparte. Existen dos ficheros de configuraci�n: `gitlab.yml` y `secrets.yml` necesarios para recuperar la copia de seguridad que NO SE INCLUYEM en el tar ya que su ubicaci�n en el conteneor es `/home/git/gitlab/config`
Dicha ubicaci�n no tiene un volumen mapeado por lo que es necesario copiar estos ficheros aparte. Se pueden copiar mediante un comando de docker desde dentro del contenedor a una carpeta local. Yo por seguridad copi� toda la carpeta `config`.
Desde un terminal conectado a argonte se ejecuta:

	sudo docker cp synology_gitlab:/home/git/gitlab/config /volume1/docker/gitlab/gitlab/backups

lo que nos dejar� la carpeta config del contenedor dentro de `/volume1/docker/gitlab/gitlab/backups` lo dej� ah� para tener la copia de seguirdad toda junta en local.
* NOTA IMPORTANTE: Para restaurar la copia de seguridad tiene que hacerse desde un contenedor generado CON LA MISMA IMAGEN DOCKER con la que se hizo la copia.

## RESTAURAR COPIA DE SEGURIDAD

### Tutoriales �tiles e info �tiles para esta tarea.

#### Para recuperar los secrets de gitlab (tutorial)
https://docs.gitlab.com/ee/raketasks/backup_restore.html#storing-configuration-files

#### Tutorial fantastico para levantar un docker compose.
https://blog.golimb.com/2017/07/16/synology-docker-gitlab-redis-postgresql/

#### Informaci�n respecto a docker-compose 
Antes de restaurar la copia de seguridad tenemos que tener en ejecuci�n los tres contenedores indicados al principio. Tenemos que pensar que en la versi�n de DSM nueva no disponemos ya del package gitlab.
Es decir antes de poder recuperar la copia tendremos que levantar las tres im�genes con las mismas configuraciones y par�metros que ten�an antes. Para ello empleamos docker-compose una utilidad de docker que permite hacerlo.
docker-compose para funcionar necesita un fichero con el mismo nombre y extensi�n `yml` (yaml) o sea: `docker-compose.yml`.
Este fichero de configuraci�n indica a docker que imagenes descargar, que puertos y volumenes comparten los contenedores etc. 
Tras mucha investigaci�n y pruebas he conseguido generar un fichero `docker-compose.yml` que funciona y permite hacerlo. (Testeado en proteo con DSM.7). Contiene el c�digo que figura al final de este documento.

### Pasos para restaurar el backup.

1 Levantamos los contenedores implicados [indicados al principio](#informaci�n-respecto-a-los-contendores-implicados). Para ello ejecutamos el docker compose. Debemos ejecutarlo desde el terminal ubicandonos primero el la carpeta adecuada.

```bash	
cd /volume1/docker/gitlab/
sudo docker-compose up -d 
```
	
La opci�n `-d` indica que se ejecute no verbose en background. Se aconseja no ponerla la primera vez que lo ejecutemos. Cuando queramos terminar la ejecucion de docker-compose ejecutaremos tambien desde el terminal:

```bash	
cd /volume1/docker/gitlab/
sudo docker-compose down
```
Este comando descargar� los contenedores y terminar� la ejecuci�n de gitlab (Los datos no se pierden).

2 Una vez levantados los contenedores, ejecutaremos la restauraci�n de la copia de seguridad. Para ello ejecutaremos desde el terminal en modo sudo:

	docker exec --user git -it <contenedorID> bundle exec rake gitlab:backup:restore RAILS_ENV=production

Donde contenedorID es el contenedor principal `synology_gitlab`, si hay mas de un backup mostrar� una lista con todos los backups disponibles que haya en la unidad, en orden cronol�gico inverso. Seleccionaremos el que queramos restaurar y continuamos.
Los backups se almacenan en estos directorios:
* dentro del contenedor: /home/git/data/backups
* dentro del host: /volume1/docker/gitlab/gitlab/backups
Recordemos que el volumen est� mapeado.. `/volume1/docker/gitlab/gitlab:/home/git/data`

3 Una vez ejecutado el restore debemos copiar los secretos. Para ello copiamos ambos ficheros (`gitlab.yml` y `secrets.yml`) que estan guardados en `/volume1/docker/gitlab/gitlab/backups/config/`.

	sudo docker cp /volume1/docker/gitlab/gitlab/backups/config/secrets.yml synology_gitlab:/home/git/gitlab/config
	sudo docker cp /volume1/docker/gitlab/gitlab/backups/config/gitlab.yml synology_gitlab:/home/git/gitlab/config

Y eso es todo. Probaremos a ver si funciona eject�ndolo en un navegador usando la direcci�n IP del host puerto 30000 (`192.168.0.12:30000` en el caso de argonte).


### Como conectarse desde ssh a proteo y argonte

a proteo: 

	ssh juan.nouche@192.168.0.12 -p 2367
a argonte:

	ssh juan.nouche@192.168.0.16 -p 2222

la opci�n `-p` indica el puerto

### C�digo fuente del docker-compose.yml

```yml
version: '2'

services:
  redisio:
    restart: always
    image: sameersbn/redis:4.0.9-1
    container_name: synology_gitlab_redis
    command:
    - --loglevel warning
  db:
    restart: always
    image: sameersbn/postgresql:12-20200524
    container_name: synology_gitlab_postgresql
    volumes:
    - /volume1/docker/gitlab/postgresql:/var/lib/postgresql
    environment:
    - DB_USER=gitlab_user
    - DB_PASS=gitlab_pass
    - DB_NAME=gitlab
    - DB_EXTENSION=pg_trgm,btree_gist

  gitlab:
    restart: always
    image: sameersbn/gitlab:13.12.2
    container_name: synology_gitlab
    depends_on:
    - redisio
    - db
    ports:
    - "30000:80"
    - "30001:22"
    volumes:
    - /volume1/docker/gitlab/gitlab:/home/git/data
    environment:
    - GITLAB_HOST=localhost
    - GITLAB_PORT=30000
    - GITLAB_SSH_PORT=30001
    - GITLAB_EMAIL=admin@antaruxa.com
    - REDIS_HOST=redisio
    - REDIS_PORT=6379
    - DB_ADAPTER=postgresql
    - DB_HOST=db
    - DB_PORT=5432
    - DB_USER=gitlab_user
    - DB_PASS=gitlab_pass
    - DB_NAME=gitlab
    - GITLAB_SECRETS_DB_KEY_BASE=v3_W4RIdV8E9ydkoXU65bqBz0yWvHzILDFp4J1na4kNSxP75yTk0PFty3pszFDuN
    - GITLAB_SECRETS_SECRET_KEY_BASE=uQZTyNV+ttn6RroT0uGsCoK+kVSYZplADhzMz87ht6sL0saHGWvZYM1javTYlME1
    - GITLAB_SECRETS_OTP_KEY_BASE=wILR0ehbJa4rDxU80g4PkYlVwoVDw691JRa5FEUys_PmP8_l9ka7lypNcv6L+5Xp
    - SMTP_ENABLED=true
    - SMTP_DOMAIN=ssl0.ovh.net
    - SMTP_HOST=ssl0.ovh.net
    - SMTP_PORT=465
    - SMTP_USER=admin@antaruxa.com
    - SMTP_PASS=Leonidas2005
    - SMTP_OPENSSL_VERIFY_MODE=peer
```

