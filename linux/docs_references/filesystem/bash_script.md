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
