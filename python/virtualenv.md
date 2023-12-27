# Virtualenv


### Virtual env creation on python3 (lo trae incorporado)

Make a project directory(folder) and cd into it. To make a virtual environment type the command:

#### Creating a virtualenv folder

    #cd to the project folder

    python -m venv <envmane>
    #<envmane> is the name of virtual env folder you will create

#### Now activate the virtual environment.

* In Windows
  * From CMD - `.\<envname>\Scripts\activate`
  * From Powershell - `.\env\Scripts\Activate.ps1`. If it doesn't work try to activate current user execution policy with: `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`

* In linux (or Mac) use  `. env/bin/activate`

#### Deactivating the virtual environment

* In all platforms: `deactivate`

#### Upgrading python version to the venv 

python -m venv --upgrade <envname>

o bien desinstalar la actual rm -r <envname>  e instalar de nuevo
python -m venv <envmane>
En este ultimo caso recordar que hay que actualizar las instalaciones

## Exporting requirements.txt
You can do that with pip freeze command
``` bash
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```

### Método tradicional para usar virtualenv:


VirtualEnv se usa para crear un entorno virtual para trabajar en python sin contaminar lo demas

para instalar virtualenv:

desde CMD: pip install virtualenv

para crear un entorno virtual:

desde CMD: virtualenv --python=python2.7 flaskpymongo
donde se pone la version de python y el nombre del directorio

para activar el entorno virtual:

desde CMD: source flaskpymongo/bin/activate (Mac)
desde CMD: call flaskpymongo/scripts/activate  (Windows)
donde flaskpymongo es el nombre del directorio donde esta el entorno virtual

para desactivar el entorno virtual

desde CMD: deactivate


Método con virtualenvwrapper:

Otro modo de poner el virtualenv mas facil es con mkvirtualenv. Previamente tenemos que ejecutar virtualenvwrapper

Explicacion de virtualenv https://gist.github.com/IamAdiSri/a379c36b70044725a85a1216e7ee9a46
en windows http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/
virtualenvwrapper https://virtualenvwrapper.readthedocs.io/en/latest/index.html
virtualenvwrapper https://pypi.org/project/virtualenvwrapper-win/
instalar en mac http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-mac-os-x/

comandos mkvirtualenv https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

para instalar en windows
pip install virtualenvwrapper-win
en mac
pip install virtualenvwrapper

Uso:
makevirtualenv nombre
crea un entorno virtual denominado nombre

luego nos ubicamos en el directorio por ejemplo cd f:\projects\env\nombre

y lo hacemos proyecto actual con:

setprojectdir .   (desde dentro del directorio creado)

con deactivate desactivamos el entorno.

Para volverlo a activar:  workon nombre

## Atencion virtualenv no es compatible con poetry
Ver el tutorial de `poetry.md` para ver como funciona Poetry
