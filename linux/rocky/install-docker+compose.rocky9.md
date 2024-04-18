# Instalar docker en rocky 9

0. ### Tutorial aqui: 

    https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-rocky-linux-9

1. ### Primero actualizar la base de datos de paquetes

    ```bash
    sudo dnf check-update
    ```
2. ### Añadir el repositorio oficial de docker (como no existe repositorio especifico de Rocky se usa el de CentOs)

    ```bash
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    ```

3. ### Con el repositorio anhadido instalamos docker que se compone de 3 paquetes:

    ```bash
    sudo dnf install docker-ce docker-ce-cli containerd.io
    ```

4. ### Con la instalacion completada arrancar el daemon

    ```bash
    sudo systemctl start docker
    ```
5. ### Verificar que esta ejecutandose

    ```bash
    sudo systemctl status docker
    ```
    La salida deberia ser algo parecido a esto
    ```bash
    Output
    ● docker.service - Docker Application Container Engine
      Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
      Active: active (running) since Sun 2016-05-01 06:53:52 CDT; 1 weeks 3 days ago
        Docs: https://docs.docker.com
    Main PID: 749 (docker)
    ```

6. ### Y ultimo. Asegurarse de que se arranque con cada reinicio:

    ```bash
    sudo systemctl enable docker
    ```


# Instalar docker compose en rocky 9

0. ### Tutorial aqui: 

    https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-rocky-linux-9#step-2-setting-up-a-docker-compose-yml-file

1. ### Primero actualizar la base de datos de paquetes

    ```bash
    sudo dnf check-update
    ```
2. ### Añadir el repositorio oficial de docker (como no existe repositorio especifico de Rocky se usa el de CentOs)

    ```bash
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    ```

3. ### Con el repositorio anhadido instalamos docker compose:

    ```bash
    sudo dnf install docker-compose-plugin
    ```

4. ### Y ultimo. Verificar la instalacion

    ```bash
    docker compose version
    ```
    La salida deberia ser algo parecido a esto
    ```bash
    Output
    Docker Compose version v2.10.2
    ```



