s## SCHEDULING IN CRON
Cron (cronus) es una utilidad que permite ejecutar ciertas tareas periódicamente programando el lanzamiento mediante un timer.
estos comportamientos se programan con el comando crontab
* `crontab -e`. Permite seleccionar el editor de texto. Esto abrirá un fichero de texto en el que podemos incluir una fila por cada comando que queramos poner en crontab. Cada fila va a contener 6 columnas, las 5 primeras de ellas incluyen información y la última lleva el comando que queremos ejecutar.
Estas Columnas tienen este siguiente patrón:

`m h dom mon dow command`

Ver en https://crontab.guru la sintaxis de dicho pattern. los valores pueden ser wildcards:

*	any value
,	value list separator
-	range of values
/	step values

La primera columna va a contener el minuto en el que queremos la ejecución.
La segunda columna contiene la hora del día
La tercera columna contiene el día del mes
La cuarta columna contiene el mes
La quinta columna contiene el día de la semana
Por último como hemos dicho antes en la sexta columna va el comando
