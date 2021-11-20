## Carecteres especiales que usa linux

1. `\`   escape para caracteres especiales individuales
2. `*`   comodín multiples caracteres
3. `?`  comodín caracter simple
4. `[]`  especificacion de rangos
5. `""` y `''` escapes para strings (ambos)
6. `>`   redireccionar salida. `>>` Lo mismo pero con actualizacion
7. `<`   redireccionar entrada
8. `;`   separa comandos en la misma linea comando1; comando2; etc
9. `&`   ejecución en segundo plano comando1&
10. `&&`  ejecución consecutiva de comandos: comando1 && comando2. El segundo se ejecuta solo si el primero acabo sin errores
11. `|`   Pasa la salida del primer comando a la entrada del segundo. Muy importante es el comando pipe comando1 | comando2
12. `||`  ejecución consecutiva de comandos: comando1 || comando2. El segundo se ejecuta solo si el primero ha fallado.
13. `~`   Identifica el directorio home del usuario: ls ~ (Alt gr +  4)
14. \`\`   Ejecutar el comando incluido:  \`comando\`  
15. `$`   Identifica varialbes del sitema ej. $HOME o ejecuta comandos $(comando1)
16. `!`   Ejecuta el comando indicado del buffer !5 (comando cinco del buffer). Caso especial !! ultimo comando ejecutado.
17. `!!`  Ejecuta el último comando ejecutado.
