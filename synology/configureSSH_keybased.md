# Configure Synology NAS SSH Key-based authentication

Please read this document: https://blog.aaronlenoir.com/2018/05/06/ssh-into-synology-nas-with-ssh-key/

Read this one too: https://robferguson.org/blog/2016/11/11/enable-ssh-scp-sftp-and-configure-a-static-ip-address-on-your-synology-nas/

ssh-copy-id -p 2035 showadm@ldap.antaruxa.com

rsync -av -e 'ssh -p 2035' /home/updatelinode/projects/carpeta_ejemplo juan.nouche@ldap.antaruxa.com:/home/juan.nouche/test/
rsync -av -e 'ssh -p 2035' /home/updatelinode/projects/carpeta_ejemplo showadm@ldap.antaruxa.com:/mnt/servers/fs01/lv-2/common/arpo2/vault/test/

rsync -av -e 'ssh -p 2035' /home/updatelinode/projects/carpeta_ejemplo juan.nouche@ldap.antaruxa.com:/mnt/servers/fs01/lv-2/common/arpo2/vault/test/

https://silica.io/using-ssh-key-authentification-on-a-synology-nas-for-remote-rsync-backups/

ojo no es synoservicectl --restart sshd sino systemctl restart sshd.service