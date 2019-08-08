Usando git
==========

Video introductorio a git puedes verlo en este enlace:


https://www.youtube.com/watch?v=HVsySz-h9r4



Configuración y básicos
-----------------------

Comandoa para configuración:

	git config --global user.name "Juan R Nouche"
	git config --global user.email "juan.nouche@gmail.com"

de este modo configuramos nuestro usuario

	git add --help

obtener ayuda de cualquier comando (por ejemplo add)

	git init

inicializa el directorio del proyecto local para trabajar con git

	git status

comprueba el status de los commits

Para excluir ficheros del commit debemos crear el fichero **.gitignore**
dentro de este fihero van los nombres de fichero directorios o tipos de datos a excluir (Ejemplo ``*``.pyc excluye del commit todos los ficheros tipo pyc)

**STAGING AREA:** es una zona intermedia donde quedan los ficheros antes de hacer el final commits. Primero se marcan ahí y una vez que estamos
seguros de lo que queremos enviar se hace el commits

	git add

se añaden ficheros al staging AREA
solo se añaden los ficheros que no estén dentro de gitignore por ejemplo:

	git add mifichero.xxx

mp funcionaria si mifichero.xxx estuviese incluido en *.gitignore*

	git add -A

añade todo lo que no esté en .gitignore al commit

	git reset

contrario de add quita ficheros del commit

	git reset mifichero.xxx

quita del staging a mifichero.xxx

	git reset

elimina todos los ficheros del staging

podemos si estan bien o mal con git status

*Nota: en este link podemos encontrar los comandos del editor por defecto VI por si nos encontramos con dificultades de uso.*

https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor


Manipulando repositorio
-----------------------


Enviar REPO
^^^^^^^^^^^

Un proyecto que ya existe en carpeta local enviarlo a github (o gitlab)

Comandos para empezar un proyecto

Después de iniciar el git hacemos nuestro primer commit:

	git add -A #añadimos todo lo que no esté en **.gitignore**
	git status  #comprobamos si es correcto
	git commit -m "primer commit o algo así" #Prepara el commit

A continuación creamos el proyecto en github:

  git remote add origin ``https://github.com/aliencow/flask_pymongo.git``

Esto crea el remote en github desde nuestro usuario previamente github nos da el link para
añadir el origin

  git push -u origin master

envía y crea un proyecto en github
(nos va a pedir nuestro usuario y pass en github)

Clonar REPO
^^^^^^^^^^^

Un proyecto existente en github que se clona en carpeta local

Comandos para clonar un proyecto

Antes de clonar debemos obtener la dirección del repo en github ejemplo: ``https://github.com/aliencow/flask_pymongo.git``

Para clonar ejecutamos:

  git clone <urlgit> <carpeta>

ejemplo:

  git clone ``https://github.com/aliencow/flask_pymongo.git`` micarpeta   //crea el directorio micarpeta y clona el repositorio

si creamos primero la carpeta y queremos clonar dentro de ella se pone . en lugar del nombre de la micarpeta ejemplo:

  cd micarpeta
  git clone ``https://github.com/aliencow/flask_pymongo.git`` .

de ese modo el proyecto se clonaría dentro de micarpeta sin crear una nueva

  git remote -v

para ver el status del remoto

  git branch -a

para ver la rama en la que estamos


Actualizaciones REPO
--------------------

  git diff

podemos ver los cambios en el código que no ha sido realizado en commit

  git add -A

una vez actualizados los campos añadimos todo al commit y...

  git commit -m "los cambios que sean"

... preparar el commit que sea

  git pull origin master

Hacemos un pull previo por si alguien ha hecho cambios que no tenemos

  git push origin master

Finalmente hacemos el push para subir nuestros cambios

  git stash save --keep-index --include-untracked

Si queremos descartar los cambios hechos en local desde el ultimo commit y
sincronizar con el master con pull

  git push --force --set-upstream origin master

forzar a que el repositorio se actualice con el local para cuando haya
conflictos pull y push

BRANCHING
---------

A continuación los comandos para crear ramificaciones de cógigo

	git branch cambio-codigo

crea una rama llamada cambio-codigo

	git branch

git branch a secas muestra las ramas que hay y cual está activa

	git checkout cambio-codigo

pone cambio-codigo como rama activa

	git push -u origin cambio-codigo

hacer el push a una rama especifica

	git push

una vez hemos hecho el checkout no es preciso especificar la rama con
git push y git pull enviamos o bajamos de la rama seleccionada

	git branch -a

Nos muestra todas las ramas vivas y el estatus de cada incluido el master.

	git branch --merged

Nos permite ver como esta el merge de branchs

	git chekout master
	git pull origin master
	git merge cambio-codigo
	git push origin master

Secuencia de comandos para hacer el merge de una rama en el master
observese que se hace el push directamente.. no hace falta el commit en este caso

	git branch -d cambio-codigo

Borra una rama en el repositorio local

	git push origin --delete cambio-codigo

pero hay que hacer el push del delete para borrarlo en github
