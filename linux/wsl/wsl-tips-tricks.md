
## Windows WSL tips and tricks

### Como saber en que carpeta física de windows esta el $HOME  de wsl

```bash
# Nos ubicamos en home (u otra carpeta)
cd ~
# Ejecutamos el explorador de archivos desde alli sobre el dir actual (`.`)
explorer.exe .
# Se abrirá un explorador de archivos en la ruta física.
```

### Compactar el wsl
https://terminaldelinux.com/terminal/wsl/liberar-espacio-disco-wsl/

Copiar una variable de entorno con el mismo nombre y contenido que la de windows

    export CURRENT_PROJECT=$(cmd.exe /c echo %CURRENT_PROJECT%)

Eliminar una variable de entorno en linux (en este caso wsl)

    unset CURRENT_PROJECT



### Acceso a C: desde command line linux:

cd /mnt/c para C:
cd /mnt/c/Users/juan.nouche/Desktop para escritorio
cd /mnt/d para D:

Create and modify the new WSL configuration file: (docker)

sudo nano /etc/wsl.conf

#### Now make it look like this and save the file when you're done:
``` bash
[automount]
root=/                  #<<<<<<<< importante SIN ESPACIOS (tal como esta).
options = "metadata"
```


We need to set root=/ because this will make your drives mounted at /c or /e instead of /mnt/c or /mnt/e.
Aplicando la configuración anterior las unidades quedaran en /c o /d en lugar de /mnt/c o /mnt/d

https://superuser.com/questions/1780345/why-wsl-mounts-at-mnt-c-and-not-c



### INVOCAR COMANDOS WSL DESDE LA VENTANA DE COMANDOS
https://devblogs.microsoft.com/commandline/a-guide-to-invoking-wsl/

Se escribe en cmd `wsl` seguido del comando o comandos que se quieran ejecutar
Si en la misma linea queremos ejecutar varios comandos se separan por `;`
ejemplo:
```
wsl cd /mnt/argonteweb/enchiridion/data; git push; git pull
```

### Resetear el servicio de linux desde PowerShell como administrador:
```
Get-Service LxssManager | Restart-Service
```

### Trabajar con ventanas en wsl y ejecutar pyside

Es necesario instalar VcXsrv server. https://sourceforge.net/projects/vcxsrv/ para servir xwindows.
Tutorial para ejecutar gui apps en wsl  https://techcommunity.microsoft.com/t5/modern-work-app-consult-blog/running-wsl-gui-apps-on-windows-10/ba-p/1493242
Tutorial para trabajar con Pyside desde wsl https://www.appsloveworld.com/python/1235/wsl2-and-pyside6


1. X Server https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242

    1. Install https://sourceforge.net/projects/vcxsrv/

    2. ```export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0" ``` 
    3. Run `xev` to test image

    4. Include the command ii at the end of the `/etc/bash.bashrc` file:

2. ```sudo apt install pyside2-tools libopengl-dev```

3. Run python3 xxx.py it worked but still has some problem. output:

```bash
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-dev'
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
```



