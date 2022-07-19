# Desarrollando en remoto con VScode en Synology

### I. Segunda consulta

#### 1. Contenido consulta I

Conexión vía SSH para VS Code

VS Code se ha convertido en mi editor preferido para casi todo... y resulta que tiene algunas características útiles para editar archivos docker-compose.yml. Como estoy jugando con la ejecución de algunos contenedores Docker en mi Synology DS 920+, he estado trabajando en la configuración del acceso ssh al NAS.
Hasta ahora, puedo ssh en el NAS a través de MobaXterm (similar a PuTTY), tanto utilizando la contraseña y ahora usando ssh-claves. Puedo conectar VS Code a otros dispositivos a través de SSH, con claves, pero... No consigo que VS Code se conecte al NAS de Synology vía ssh, ni con contraseña ni con claves.
Me sale un error "No se pudo establecer la conexión con "192.168.1.19": El proceso intentó escribir en una tubería inexistente".
¿Alguien ha conseguido que esto funcione? He estado buscando el mensaje de error y encontrar algunos resultados, pero nada es realmente saltando a mí como una pistola de fumar hasta el momento.

#### 2. Respuesta consulta  II


El mensaje de error podría ser engañoso. Sin embargo, el servidor SFTP/SSH en Synology se comporta de una manera no estándar, y muchas herramientas de terceros tienen que implementar soluciones específicamente para las estaciones de disco Synology.
Puede que no merezca la pena intentar luchar contra los molinos de viento en este caso, y en su lugar yo montaría su recurso compartido SFTP con rclone mount, con caché, ocultando todas las travesuras SFTP de VSCode al presentar el recurso compartido como un disco local.
Tenga en cuenta que cuando especifique la ruta a las cosas en el synology a través de SFTP debe comenzar con la ruta absoluta: es decir, sftp://nas.local//share/file. Tenga en cuenta el // después de la URL. De lo contrario, se encontrará con todo tipo de problemas extraños cuando el archivo pueda leerse pero no guardarse, etc.
Sin embargo, si está en la LAN, yo simplemente utilizaría NFS o SMB.


### II. Segunda consulta

#### 1. Contenido consulta II

Hola a todos,

hasta ahora me he conectado a mi NAS a través de PuTTy. No hay ningún problema, todo funciona bien. Recientemente he pensado que quizás podría conectarme al NAS directamente a través de VSCode, lo que podría mejorar mi flujo de trabajo, pero parece que no puedo establecer una conexión.

He instalado el módulo SSH remoto, pero cuando intento conectarme al NAS obtengo

` The remote host may not meet VS Code Server's prerequisites for glibc and libstdc++ `



Me pregunto si alguno de vosotros ha conseguido hacer esto y -si es así- cómo


#### 2. Respuesta consulta  II


Pude hacerlo funcionar. Sigo utilizando el último DSM 6.x.
Uso los repos de SynoCommunity y allí instalé "IPKGui"
con eso agregué el glibc-locale.
Y edite sshd_config y cambie AllowTcpForwarding no a AllowTcpForwarding yes. Luego reinicié el servicio SSH desde el panel de control del NAS.
En mi caso no fue necesario nada más.
