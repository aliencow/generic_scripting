## Firewalls
Un firewall sirve para evitar accesos no deseados. Una barrera que impide que se accedan desde sitios que no nos interesen.
## UFW (uncomplicated fire wall)
Antes de activarlo comprobar si nuestra conexión esta deshabilitada en en firewall

usando `sudo ufw allow "OpenSSH"` habilitamos el accesos mediante ssh exclusivamente.

si usamos nginx hay que havilitar Nginx con `sudo ufw app list` lo buscamos en la lista de aplicaciones y se habilita para el firewall con `sudo ufw allow "Nginx Full"`
Hay un tutorial completo en este link: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu


### FAIL2BAN
Permite bloquear accesos repetitivos o incorrectos. Para instalarlo `sudo apt install fail2ban`
Configurarlo:

En /etc/fail2ban copiamos con sudo jail.conf a jail.local (la configuración local tiene prioridad)
Y en ese fichero dese sudo cambiamos los retrys, tiempo de bloqueo etc.
comprobar status `sudo fail2ban-client status`
Reiniciar `sudo systemctl restart fail2ban.service`
Si nos quedamos bloqueados por fail2ban, primero acceder al sistema desde el panel de control de nuestro proveedor de VPS (linode) y una vez dentro teclear
`sudo fail2ban-client set sshd unbanip 62.83.166.78` donde la ip que introducimos es la de nuestro equipo local.
