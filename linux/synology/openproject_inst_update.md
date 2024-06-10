## Open project instalacion backup actualizacion
Instalacion
https://github.com/opf/openproject-deploy/tree/stable/12/compose

Control de backups y updates
https://github.com/opf/openproject-deploy/tree/stable/12/compose/control


Ejecutar el docker composer con puertos o tag personalizados
If you want to specify a different port, you can do so with:

    PORT=4000 docker-compose up -d

If you want to specify a custom tag for the OpenProject docker image, you can do so with:

    TAG=my-docker-tag docker-compose up -d    

Para arrancar con nombre de proyecto propio

    docker-compose --project-name OpenProject up  -d
