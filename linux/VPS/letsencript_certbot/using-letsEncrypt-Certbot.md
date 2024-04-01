## COMO USAR LET´S ENCRYPT and Certbot

### Let´s Encrypt
Getting Started Let´s Encrypt
https://letsencrypt.org/getting-started/

Que es let´s encrypt. Una entidad certificadora gratuita.
Para poder usar sitos https (secure) Se necesita que nuestra web disponga de un certificado seguro emitido por una entidad certificadora. Es parecido al sistema de llaves SSH

Permite obtener los certificados y sobre todo automatizar la obtención de estos.

### Certbot
Certbot es una herramienta open source para automatizar el uso de Let´s Encrypt sobre VPS que permitan HTTPS.
Instala un cron job que verifica cada cierto tiempo la expiración del certificado Let´s Encript y cuando lo detecta hace la actualización automática.

#### Instalacion de Certbot
En la página de certbot https://certbot.eff.org/instructions seleccionamos las instrucciones de instalación en nuestro caso par nginx y sistema Ubuntu 20
Necesitaremos lo primero que esté instalado el gestor de paquetes snap. En Ubuntu 20 ya viene preinstalado así que o actualizaremos a la última version.

    sudo snap install core; sudo snap refresh core

A continuación debemos eliminar cualquier instalacion previa de certbot hecha con apt-get

    sudo apt-get remove certbot

y se instala certbot con snap:

    sudo snap install --classic certbot

Creamos un link simbolico para que el sitema encuentre certbot facilmente

    sudo ln -s /snap/bin/certbot /usr/bin/certbot

#### Configurando Certbot y obtener certificados

Lo primero vamos a hacer tuq certbot obtenga los certificados como nos interesan. Para ello incluiremos en el comando las opciones:
* `--nginx`. Indicamos que tome los dominios a certificar de nuestra configuración de nginx.
* `--hsts`. Indicamos que queremos que por defecto redirija sempre la la version https (segura) de nuestros dominios.
* `--staple-ocsp`. Genera un certificado junto con el certificado de la autoridad aseguradora. Va compbinada con la opcion siguiente (`--must-staple`) no puede ir sola
* `--must-staple`. Obliga a que el certificado de la autoridad aseguradora se chequee siempre (por seguridad). Va combinada con la opcion anterior (`--staple-ocsp`) no puede ir sola.
* `-d`. Dominio o lista de dominios (separados por espacios) que queremos certificar. Ejemplo `-d myname.me -d www.myname.me -d myname.net -d www.myname.net etc`

el comando quedaría así:

    # Aunque se podría hacer en una sola vez:
    sudo certbot --nginx --hsts --staple-ocsp --must-staple -d myname.me -d www.myname.me -d myname.net -d www.myname.net -d myname.app -d www.myname.app

    # Es preferible por claridad hacer un comando por cada dominio.
    sudo certbot --nginx --hsts --staple-ocsp --must-staple -d myname.me -d www.myname.me
    sudo certbot --nginx --hsts --staple-ocsp --must-staple -d myname.net -d www.myname.net
    sudo certbot --nginx --hsts --staple-ocsp --must-staple -d myname.app -d www.myname.app

A partir de aqui ya podemos acceder con https a nuestros sitios.

#### Como funciona CertBot
Certbot genera una serie de cron jobs para mantenimiento de los certificados.
Para el acceso el comando principal es `certbot` poniendo en el cli `certbot --help` veremos las opciones que tiene.
Esta pensado para ejecutarse como sudo

Con este comando comprobamos los certificados que están instalados:

    sudo certbot certificates

    # esta seria la salida

    Certificate Name: myname.app
      Serial Number: 3752b586ed21878048294439cb751b5ef3f
      Key Type: RSA
      Domains: myname.app www.myname.app
      Expiry Date: 2022-06-10 18:08:39+00:00 (VALID: 89 days)
      Certificate Path: /etc/letsencrypt/live/myname.app/fullchain.pem
      Private Key Path: /etc/letsencrypt/live/myname.app/privkey.pem

Podemos ver el timer que tiene programado con. Podríamos hacerlo nosotros pero lo hace certbot cuando lo instala snap .

    # Comprobar que listando todos los timers
    sudo systemctl list-timers
    # está instalado este
    snap.certbot.renew.service
