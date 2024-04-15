## Como hacer scripts en linux
Primero hay que crear un fichero con la estenxión .sh
Va a ser un fichero de texto que luego va a ser interpretado como un fichero batch.

### Indicativo de que es un archivo bash y que interprete lo ejecutará

Hay unos caracteres especiales para especificar que una linea lleva un comand: `#!` Identifica que el tipo de fichero va a ser un bath y que se interpretara con el script que se indica.

    #!/bin/bash

Significa que el interprete va ser el interprete de comandos. Si pusiesemos en la primera linea por ejemplo `#!/bin/python/python3` indicaría que el interprete de comandos seria python3

Este indicativo debe ir en la primera línea y las demás líneas serán comandos. Un ejemplo

    #!/bin/bash
    mkdir ~/Escritorio/magic
    cd ~/Escritorio/magic
    touch file{1..100}
    ls -lh ~/Escritorio/magic > ~/Escritorio/magic.log

Guardamos este fichero como comando.sh
Para ejecutar el bash usaremos el propio comando bash ejemplo

    bash comando.sh

si queremos ejecutarlo como un comando sin llamar a bash debemos hacer lo siguiente:
* Copiarlo a una carpeta bin normalmente ~/bin (si no existiese la carpeta la creamos).
  * Si hemos creado la carpeta bin hay que añadirla al path del sistema para que luego se encuentre el comando. Esto se hace editando el fichero `$HOME/.bashrc` donde se configuran los recursos de bash. Se añade al final del comando esta línea:

      PATH="$PATH:$HOME/bin"

  * Si hemos añadido el path a .bashrc debemos ejecutar otra consola para que funcione

* renombramos el comando ejemplo

    mv ~/bin/comando.sh ~/bin/comando

* con el comando  chmod añadimos permisos de ejecución (+x)
* Voila!! ya podemos ejecutar desde linea de comandos.


### fichero .bashrc
fichero que se encuentra en la carpeta home del usuario y que se ejecuta cada vez que se inicie esta por ejemplo al arrancar una consola.

### SETTING ENVIRONMENT VARS
https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
https://linuxconfig.org/how-to-set-and-list-environment-variables-on-linux

Para ver las variables de entorno acivas se utiliza el comando de entorno `printenv` por defecto printenv muestra todas las variables que tiene el sistema. Tambien podemos usar el nombre de una  variable concreta para ver el contenido o filtrar la salida con grep.
```
printenv # lista todas las variables
printenv PATH # muestra el contenido de la variable PATH
printenv | grep TEST_VAR # muestra todas las lineas  de entorno que contengan TEST_VAR

```

### Establecer una variable de entorno temporal

A continuación se explica cómo crear una nueva variable de entorno en Linux. Tenga en cuenta que esta es una variable de entorno temporal y no sobrevivirá a un reinicio del sistema, al cierre de sesión del usuario o a un nuevo shell. Como ejemplo, crearemos una nueva variable llamada MY_SITE.

  * Utilice el siguiente comando para crear una nueva variable de shell. Esto sólo hará que la variable esté activa en su sesión actual, pero pronto haremos una variable de entorno.

    `MY_SITE='linuxconfig.org'`

   * A continuación, utilice el comando export para establecer la nueva variable como una variable de entorno.

    `$ export MY_SITE`

  * Alternativamente, podemos establecer la variable de entorno temporal utilizando un solo comando con esta sintaxis:

    `$ export MY_SITE="linuxconfig.org"`

### Configurar una variable de entorno permanente

Para configurar una nueva variable de entorno para que sea persistente, necesitaremos editar los archivos de configuración de Bash. Esto se puede hacer a través de tres archivos diferentes, dependiendo de cómo se planea acceder a la variable de entorno.

* `~/.bashrc` - Las variables almacenadas aquí residirán en el directorio de inicio del usuario y sólo son accesibles por ese usuario. Las variables se cargan cada vez que se abre un nuevo shell.
* `/etc/profile` - Las variables almacenadas aquí serán accesibles para todos los usuarios y se cargan cada vez que se abre un nuevo shell.
* `/etc/environment` - Las variables almacenadas aquí son accesibles para todo el sistema.

Añade una nueva variable a los archivos de configuración~/.bashrc o /etc/profile añadiendo una línea al final del mismo con esta sintaxis. Observe que precedemos cada nueva variable con export.
```
export MY_SITE='linuxconfig.org'
```

Después, puedes cargar las nuevas variables de entorno en la sesión actual con el siguiente comando.
```
$ source ~/.bashrc # user
# source /etc/profile # sudo
```

Si añade una variable de entorno al archivo /etc/environment, no necesita preceder la línea con "export".

MY_SITE='linuxconfig.org'

Utilizando los métodos anteriores, sus configuraciones de variables persistirán hasta que las elimine.

### Establecimiento de variables de entorno en el inicio de sesión

Ya hemos mencionado que muchos programas utilizan variables de entorno para decidir los detalles de su funcionamiento. No queremos tener que configurar variables importantes cada vez que iniciamos una nueva sesión del shell, y ya hemos visto cómo muchas variables ya están configuradas al iniciar la sesión, así que ¿cómo hacemos y definimos las variables automáticamente?

Esto es en realidad un problema más complejo de lo que parece inicialmente, debido a los numerosos archivos de configuración que el shell bash lee dependiendo de cómo se inicie.

### La diferencia entre las sesiones de shell con inicio de sesión, sin inicio de sesión, interactivas y no interactivas

El shell bash lee diferentes archivos de configuración dependiendo de cómo se inicie la sesión.

Una distinción entre las diferentes sesiones es si el shell se inicia como una sesión de inicio de sesión o no.

Un shell de inicio de sesión es una sesión de shell que comienza autenticando al usuario. Si está iniciando una sesión de terminal o a través de SSH y se autentifica, su sesión de shell se establecerá como una shell de inicio de sesión.

Si inicias una nueva sesión de shell desde tu sesión autenticada, como lo hicimos llamando al comando bash desde la terminal, se inicia una sesión de shell que no es de inicio de sesión. No se le pidieron sus detalles de autenticación cuando inició su shell hijo.

Otra distinción que se puede hacer es si una sesión de shell es interactiva, o no interactiva.

Una sesión de shell interactiva es una sesión de shell que está conectada a una terminal. Una sesión de shell no interactiva es aquella que no está unida a un terminal.

Así que cada sesión de shell se clasifica como de inicio de sesión o de no inicio de sesión e interactiva o no interactiva.

Una sesión normal que comienza con SSH suele ser una shell interactiva de inicio de sesión. Un script ejecutado desde la línea de comandos se ejecuta normalmente en un shell no interactivo, no de inicio de sesión. Una sesión de terminal puede ser cualquier combinación de estas dos propiedades.

El hecho de que una sesión de shell se clasifique como de inicio de sesión o de no inicio de sesión tiene implicaciones en los archivos que se leen para inicializar la sesión de shell.

Una sesión iniciada como sesión de inicio de sesión leerá primero los detalles de configuración del archivo /etc/profile. Luego buscará el primer archivo de configuración del shell de inicio de sesión en el directorio raíz del usuario para obtener los detalles de configuración específicos del usuario.

Lee el primer archivo que puede encontrar de ~/.bash_profile, ~/.bash_login y ~/.profile y no lee ningún otro archivo.

En cambio, una sesión definida como shell no interactiva leerá /etc/bash.bashrc y luego el archivo ~/.bashrc específico del usuario para construir su entorno.

Los shells no interactivos leen la variable de entorno llamada BASH_ENV y leen el archivo especificado para definir el nuevo entorno.


Funcionamiento de zenity para hacer msgboxes
https://linoxide.com/bash-shell-script-show-dialog-box/
