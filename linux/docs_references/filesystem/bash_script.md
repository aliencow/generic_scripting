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
