## Actualizacion de versiones gitlab

### UPGRADE

Lo primero hacer un backup de la version actual que esté funcionando correctamente y de los ficheros secrets y gitlab (.yml) conforme a lo que se explica en el tutorial de como hacer el backup y restore.

Aqui hay un tutorial de actualizacion
https://danielbkr.net/gitlab-upgrade/


Antes de actualizar la version de gitlab debemos actualizar en docker-compose.yml el redis(si hay que hacerlo) y la base de datos(si hay que hacerlo) y comprobar que funcionen los nuevos contenedores con la versión actual

Luego hay que ir haciendo una actualización progresiva cambiando la version de la imagen de gitlab en docker-compose.yml e ir probando.
Si no funcionase algo hay que hacer el downgrade.

IMPORTANTE - En cada actualizacion de version debemos copiar los ficheros de secrets al contenedor de docker una vez hecho el docker-compose up se copian dentro del contenedor con este comando:

    sudo docker cp /volume1/docker/gitlab/gitlab/backups/config/secrets.yml synology_gitlab:/home/git/gitlab/config
    sudo docker cp /volume1/docker/gitlab/gitlab/backups/config/gitlab.yml synology_gitlab:/home/git/gitlab/config


#### Path de upgrade

Primero hay que actualizar a la versión menor mas alta de la versión actual ejemplo:
la version actual es 13.12.2 la version menor mas alta es la 13.12.4  entonces upgradearemos de 13.12.2 -> 13.12.4

Despues actualizaremos a la version menor 0 de la siguente versión, por ejemplo: de 13.12.4 -> 14.0.1.

Por el momento el path de actualización estaría así 13.12.2 -> 13.12.4 -> 14.0.1

En la versión 14 docker introduce un concepto llamado Batched Background Migrations que son procesos que tienen que finalizar antes de poder hacer el upgrade a la siguiente versión.
https://docs.gitlab.com/ee/update/index.html#batched-background-migrations

Instances running 14.0.0 - 14.0.4 should not upgrade directly to GitLab 14.2 or later, because of batched background migrations.
    1- Upgrade first to either:
        14.0.5 or a later 14.0.Z patch release.
        14.1.0 or a later 14.1.Z patch release.
    2- Batched background migrations need to finish before you update to a later version and may take longer than usual.
https://docs.gitlab.com/ee/update/index.html#1400

O sea que debido a ese issue debemos actualizar antes a la 14.0.5 para que ejecute el patch de background migrations.
ahora el path de actualización estaría así 13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5
es posible que funcione directamente 13.12.2 -> 13.12.4 -> 14.0.5

Tras instalar la version 14.0.5 debemos dejar el contenedor funcionando hasta que se terminen de actualizar las Background Migrations que puede tardar desde unas horas hasta días

Este es un buen momento para hacer una copia de seguridad por si tenemos que dar un paso atrás en la instalación no tener que volver al principio.
HECHA COPIA DE SEGURIDAD en la version 14.0.5

Pasado este punto actualizamos a la 14.3.0  

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0

Pasado este punto actualizamos a la 14.4.4

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4

Pasado este punto actualizamos a la  14.5.0

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4 -> 14.5.0

HECHA COPIA DE SEGURIDAD en la version 14.5.0

Pasado este punto actualizamos a la 14.6.0

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4 -> 14.5.0 -> 14.6.0

That´s work Vamos a probar la version 14.7.1

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4 -> 14.5.0 -> 14.6.0 -> 17.7.1

That´s work again vamos a la version final (por el momento) 14.8.0

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4 -> 14.5.0 -> 14.6.0 -> 17.7.1 -> 14.8.0

Finalmente actualizamos a la última versión: la 14.8.2

13.12.2 -> 13.12.4 -> 14.0.1 -> 14.0.5 -> 14.3.0 -> 14.4.4 -> 14.5.0 -> 14.6.0 -> 17.7.1 -> 14.8.0 -> 14.8.2

INSTALADO Y LISTO HASTA LA PRÓXIMA

Se eliminan todas las imágenes de docker inferiores a la 14.7.1



### DOWNGRADE
Es necesario a veces para recuperar las versiones anteriores si algo falla en la actualización.
Es tan sencillo como recuperar el docker-compose.yml de la version que queremos downgradear y ejecutarlo.
En algunos downgrades de un error de que no se puede downgradear porque gitlab guarda en /volume1/docker/gitlab/gitlab/tmp un fichero llamado VERSION que contiene la última versión que se instaló y el startup del gitlab en algunas versiones lo lee y da ese error.

Para corregirlo es muy sencillo se renombra o se borra el fichero VERSION y ya deja downgradear.

Ejecutamos el docker-compose.yml de la version a la que queramos downgradear y recuperamos el backup de esa versión conforme a las instrucciones del tutorial de backup y restore.
