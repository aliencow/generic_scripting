### Regular expressions

Visualizer gratuito de regular expressions https://regex101.com/

* `*`. Comodin absoluto equivale a cualquier palabra.
* `[]`. Indicar rangos de búsqueda ej `[aeiou]` buscará las vocales en minúscula `[AEIOU]` en mayúscula. Si se incluye el signo `-` se puede especificar desde hasta ej `[a-z]` buscará todas las letras del alfabeto minúsculas, `[A-Za-z]` buscará tanto mayúscusculas como minúsculas o `[0-9a-z]` caracteres numéricos y alfabeto minúscula. Si añadimos `^` dentro del rango sirve para negar la condición. Ejemplo `[^a-z]` buscaría las letras del alfabeto excepto las minúsculas. Para incluir el signo `-` en la búsqueda como caracter lo pondremos precedido del carater de escape `\` `[\-a-z]` o bien al final del rango `[a-z-]`
* `^`.  
* '|'. Funciona como or busca una u otra expresión a cada lado del símbolo `|` ejemplo `cat|dog` encontrará todos los 'cat' o 'dog' que haya en el texto. No se limita a dos opciones puede tener mas ej `cat|dog|fish|etc.|...`.
* `.`. Shorcut Equivale a cualquier dígito.
* `\w`. Shortut Equivale a `[a-zA-Z0-9]`
* '\W'. Shortcut Equivale a `[^a-zA-Z0-9]`
* `\d`. Shortut Equivale a `[0-9]`
* '\D'. Shortcut Equivale a `[^0-9]`
* `\t`. Busca tabs
* '\n'. Busca enter (newline)
* `\s`. Shorcut equivale a buscar tabs, intros, etc.
* `\S`. Negación de la anterior es decir busca todo menos tabs, intros, etc.
* `\`. Caracter de escappe para incluir los caracteres de sintaxis como `-[]^ ()`.

Quantifiers

* `*`. significa 0 o mas veces
* `+`. significa 1 o mas veces

Ver el resto en el curso de UDEMY y consultar algo mas.
