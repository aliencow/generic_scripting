## Windows10 tips-tricks

* Acceso a la carpeta de inicio
* `Windows+R` y tecleamos: `shell:common startup` para la carpeta de inicio común.
* `Windows+R` y tecleamos: `shell:startup` para la carpeta de inicio del usuario activo.

* Algunas teclas de interés:
  * `Windows+R`. Accedemos a ejecutar y tecleamos el programa que queremos
  * `Windows+L`. Bloquear (antiguo `Ctrl+Alt+Supr`).
  * `Windows+Break`(pausa). Acceso directo a configuración.

dir /s /b maya.exe to find an exe if we know the name

### Variables de entorno permanentes crear y borrar

Para crear. Ejemplo queremos crear PYENVROOT desde CMD. Ojo la crea en el entorno del usuario activo.
https://stackoverflow.com/questions/5898131/set-a-persistent-environment-variable-from-cmd-exe

    SETX PYENVROOT \\argonte\python

Para Borrar. Ejemplo queremos eliminar PYENVROOT desde CMD ojo la remueve desde el usuario activo.
https://stackoverflow.com/questions/13222724/command-line-to-remove-an-environment-variable-from-the-os-level-configuration

    SETX PYENVROOT "" & REG delete HKCU\Environment /F /V PYENVROOT

### Activar desactivar fast init en WINDOWS

desde ejecutar (Ventana + R) teclear
`powercfg.cpl`  
