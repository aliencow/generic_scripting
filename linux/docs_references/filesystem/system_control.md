### Control del sistema (todo requiere privilegios root)
## systemctl - Control de procesos

* `systemctl`. Sirve para iniciar, terminar, recargar (reload), reiniciar (restart), terminar, listar etc. los procesos que ejecuta el sistema.
  * option `status`+` <nombreproceso>` muestra el stado del proceso.
  * option `start`+` <nombreproceso>` arranca el proceso.
  * option `stop`+` <nombreproceso>` detiene el proceso.
  * option `kill`+` <nombreproceso>` elimina el proceso
  * option `reload`+` <nombreproceso>` recarga el proceso (mientras esta funcionando ) no funciona en algunos casos no todos los procesos lo incorporan
  * option `restart`+` <nombreproceso>` reinicia el proceso (ejetuca `stop` + `start`)

## reboot

* `reboot`. Este comando reinicia el sistema. Ojo al hacerlo perderemos la conexión y tendremos que esperar a que reinicie para volver a conectar.

## crontab - Programar tareas

* `crontab`. Este comando permite programar tareas periódicamente guardando en un fichero de configuración.
  * option `-e`. Crea un fichero de texto que se puede abrir en nano donde introducimos los comandos y el pattern de periodicidad. Ver en https://crontab.guru la sintaxis de dicho pattern. El fichero se guarda por defecto en un lugar específico y debe accederse con usuario root.

## Crear y remover cuentas de usuario

* `adduser`+` <username>`. Sirve para añadir un usuario nuevo, crea un grupo, el usuario (con el mismo nombre <username>) y una carpeta `/home/<username>`. Va a pedir una contraseña y varios datos del usuario se rellenan y punto.
* `deluser`+` <username>`. Sirve para remover una cuenta de usuario. Remueve usuario y grupo.
  * option `--remove-home` Elimina además del usuario sus carpetas y spool de correo.
* `adduser <username> sudo`. Agrega un usario ya creado al grupo sudo, lo que le proporcionará privilegios de root.

## Claves ssh (las instrucciones van en formato linux y sirve para windows wsl, mac o Ubuntu)

Es un sistema de claves seguras que permite acceder a equipos remotos de modo muy fácil. El sistema consiste en dos claves:

* Private key. Es una clave que UNICAMENTE contendrá el equipo que demanda el acceso. no tiene extensión y se guarda en la carpeta `.ssh` del usario de que se trate.
* Public key. Es la clave pública que se subirá al equipo de destino y se guardará como una línea en el fichero `authorized_keys` dentro de la carpeta `.ssh` del usuario destinatario. Tiene la extensión .pub

Se accede al sistema de destino mediante el comando `ssh <username>@<remote IP>` lo que nos garantiza una conexión segura ya que se contrastarán las claves publica y privada codificadas mediante encriptación. Una vez verificado el usuario la consola accederá al
sistema remoto.

Necesitaremos una clave (privada y pública) para cada dispositivo desde el que queramos conectar.

* `ssh-keygen`. Crea (por defecto dentro de la carpeta `.ssh`) un par de ficheros de clave codificados (Private key y Public key)
  * option `-b`. Permite indicar el numero de bits para la encriptación por defecto 2048 es preferible ponerle 4096 para evitar la desencriptación (aunque con 2048 es muy dificil).
  * option `-f`+` <filename>`. Permite indicar el nombre de fichero para la clave que queremos, util cuando necesitemos varias. Por defecto el comando asigna el nombre 'id_rsa'. Recordar que se crean dos files el id_rsa y el id_rsa.pub el primero es la clave privada (se queda en el equipo local) y el segundo la clave pública que tendremos que copiar al fichero `authorized_keys` del equipo remoto.

Es decir:
1. Generamos con ssh-keygen los dos ficheros de clave en el equipo local
2. En el equipo remoto copiamos la public key en una sola linea del fichero `~/.ssh/authorized_keys` haciendo copy paste y editando en nano por ejemplo.
3. Una vez completado el proceso accedemos con el comando ssh al equipo remoto.
4. Repetiremos el proceso por cada equipo local que utilicemos para conectarnos.
