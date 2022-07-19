## Windows WSL tips and tricks

Como saber en que carpeta física de windows esta el $HOME  de wsl
```bash
# Nos ubicamos en home (u otra carpeta)
cd ~
# Ejecutamos el explorador de archivos desde alli sobre el dir actual (`.`)
explorer.exe .
# Se abrirá un explorador de archivos en la ruta física.
```

Compactar el wsl
https://terminaldelinux.com/terminal/wsl/liberar-espacio-disco-wsl/

Copiar una variable de entorno con el mismo nombre y contenido que la de windows

    export CURRENT_PROJECT=$(cmd.exe /c echo %CURRENT_PROJECT%)

Eliminar una variable de entorno en linux (en este caso wsl)

    unset CURRENT_PROJECT


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
