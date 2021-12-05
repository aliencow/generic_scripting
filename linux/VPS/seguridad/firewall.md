## Firewalls
Un firewall sirve para evitar accesos no deseados. Una barrera que impide que se accedan desde sitios que no nos interesen.
## UFW (uncomplicated fire wall)
Antes de activarlo comprobar si nuestra conexión esta deshabilitada en en firewall

usando `sudo ufw alloy "OpenSSH"` habilitamos el accesos mediante ssh exclusivamente.

### FAIL2BAN
Permite bloquear accesos repetitivos o incorrectos. Para instalarlo `sudo apt install fail2ban`
Configurarlo:

En /etc/fail2ban copiamos con sudo jail.conf a jail.local (la configuración local tiene prioridad)
Y en ese fichero dese sudo cambiamos los retrys, tiempo de bloqueo etc.
comprobar status `sudo fail2ban-client status`
Reiniciar `sudo systemctl restart fail2ban.service`
Si nos quedamos bloqueados por fail2ban, primero acceder al sistema desde el panel de control de nuestro proveedor de VPS (linode) y una vez dentro teclear
`sudo fail2ban-client set sshd unbanip 62.83.166.78` donde la ip que introducimos es la de nuestro equipo local.
