## Resumen del pipe de linux y loa alias de comandos.
Pipe standard streams
0. Standard Input STDIN
1. Standard Output STDOUT
2. Error Output STDERR

### Redirigir entradas o salidas
Para redirigir la entrada por ejemplo de un fichero se utiliza el simbolo '<' precedido por el número.
Por ejemplo si queremos que la entrada del comando cat sea un fichero podremos hacerlo así:

	cat 0< rutadelfichero


Para redirigir la salida de un comando se utiliza el simbolo '>' precedido del número de stream.
Por ejemplo para redirigir la salida de un comando a un fichero:

	echo hola mundo 1> fichero.txt

y se volcaría la salida hola mundo en fichero.txt (comprobar con cat)
si quisieramos volcar la salida de errores a un fichero por ejemplo haríamos:

	echo hola mundo 2> errores.txt

con lo que errores txt guardaría los errores generados por el comando.
En los dos casos anteriores cada ejecución sobreescribe los ficheros. Si queremos utilizar el mismo fichero siempre y que el stream vaya añadiendose al final debemos usar el simbolo '>' repetido.
Por ejemplo:

	echo hola mundo >> fichero.txt (stream 1 por defecto)

en cada ejecución añadiría la salida a lo ya grabado en fichero.txt


### Comando pipe ('|')

Pipe. Se trata de que el standar output de un comando se interprete como standard input del comando siguiente.
Para ello se utiliza el simbolo '|' también llamado símbolo pipe.
Ejemplo:

	date | cut --delimiter=" " fields=1

date por si solo produce esta salida:

	Sat Oct 23 19:57:43 CEST 2021

Utilizando el pipe esta salida se usa como entrada de cut:

	date | cut --delimiter=" " --fields=1

Obteniendo esta salida:

	Sat

Es de recalcar que el comando pipe utiliza la salida estándar (stream 1) para pasársela al sigueinte comando por lo que si redirigimos la salida de uno de los comandos se cortará el pipe. Ejemplo:

date > hoy.txt | cut --delimiter=" " --fields=1

al redirigir el standar output al fichero hoy.txt en el comando date no llegará a ejecutarse el comando cut.

### Comando tee la bifurcación del standard Output

El comando tee funciona como una T en una cañeria

	command1 output _______tee________ input command2
	                       |
	                 output to file				

Es decir permite redirigir la salida sin interrumpir el streams
Ejemplo:

	date | tee hoy.txt | cut --delimiter=" " --fields=1

Permite obtener la salida de date en el fichero hoy.txt sin interrumpir el stream

### Usando salida como argumentos: xargs

Hay determinados comandos que no aceptan standard input por lo que no podemos usar el pipping, por ejemplo echo:

	date | echo

No producirá ninguna salida. Pare estos casos está el comando xargs. Es decir si un comando no acepta STDIN y queremos incluirlo en el pipe utlizaremos xargs. Ejemplo:

	date | xargs echo

producirá la salida:

	Sun Oct 24 11:17:32 CEST 2021

es decir date pasa la salida a echo mediante pipe.

### Aliases en el pipe

Supongamos que tenemos un pipe muy largo de comandos como este:

	date | tee ~/fulldate.txt | cut --delimiter=\  --filters=1 | tee ~/today.txt | xargs echo hello

Y que queremos utilizarlo varias veces sin volver a teclar todo. Para eso son los alias. Son como etiquetas que identifican comandos largos.

Por eejmplo el comando anterior podemos definirlo con la etiqueta getdates o algo así.
Para poder crear un alias debemos crear en `$HOME` (si no existiese ya) un fichero denominado `.bash_aliases`.  El fiheo se eita y se añade esta línea:

	alias getdates='date | tee ~/fulldate.txt | cut --delimiter=\  --filters=1 | tee ~/today.txt | xargs echo hello'

es decir:
1. literal `alias`
2. nombre del comando (`getdates` en este caso)
3. signo igual (`=`)
4. el contenido del comando o pipe entre comillas simples(`''`) o dobles (`""`).

Una vez guardado este fichero y OJO IMPORTANTE: reiniciado el equipo o el terminal ya podremos usar directamente el comando:

	getdates

los aliases se pueden integrar en el pipping y con el resultado hacer un nuevo alias, por lo que se puede prever su potencia. por ejemplo:

	alias1 | tee mifichero | alias2 | alias3 | xargs echo
