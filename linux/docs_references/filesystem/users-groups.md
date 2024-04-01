## Administrar usuarios y grupos en linux.

Primero hay que crear un fichero con la estenxión .sh
Va a ser un fichero de texto que luego va a ser interpretado como un fichero batch.

Normalmente los grupos se almacenan en el fichero /etc/groups

### Listar los grupos que hay
Si queremos un listado de los grupos que hay usaremos el comando `groups`

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
