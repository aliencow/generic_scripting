## comandos synology
https://forum.synology.com/enu/viewtopic.php?t=126516#p464447


## configure a raspberrypi with openmediavault
https://www.google.com/search?q=raspberry+pi+as+nas+openmediavault&oq=raspberry+pi+as+nas+openmediavault&aqs=chrome..69i57.34991j0j9&sourceid=chrome&ie=UTF-8#kpvalbx=_swtTXfHED62CjLsPs6KjqAM17


## Info sobre redirección
http://mywiki.wooledge.org/BashGuide/InputAndOutput?#Redirection
https://www.gnu.org/software/bash/manual/html_node/Redirections.html


## Como poner el Prompt de terminal en líneas multipes

Edit the file .bashrc with editor (VI, nano etc.).

```bash
sudo nano ~/.bashrc
```
Then lockup for the following line

```bash
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```
Add the `\n` (new line) special character just before the `\$` at the end of the line. You should have a line looks like :

```bash
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n\$ 
```
That's all.