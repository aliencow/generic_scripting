### Crear y remover cuentas de usuario

* `adduser`+` <username>`. Sirve para añadir un usuario nuevo, crea un grupo, el usuario (con el mismo nombre <username>) y una carpeta `/home/<username>`. Va a pedir una contraseña y varios datos del usuario se rellenan y punto.
* `deluser`+` <username>`. Sirve para remover una cuenta de usuario. Remueve usuario y grupo.
  * option `--remove-home` Elimina además del usuario sus carpetas y spool de correo.
* `adduser <username> sudo`. Agrega un usario ya creado al grupo sudo, lo que le proporcionará privilegios de root.
* `sudo su`. Accede directamente al usuario root por si hay que hacer alguna configuración.

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
1. Generamos con ssh-keygen los dos ficheros de clave en el equipo local. Crear el fichero de claves ssh:
```bash
#filename optional si no se pone genera un fichero por defecto id-rsa
ssh-keygen -b 4096 -f filename
# Create a new key with email and user name
ssh-keygen -b 4096 -t rsa -C My-Email -f filename
```
este fichero se ubica en linux `~/.ssh` y en Windows en `C:\Users\<username>\.ssh`
2. En el equipo remoto copiamos la public key en una sola linea del fichero `~/.ssh/authorized_keys` haciendo copy paste y editando en nano por ejemplo. O usando:
```bash
#Copy the key to a server - portnumber default 22 if you changed it put -p portnumber
ssh-copy-id -i ~/.ssh/filename -p portnumber user@host
ssh-copy-id -i ~/.ssh/filename user@host #nos pide la contraseña
#Test the new key
ssh -i ~/.ssh/mykey user@host
```
3. Una vez completado el proceso accedemos con el comando ssh al equipo remoto.
4. Repetiremos el proceso por cada equipo local que utilicemos para conectarnos.

### configuración de seguridad ssh
La configuración de ssh se encuentra en la carpetea `/etc/ssh/sshd_config` ojo sshd_config literal no confundir con ssh_config u otros del archivo.

Editanto con sudo nano:
Ponemos `PermitRootLogin no` para que no se pueda usar root.
Ponermos `PasswordAuthentication no` para que nadie puede hacer ingreso con password. Ojo asegurarse primero que podemos acceder mediante ssh antes de cambiar esta configuracion.
Ponemos `ChallengeResponseAuthentication no` por la misma razón.

Tras confirmar cambios recargamos el servicio con sytemctl: `sudo systemctl reload ssh.service`
y a partir de ese momento no se adminitán accesos como root ni con contraseña normal.
