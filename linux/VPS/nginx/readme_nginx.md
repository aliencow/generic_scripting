## Como configurar nginx en VPS

En este fichero se anota todo lo necesario para configurar el servidor web
en linode (nginx)



### Como instalar y configurar nginx en VPS linode

Dentro de este tutorial hay una explicación sobre como instalar nginx:

https://www.linode.com/docs/guides/set-up-web-server-host-website/


Este es mi fichero de configuración nginx para el dominio nouche.me

    #Este fichero se ubica en /etc/nginx/conf.d/nouche.me.conf

    server {
        listen         80;
        listen         [::]:80;
        server_name    nouche.me  www.nouche.me;
        root           /var/www/nouche.me;
        index          index.html;

        gzip             on;
        gzip_comp_level  3;
        gzip_types       text/plain text/css application/javascript image/*;
    }


Una vez instalado nginx ya queda listo para funcionar. Instala un firewall automáticamente.

comprobar status nginx: `sudo nginx -t`
recargar el servicio `sudo systemctl reload nginx.service`


### Robots.txt para evitar que nos accedan los crawlers.

Configurar robots.txt para que no accedan crawlers
https://moz.com/learn/seo/robotstxt

Este es el robots.txt de `/var/www/nouche.me`

    User-agent: *
    Disallow: /


###K Configuracion nginx
Usuario nginx: `user www-data;`
recargar nginx: `sudo systemctl reload nginx.service`
carpeta instalacion: `/etc/nginx`
carpeta sitios disponibles: `/etc/nginx/modules-available`
carpeta sitios activos:`/etc/nginx/modules-enabled`
Los enabled son simplemente enlaces directos (links con `ln`) a algunos de los archivos de configuración existentes en available.



[Consulta formato Mark Down](https://www.markdownguide.org/cheat-sheet/).
