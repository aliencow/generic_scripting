## Acesso a Windows con configuración propia.
https://www.tenforums.com/tutorials/173596-how-create-task-run-app-script-logon-windows-10-a.html
https://docs.microsoft.com/en-us/windows/win32/taskschd/logon-trigger-example--xml-

Se trata de crear un script en xml que ejecute una acción al realizar el usuario un login.
Este xml debe importarse después al programador de tareas


### Custom logon
https://redmondmag.com/articles/2016/02/09/logon-scripts-for-active-directory.aspx
https://docs.microsoft.com/en-us/windows-hardware/customize/enterprise/custom-logon

#### Directorio para login scripts
El directorio para los login scripts en el dominio ANTARUXA es el siguiente:
`\\ANTARUXA\sysvol\antaruxa.home.arpa\scripts`
o lo que viene a ser lo mismo en `\\argonte\sysvol\antaruxa.home.arpa\scripts`

Cualquier script de ejecución que guardemos en esta carpeta estará accesible para asignarlo como fichero de ejecución al hacer login.
El tipo de fichero que se ejecute puede ser:
* Un ejecutable.
* Un fichero .BAT.
* Un script Visual Basic .VBS o JScript .JS (ojo no es el javascript standard es el JScript de microsoft)

#### Pasos para generar y asignar el script de logon

* Crear el ejecutable o bat que deseemos y guardarlo en la carpeta para login scripts
* Asignar el script de login a un usuario concreto para ello:
  * Seleccionar el usuario:
    * Desde un administrador de domino en Windows: Entramos en `Panel de control\Sistema y seguridad\Herramientas administrativas\Usuarios y equipos de Active Directory` y seleccionamos dentro `antaruxa.home.arpa->Users` el usuario que queramos configurar.
    * Desde DSM de argonte: Abrimos `Synology Directory Server->Usuarios y ordenadores->Users` y seleccionamos el usuario a configurar.
  * Asignar el ejecutable de login al usuario: En las propiedades del usuario que hemos abierto, iremos a la solapa perfil o profile poner en `Script de inicio de sesión` el nombre del ejecutable (sin el path, solo el nombre y extensión).
