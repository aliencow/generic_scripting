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
