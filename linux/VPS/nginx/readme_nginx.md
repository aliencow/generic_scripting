## Como configurar nginx en VPS

En este fichero se anota todo lo necesario para configurar el servidor web
en linode (nginx)



### Como instalar y configurar nginx en VPS linode

Dentro de este tutorial hay una explicación sobre como instalar nginx:

https://www.linode.com/docs/guides/set-up-web-server-host-website/


Este es mi fichero de configuración nginx para el dominio myname.me

    #Este fichero se ubica en /etc/nginx/conf.d/myname.me.conf

    server {
        listen         80;
        listen         [::]:80;
        server_name    myname.me  www.myname.me;
        root           /var/www/myname.me;
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

Este es el robots.txt de `/var/www/myname.me`

    User-agent: *
    Disallow: /


###K Configuracion nginx
Usuario nginx: `user www-data;`
recargar nginx: `sudo systemctl reload nginx.service`
carpeta instalacion: `/etc/nginx`
carpeta sitios disponibles: `/etc/nginx/modules-available`
carpeta sitios activos:`/etc/nginx/modules-enabled`
Los enabled son simplemente enlaces directos (links con `ln`) a algunos de los archivos de configuración existentes en available.


### Securizacion servidor en nginx
1- Impedir que accedan a nuestra versiòn linux
Abriremos la configuracion en nano `sudo nano /etc/nginx/nginx.conf`
activamos la linea de server token poniendolo a off `server token soff`
2- Uso de snippets para los sitios habilitados.
Sinppets de nginx permite utilizar la misma funcionalidad desde varios sitios.
Los snippets estan en carpeta `/etc/nginx/snippets/`
crearemos el snippet `security-headers.conf` para incrementar protección a todos los sitios que tenemos instalados. El contenido sera este

  ##
  # Security Setting
  ##

  # impedir la inclusion en un iframe desde fuera del site
  add_header X-Frame-Options SAMEORIGINS;

  # impedir el sniffing por tipo MIME
  add_header X-Content-Type-Options nosniff;

  # Evitar ataquess XSS (inyeccion de contenido)
  add_header X-XSS-Protection "1; mode=block";

  # Referrer policy,  only use full path on same origin
  add_header Referrer-Policy "strict-origin-when-cross-origin"

Se pueden consultar mediante ventana de incógnito mas opciones de seguridad para cabeceras en `securityheaders.com`

3- Habilitar compresión en gzip a nginx. No es de seguridad pero es importante para mejorar la transferencia de ficheros. Para ello tocamos la seccion GZIP SETTINGS en `/etc/nginx/nginx.conf` quedaría de esta forma:

  ##
  # Gzip Settings
  ##

  gzip on;

  gzip_vary on;
  # gzip_proxied any;
  gzip_comp_level 6;
  gzip_buffers 16 8k;
  gzip_http_version 1.1;
  gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xmlon/xml+rss text/javascript;

### Evitar ataques DoS y DDoS (ataque de denegación de servicio)
DoS peticiones de servicio recurrente y continuo para bloquear el servidor
DDoS igual pero el ataque se produce desde servidores distribuidos
No se puede evitar pero se puede mitigar.

Detectar si recibimos demasiadas peticiones desde el mismo servidor.
Creamos un snippet `snippets/dos-protection.conf`
con este contenido:
  ##
  # DoS and DDoS Protection Settings
  ##

  #Define limit connection zone called conn_limit_per_ip with memory size 15m based on the un$
  limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:15m;

  #Define limit request to 40/sec in zone called req_limit_per_ip memory size 15m based on IP
  limit_req_zone $binary_remote_addr zone=req_limit_per_ip:15m rate=40r/s;

  #Using the zone called conn_limit_per_ip with max 40 connections per IP
  limit_conn conn_limit_per_ip 40;

  #Using the zone req_limit_per_ip with an exceed queue of size 40 without delay for the 40 a$
  limit_req zone=req_limit_per_ip burst=40 nodelay;

  #Do not wait for the client body or headers more than 5s (avoid slowloris attack)
  client_body_timeout 5s;
  client_header_timeout 5s;
  send_timeout 5;

  #Establishing body and headers max size to avoid overloading the server I/O
  client_body_buffer_size 256k;
  client_header_buffer_size 2k;
  client_max_body_size 3m;
  large_client_header_buffers 2 2k;

Ojo comprobar los tamaños que necesitamos sobre todo de numero de peticiones y el tamaño máximo de tamaño de body según nuestras necesidades los modificaremos.

### Evitar que los sitios nginx sean secuestrados
Hacer que nadie pueda apuntar su dominio a nuestra dirección de servidor.
Haciendo que no se acepten redirecciones a otros dominios que nosotros no tenemos en propiedad.

Añadiendo un bloque server en el dominio que tenemos configurado por defecto en mi caso myname.me
(/etc/nginx/sites-available/myname.me)

    server {
            listen 80 default_server;
            listen [::]:80 default_server;

            server_name _;  #cualquier peticion externa que de cualquier servidor
            return 301 http://myname.me;  #la enviamos al sitio por defecto
            # return 301 http://www.myname.me; #opcionalmente puede enviarse con www
    }


[Consulta formato Mark Down](https://www.markdownguide.org/cheat-sheet/).
