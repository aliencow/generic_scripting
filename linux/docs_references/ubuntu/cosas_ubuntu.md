## Algunas particularidades de Ubuntu
Consultar la versión de ubuntu
`lsb_release -a`

Tutorial como instalar ubuntu en virtual box:
https://osl.ugr.es/2020/09/29/como-instalar-ubuntu-en-virtual-box/

Atajos teclado UBUNTU
- `Ctrl+Alt+t` Open terminal window .
- `Ctrl+d` Close terminal.
- `Ctrl+l` Clear terminal.



[Consulta formato Mark Down](https://www.markdownguide.org/cheat-sheet/).

curl no viene por defecto en Ubuntu
hay que instalarlo:

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt-get install curl `

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

## Modificando el prompt de linux. Información mas detallada de modificacion del prompt utilizando la variable PS1


Codigo para incluir en .bashrc:

```bash 
#\u - user name
#\h - short hostname
#\W - current working dir
#\w - complete path working dir
#\? - exit status of the command

# FORMATED COLORS 
LIGHTBLUE="$(echo -e '\033[1;34m')"
LIGHTGREEN="$(echo -e '\033[1;32m')"
GREEN="$(echo -e '\033[0;32m')"
ORANGE="$(echo -e '\033[0;33m')"
WHITE="$(echo -e '\033[1;37m')"

# $'' is for using UTF-16 unicode characters. The unicode characters are coded with \u and four hex digits for example \u2143 = ⅃
# Remember to wrap format codes (everything not printed) between \[ and \] otherwise you could have pasting text prompt overriding


export PS1=$'\[${LIGHTBLUE}\]\u250C\u2500\u2500(\[${LIGHTGREEN}\]\\u\[${GREEN}\]@\[${LIGHTGREEN}\]\\h\[${LIGHTBLUE}\]) [\[${ORANGE}\]\\w\[${LIGHTBLUE}\]]\n\u2514\u2500\[${WHITE}\]$ '
```
