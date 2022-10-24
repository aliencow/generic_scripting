# Poetry
Is a package manager for python to control de virtual environments and dependencies for projects.
you can download and install it from https://python-poetry.org

A config Tutorial
https://www.youtube.com/watch?v=Ib7fNOIGM7E


## Poetry - Package Management for Python

Poetry is a dependency manager tracking local dependencies of your projects and libraries.
See https://github.com/python-poetry/poetry for more information.

>>>>>>>>>>>>>>>>>>>>>> ATENCION NO ES COMPATIBLE CON virtualenv si se va a usar desinstalar virtualenv primero

## Poetry PATH insertion to use in wsl

Poetry adds to default path this route `.poetry\bin`, for example: `C:\Users\juan.nouche\.poetry\bin` but when whe are in wsl it can´t find it because of linux wsl path environment is other format and another syntax.
Then we need to add the route of this route to wsl path. To make it, we´ll include at the end of The ` ~/.bashrc` (startup script) a new line including one export to path like the lower example:

``` bash

# Anhadido por JUAN para poder usar poetry

export PATH="$PATH:/c/Users/juan.nouche/.poetry/bin"

```

## Poetry set the virtualenv folder to same folder as the project

By default poetry installs the virtualenvs in this path `~/.cache/pypoetry/virtualenvs`
Is preferably to set the virtualenv folder in the same path as the project. To do this (if we use VS code) we need to modify the poetry config.
Let´s see the actual config listing it with `poetry config --list` to check the content of this config var: `virtualenvs.in-project`.
If it´s set to false we need to set it to true using this command `poetry config virtualenvs.in-project true`.

## Create a poetry environments

### From an existing project folder

Go to a terminal and change pwd to your project dir. Once in your folder we use the command `poetry init`
The master will ask some question about package name, your name, your email and so on.
You can leave default values or you can skip these question with the option `-n` (`poetry init -n`)
In any case poetry will create the `pyproject.toml` that will contains all dependencies of our project.

### Creating his own folder
To do that form the terminal go to the parent path of the project you want to create an type the command: `poetry new <project_name>`
this creates a basic configuration for the project.

## Adding some installations to project (`poetry add`)

It works like `pip install` adding to the project the python library we demand, `poetry add fastapi` will install fastAPI library in our project. Updating immediatly the dependencies.

## How to run python

If we run the python file as usual (`python <program_name>.py`) the program won´t get the installed libraries because its behavior is global python so it can´t find the libraries added with poetry. To fix this item we could do it in one of this ways:
* To run a .py file inside de environment the command is `poetry run python <program_name>.py`. A bit large.
* If we use `poetry shell` instead, it will execute the environment and we can run the program like we always do in python: `python <program_name>.py`
* To exit from `poetry shell` type `exit` in the command line.

## Extract requirements.txt from poetry

Use this commands that are like `pip freeze`:
``` bash
# exporting with hashes
poetry export -f requirements.txt --output requirements.txt
# exporting without hashes
poetry export --without-hashes --format=requirements.txt > requirements.txt
# or
poetry export --without-hashes --format=requirements.txt --output requirements.txt
```


## Poetry help

``` bash

USAGE
  poetry [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]

ARGUMENTS
  <command>              The command to execute
  <arg>                  The arguments of the command

GLOBAL OPTIONS
  -h (--help)            Display this help message
  -q (--quiet)           Do not output any message
  -v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more verbose output and
                         "-vvv" for debug
  -V (--version)         Display this application version
  --ansi                 Force ANSI output
  --no-ansi              Disable ANSI output
  -n (--no-interaction)  Do not ask any interactive question

AVAILABLE COMMANDS
  about                  Shows information about Poetry.
  add                    Adds a new dependency to pyproject.toml.
  build                  Builds a package, as a tarball and a wheel by default.
  cache                  Interact with Poetry's cache
  check                  Checks the validity of the pyproject.toml file.
  config                 Manages configuration settings.
  debug                  Debug various elements of Poetry.
  env                    Interact with Poetry's project environments.
  export                 Exports the lock file to alternative formats.
  help                   Display the manual of a command
  init                   Creates a basic pyproject.toml file in the current directory.
  install                Installs the project dependencies.
  lock                   Locks the project dependencies.
  new                    Creates a new Python project at <path>.
  publish                Publishes a package to a remote repository.
  remove                 Removes a package from the project dependencies.
  run                    Runs a command in the appropriate environment.
  search                 Searches for packages on remote repositories.
  self                   Interact with Poetry directly.
  shell                  Spawns a shell within the virtual environment.
  show                   Shows information about packages.
  update                 Update the dependencies as according to the pyproject.toml file.
  version                Shows the version of the project or bumps it when a valid bump rule is provided.

```
