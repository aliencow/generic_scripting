
# Uso de gitlab para trabajar

## Subir un proyecto existente a gitlab an????xa

tutorial here: https://medium.com/@farzanajuthi08/how-to-make-a-project-into-gitlab-and-upload-your-existing-code-into-gitlab-e6ba60e81dcb

Para subir un proyecto ya existente, es decir tenemos una carpeta ya creada con código
y queremos subirlo a gitlab. 

Iremos a gitlab y en el grupo que nos interese creamos un proyecto vacio `New Project` -> `Create Blank Project`
Nos mostrará esta información:

* ### Git global setup- Las variables globales que debemos configurar

```bash
git config --global user.name "juan.nouche"
git config --global user.email "juan.nouche@an????xa.com"
```

* ### Create a new repository - Si queremos crear un nuevo repositorio clonable

```bash
git clone ssh://git@localhost:30001/web/access-template.git
cd access-template
git switch -c main
touch README.md
git add README.md
git commit -m "add README"
git push -u origin main
```

* ### Push an existing folder <<<<<<<<<<<<<<<<<<<<<< ***Esta es la que nos interesa***

```bash
cd existing_folder
git init --initial-branch=main
git remote add origin ssh://git@localhost:30001/web/access-template.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

* ### Push an existing Git repository

```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin ssh://git@localhost:30001/web/access-template.git
git push -u origin --all
git push -u origin --tags
```

* #### En todos los apartados anteriores access-template es el nombre del proyecto.

Nos pondremos en el command line en nuestro projecto y  

1. Seteamos el usuario global 

```bash
git config --global user.name "juan.nouche"
git config --global user.email "juan.nouche@an????xa.com"
```
2. Ejecutamos lo indicado en `Push existing folder`


```bash
cd existing_folder
git init --initial-branch=main
git remote add origin ssh://git@gitlab.an????xa.com:30001/web/access-template.git
git add .
git commit -m "Initial commit"
git push -u origin main

#<<<<<<<<<<<<< HEMOS CAMBIADO >>>>>>>>>>>>>
#esta línea:
git remote add origin ssh://git@localhost:30001/web/access-template.git
#por esta otra:
git remote add origin http://gitlab.an????xa.com:30000/web/access-template.git


```
Listo!!!


## Clonar un projecto existente en nuestro folder

Un clonado simple:

`git clone http://gitlab.an????xa.com:30000/setup/vbsstudiolib.git .`

## Crear nueva rama git

In essence, there are two methods in Git for creating branches.
You can use a single command to create the branch and switch to it. Or you can create the branch first using one command and then switch to it later using another command when you wish to work with it.

```bash
// create a branch and switch to the branch
$ git checkout -b <branch-name>

// create a branch only
$ git branch <branch-name>
```

To see a list of all available branches, you can use this command:

```bash
$ git branch
```

Finally, suppose we later wish to switch to our new Git branch or any other branch we previously created. In that case, we can make use of the git checkout command.


```bash
$ git checkout <branch-name>
```

### COPIAR UNA NUEVA RAMA A REMOTO.

First, create a new local branch:

```bash
git checkout -b my-feature-branch
```

Second, make changes and create a commit:

```bash
git add --all 
git commit -m "Added a new feature."
```
Third, push your commit with the --set-upstream flag (-u for short):

```bash
git push -u origin my-feature-branch
```

### ELIMINAR UNA RAMA LOCAL

```bash
git branch --delete <branchname>
```

## Otras cuestiones adicionales

### Problemas en el clonado

Cuando se resite un ficherito como por ejemplo el shelves.mel

git stash save --keep-index
git reset --hard


### Para buscar iconitos para los projectos:

https://www.pngfly.com/  #buscador de pngs free


### Uso de git stash

uso de git stash https://code.tutsplus.com/es/tutorials/quick-tip-leveraging-the-power-of-git-stash--cms-22988

git stash guarda cambios sin stagear
git pull actualizamos
git stash pop recupera los cambios


## CONFIGURACION

```bash
git config --list # lista los parametros de configuración
git config --global <nombre_parametro> <contenido> # Cambia el parametro con nombre nombre_parametro al contenido suministrado (en global)
git config --local <nombre_parametro> <contenido> # Cambia el parametro con nombre nombre_parametro al contenido suministrado (solamente para el repositorio local)
```
