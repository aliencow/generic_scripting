## Control del sistema (todo requiere privilegios root)
con el comando `man hier` podemos ver la jerarquia de carpetas en el sistema actual
archivos especiales `/proc/cpuinfo` y `/proc/meminfo` contienen informacion sobre el sistema (cpu y memoria)
### systemctl - Control de procesos

* `systemctl`. Sirve para iniciar, terminar, recargar (reload), reiniciar (restart), terminar, listar etc. los procesos que ejecuta el sistema.
  * option `status`+` <nombreproceso>` muestra el stado del proceso.
  * option `start`+` <nombreproceso>` arranca el proceso.
  * option `stop`+` <nombreproceso>` detiene el proceso.
  * option `kill`+` <nombreproceso>` elimina el proceso
  * option `reload`+` <nombreproceso>` recarga el proceso (mientras esta funcionando ) no funciona en algunos casos no todos los procesos lo incorporan
  * option `restart`+` <nombreproceso>` reinicia el proceso (ejetuca `stop` + `start`)

### reboot

* `reboot`. Este comando reinicia el sistema. Ojo al hacerlo perderemos la conexión y tendremos que esperar a que reinicie para volver a conectar.

### crontab - Programar tareas

* `crontab`. Este comando permite programar tareas periódicamente guardando en un fichero de configuración.
  * option `-e`. Crea un fichero de texto que se puede abrir en nano donde introducimos los comandos y el pattern de periodicidad. Ver en https://crontab.guru la sintaxis de dicho pattern. El fichero se guarda por defecto en un lugar específico y debe accederse con usuario root.

### Crear y remover cuentas de usuario

* `adduser`+` <username>`. Sirve para añadir un usuario nuevo, crea un grupo, el usuario (con el mismo nombre <username>) y una carpeta `/home/<username>`. Va a pedir una contraseña y varios datos del usuario se rellenan y punto.
* `deluser`+` <username>`. Sirve para remover una cuenta de usuario. Remueve usuario y grupo.
  * option `--remove-home` Elimina además del usuario sus carpetas y spool de correo.
* `adduser <username> sudo`. Agrega un usario ya creado al grupo sudo, lo que le proporcionará privilegios de root.
* `sudo su`. Va a permitir desde el grupo sudo acceder como usuario su.

### Claves ssh (las instrucciones van en formato linux y sirve para windows wsl, mac o Ubuntu)

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
3. Una vez completado el proceso accedemos con el comando ssh al equipo remoto. Previo reseteo del service ssh `sudo systemctl restart ssh.service` o cambiando la configuracion en `/etc/ssh/sshd_config `
4. Repetiremos el proceso por cada equipo local que utilicemos para conectarnos.

### Permisos de ficheros

Si listamos con ll o ls -la nos aparecerán en el listado a la derecha de todo los permisos de los archivos tal que así.

    ...
    drwxr-xr-x 107 root root  4096 Dec  2 18:58 etc/
    drwxr-xr-x   3 root root  4096 Dec  2 18:58 home/
    lrwxrwxrwx   1 root root     7 Oct 22  2020 lib -> usr/lib/
    lrwxrwxrwx   1 root root     9 Oct 22  2020 lib32 -> usr/lib32/
    ...

Vemos que hay grupos de 10 caracteres con este formato o parecido.. `drwxrwxrwx `.La primera letra indica si es una carpeta (`d`) o un fichero (`-`) - Nota los links (`l`) y el resto de las letras van en grupos de 3 y hay 3 grupos. Estos grupos serían (empezando por la izquierda)

1. Permisos del propietario del archivo o carpeta.
2. Permisos para el grupo al que pertenezca el propietario del archivo o carpeta
3. Permisos para el resto de usuario.

el comando ll o ls -la nos muestra en la tercera y cuarta columna el propietario y el grupo al que pertenece el fichero/carpeta respectivamente.

Dentro de los permisos en cada caso tenemos tres tipos
* `r`- lectura. Con equivalente numérico `4`.
* `w`- escritura. Con equivalente numérico `2`.
* 'x'- ejecución. Con equivalente numérico `1`.
* '-'- nulo. Sin pemiso. Con equivalente numérico `0`

Veamos como funciona con un ejemplo:

Queremos que en determinado fichero
El usuario tenga todos los permisos       en letra `rwx` en número `4 + 2 + 1 = 7`
El grupo solo lectura y ejecución         en letra `r-x` en número `4 + 0 + 1 = 5`
El resto ningun permiso                   en letra `---` en número `0 + 0 + 0 = 0`
Es decir tendría en letra `rwxr-x---` y en numero `750`

Para asignar en comandos se usan tres letras `u` para usuario `g` para grupo y `o` para otros:
ejemplos

    mkdir -m u=rwx,g=rx,o= <dirname>
    mkdir -m 750 <dirname>

Creaarían ambos un folder con los permisos especificados.

* `chmod`. Cambia los permisos de ficheros o directorios. La sintaxis es `chmod <permisos> <fichero/carpeta>` donde permiso puede ser octal (en número) o modo (letra). Ejemplo: `chmod 750 <filename>` o `chmod u=rwx,g=rx,g= <filename>`
  * option `-R`. Aplica los cambios de modo recursivo
  * option `-v`. Verbose
  * option `-c`. Muestra cambios realizados

* `chown`. Change owner. Sirve para modificar los permisos de un archivo carpeta o archivo. La sintaxis es `chown <propietario>:<grupo> <ficheros/carpetas>`. Ejemplo `chown juan:juan micarpeta`. Opciones de usuario grupo pueden ser: <usuario>, <ususario>:<grupo>, <usuario>.<grupo>, .<grupo> o :<grupo>. Solo lo puede ejecutar un usuario root.
  * option `-R`. Recursivo
  * option `-v`. Verbose
  * option `-c`. Muestra los cambios realizados
* `umask`. Muestra o modifica la máscara utilizada cuando creamos ficheros o directorios. Cada usuario tiene una máscara para creación de ficheros. Solo `umask` muestra la máscara actual y con `umask <mascara>` cambia a la especificada. La máscara son 4 dígitos tomamos los ultimos 3 y de ellos el primero esta asociado a usuario el segundo a grupo y el tercero a otros. Esos tres dígitos se restan de 666 (máximos permisos) para ficheros y de 777 (maximos permisos) para carpetas y nos darán los permisos. Ej. si la umask es 022 los permisos para ficheros son 666-022 = 644 y para carpetas 777-022 = 755. Se aplica a los ficheros creados después de ejecutar umask.
