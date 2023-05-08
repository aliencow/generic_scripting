## Montar unidades en wsl
https://dev.to/rpalo/mounting-network-drives-into-windows-subsystem-linux-3ef7

Microsoft uses a new type of file system called DrvFs behind the scenes to allow the Linux subsystem to talk to native Windows directories. So you end up mounting a network drive just like you would mount any other media normally.

Let's say you've got a server on your network usually accessible as \\stroopwafel. To mount it into your WSL, you can do the following (I'm using Ubuntu, but it should be similar for the other distros):

  `sudo mkdir /mnt/stroopwafel`
  `sudo mount -t drvfs '\\stroopwafel' /mnt/stroopwafel`

Note: I used single quotes to avoid awkwardness around the backslashes in the network drive name.

If you have mapped the network drive to a drive letter on your Windows system already--let's say \\stroopwafel is mapped to S:\--or if you've just got a removable drive that isn't mounted yet but has a letter on your Windows system, the syntax changes a little:

`sudo mkdir /mnt/stroopwafel`
`sudo mount -t drvfs S: /mnt/stroopwafel`

If you ever want to unmount it:

`sudo umount /mnt/stroopwafel`


Si la unidad muntada está busy y queremos desmontar.There is a way to detach a busy device immediately - even if it is busy and cannot be unmounted forcefully. You may cleanup all later:

umount -l /PATH/OF/BUSY-DEVICE
umount -f /PATH/OF/BUSY-NFS (NETWORK-FILE-SYSTEM)

### WSL2 supports CIFS (SMB) protocol. You may need to specify your network server version when mounting. E.g. on Ubuntu 20.04:
https://newbedev.com/how-to-access-mounted-network-drive-on-windows-linux-subsystem

```bash
$ sudo apt install cifs-utils
$ sudo mount -t cifs -o user=joe,pass=shmo,vers=1.0 //server/share /mnt/share
```

### Montar unidades de USB
https://www.scivision.dev/mount-usb-drives-windows-subsystem-for-linux/

```bash
mkdir /mnt/f

mount -t drvfs f: /mnt/f

Para unidades de red
mkdir /mnt/share

mount -t drvfs '\\server\share' /mnt/share
```

### Montar permanentemente unidades de red
https://askubuntu.com/questions/1119456/how-to-create-a-persistent-mounting-point-in-ubuntu-app-on-windows-10

* 1. Asegurarse de que se ha creado un directorio en mount

  mkdir /mnt/argontepipe

* 2. editar `/etc/fstab` desde sudo `sudo nano fstab` añadiendo al fichero la siguiente línea:

    \\argonte\pipeline /mnt/argontepipe drvfs defaults 0 0

* 3. Resetear el servicio de linux desde PowerShell como administrador:

    Get-Service LxssManager | Restart-Service


### Unir puntos de montaje en uno solo con https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/

* 1. montaje manual de las rutas

sudo mount -t drvfs '\\proteo\3dp\fs01\lv-2' /mnt/3dp-pr02
sudo mount -t drvfs '\\proteo\3dp\fs01\lv-3' /mnt/3dp-pr03
sudo mount -t drvfs '\\proteo\3dp\fs02\lv-1' /mnt/3dp-pr01
sudo mount -t drvfs '\\proteo\3dp\pipe\techlib\' /mnt/3dp-pipe

* 2. con la utilidad mhddfs se unen los puntos de montaje en uno solo. Ojo importante -o allow_other para que pueda acceder todo el mundo
sudo mhddfs /mnt/3dp-pr01,/mnt/3dp-pr02,/mnt/3dp-pr03,/mnt/3dp-pipe /srv/projects -o allow_other

* 3. montaje en fstab: No se sabe si funciona bien
\\proteo\3dp\fs01\lv-2 /mnt/3dp-pr02 defaults 0 0
\\proteo\3dp\fs01\lv-3 /mnt/3dp-pr03 defaults 0 0
\\proteo\3dp\fs02\lv-1 /mnt/3dp-pr01 defaults 0 0
\\proteo\3dp\pipe\techlib\ /mnt/3dp-pipe defaults 0 0

* 4. mhddfs en fstab: No se sabe si funciona bien
mhddfs#/mnt/3dp-pr01,/mnt/3dp-pr02,/mnt/3dp-pr03,/mnt/3dp-pipe /srv/projects fuse defaults,allow_other 0 0


192.168.0.16:/3dp/fs01/lv-2  /mnt/3dp-pr02  nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0