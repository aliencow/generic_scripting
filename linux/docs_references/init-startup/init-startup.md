## PROCESOS DE INICIO EN LINUX

El proceso de inicialización de linux se queda ejecutando hasta que se finalize la ejecucion y se ejecuta con el nº de proceso 1 siempre. Puede haber dos gestores de inicialización: `init` o  `systemd`
Para conocer cual de ellos se está ejecutando usaremos el comando:
```
ps -f -p 1
```
### NIVELES DE EJECUCION DE LINUX
Los niveles de ejecución de linu son:
* 0 - Apagado
* 1 - Mono usuario (solo root) - (Modo rescate)
* 3 - Multiusuario sin entorno gráfico. (Modo normal sin gráficos)
* 5 - Multiusuario con entorno gráfico. (Modo normal con entorno gráfico)
* 6 - Reinicio

El cambio de modo se hará con `init` o `systemd` utilizando como argumento para cambiar al modo deseado lo que aparece en la siguiente tabla.

| Nivel | Cod. init | cod. systemd |
|-------|-----------|--------------|
| Apagado | 0 | runlevel0.target / poweroff.target |
| Mono usuario | 1 | runlevel1.target / rescue.target |
| Multiuser (sin ent. gráfico) | 3 | runlevel3.target / multi-user.target |
| Multiuser (con ent. gráfico) | 5 | runlevel5.target / graphical.target |
| Reinicio | 6 | runlevel6.target / reboot.target |

* Cambiar el nivel de ejecución con `init`:  `init <nivel>`. Ej: `init 6` reiniciará o `init 3` pondrá multiusuario sin entorno gráfico.
* Cambiar el nivel de ejecución con `systemd`: `systemctl isolate <nivel>`. Ej: `systemctl isolate reboot.target ó runlevel6.target` reiniciarña o `systemctl isolate multi-user.target (o runlevel3.target)` pondrá multiusuario sin entorno gráfico.
* Consultar los niveles de ejecución con el comando `runlevel`. Devolvera el nivel/niveles de ejecución activos.
* Consultar los niveles de ejecucion con `systemctl`: `systemctl list-units --type target`. Nos mostrará las unidades de configuración activas donde podremos consultar por el nombre de la tabla superior.

### Apagado, reinicio, etc.

* `shutdown`.  Apaga la máquina (o no). Se puede inditar un time: `now` apaga inmediato, `+n`(apaga en minutos) u `hh:mm`(apaga a las hh:mm)- Ejemplo `shutwown +5` apagará la máquina transcurridos 5 minutos.
  * option `-k`. No apaga realmenbte solo avisa alos usuarios.
  * option '-r'. Reinicia después de apagar.
  * option `-h`. Apaga al momento (halt).
  * option `-c`. Cancela un apagado previamente programado

* `reboot`. Reinicia el sistema.
  * option `-f`. Forzar reinicio
  * option `-n`. No sincronizar los discos (no disponible en todas las distros)

* `halt`. Apaga el sistema
  * option `-f`. Fuerza el apagado

* `poweroff`. Apaga el sistema
  * option `-f`. Fuerza el apagado
