## Administrar usuarios y grupos en linux.

Primero hay que crear un fichero con la estenxión .sh
Va a ser un fichero de texto que luego va a ser interpretado como un fichero batch.

Normalmente los grupos se almacenan en el fichero /etc/groups

### Listar los grupos que hay
Si queremos un listado de los grupos que hay usaremos el comando `groups` o `id`

* `groups`. Lista los grupos que existen
  
* `id`. Muestra usuarios y grupos. Pero solamente para el usuario especificado. Sintaxis`id <options> <user>`
  * option `-g`. Imprime solo el grupo efectivo 
  * option `-G`. Imprime todos los ID de grupo
  * option `-n`. Imprime todos los nombres de grupo.
  * option `-u`. Imprime el id del usuario efectivo.

### Crear grupos
Si queremos crear grupos usaremos el comando `groupadd`.

Ejemplo: creamos un grupo llamado `demo`.

```bash
sudo groupadd demo
```
Si queremos que tenga un ID específico (GroupID-GID) usaremos el flag `--gid` o `-g`
```bash
sudo groupadd -g 1009 demo
```
Abortará si el ID 1009 está ocupado.

### Modificar grupos
Si queremos modificar grupos usaremos el comando `groupmod`

Ejemplo: modificamos el id del grupo `demo`, usaremos el flag `--gid` o `-g`

```bash
sudo groupmod -g 1011 demo
```
Abortará si 1011 está ocupado

Si queremos cambiar el nombre del grupo usaremos el flag `--new-name` o `-n`.
```bash
sudo groupmod -n <destino> <origen>
sudo groupmod -n test demo
# hemos cambiado el nombre de `demo` a `test`
```
### Delete a group

When a group is no longer needed, you delete it by using the groupdel command:

```bash
sudo groupdel demo
sudo groupdel -f demo #forzando la eliminaciòn
```

### Add and remove users from a group
Suppose you have existing users named user1 and user2, and you want to add them to the demo group. Use the usermod command with the --append --groups options (-a and -G for short):

```bash
sudo usermod --append --groups demo user1
```

```bash
sudo usermod -aG demo user2
```

Look in the /etc/group file or use the id command to confirm your changes:

```bash
id user1
uid=1005(user1) gid=1005(user1) groups=100(users),1009(demo)
```

To remove a specific user from a group, you can use the gpasswd command to modify group information:

```bash
sudo gpasswd --delete user1 demo
```
Alternatively, manually edit the /etc/group file and remove the user from any number of groups.




```bash
```
```bash
```
```bash
```
```bash
```
```bash
```



flags de groupadd 

```bash
  -f, --force                   exit successfully if the group already exists,
                                and cancel -g if the GID is already used
  -g, --gid GID                 use GID for the new group
  -h, --help                    display this help message and exit
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -o, --non-unique              allow to create groups with duplicate
                                (non-unique) GID
  -p, --password PASSWORD       use this encrypted password for the new group
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
      --extrausers              Use the extra users database
```
