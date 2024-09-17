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
## Reinicializar el entorno gráfico gnome

Alt+F2 + r + <intro>

## Ejecutar el filebrowser desde la terminal

nautilus --browser ~/some/directory

## Instalar python 3.10 on rocky
https://www.atlantic.net/vps-hosting/how-to-install-python-3-10-on-rocky-linux/

* Step 1 – Install Required Dependencies

    First, you will need to install some dependencies required to compile Python 3.10. You can install all of them by running the following command:

    ```bash 
    dnf install tar curl gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget make -y
    ```
    Once all the dependencies are installed, you can proceed to the next step.

* Step 2 – Install Python 3.10 on Rocky Linux

    First, go to the Python official download page and download the latest version of Python using the following command:

    ```bash 
    wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
    ```

    Once the download is completed, extract the downloaded file using the following command:

    ```bash 
    tar -xf Python-3.10.0.tar.xz
    ```

    Next, change the directory to the extracted directory and configure Python using the following command:

    ```bash 
    cd Python-3.10.0
    ./configure --enable-optimizations
    ```

    Next, start the build process using the following command:

    ```bash 
    make -j 2
    nproc
    ```

    Finally, install Python 3.10 by running the following command:

    ```bash 
    make altinstall
    ```

    After the successful installation, verify the Python installation using the following command:

    ```bash 
    python3.10 --version
    ```

    You will get the following output:

    ```bash 
    Python 3.10.0
    ```

## Eliminar desde linux las carpetas @eaDir que crea synology

```bash
sudo find . -type d -name "@eaDir" -prune -exec rm -rf {} \;
```