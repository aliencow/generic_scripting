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

### WSL2 supports CIFS (SMB) protocol. You may need to specify your network server version when mounting. E.g. on Ubuntu 20.04:
https://newbedev.com/how-to-access-mounted-network-drive-on-windows-linux-subsystem

`$ sudo apt install cifs-utils
$ sudo mount -t cifs -o user=joe,pass=shmo,vers=1.0 //server/share /mnt/share`