## using wakeonlan from cli

`synonet --wake xx:xx:xx:xx:xx:xx ethX`


## docker compose: Error while loading shared libraries: libz.so.1: failed to map segment from shared object: Operation not permitted

Este error se produce cuando hace tiempo que no se ejecuta nada de docker.

Got it solved by re-mounting the /tmp to give the volume permission to execute (it was accessible with read-only). So this solved:

```bash
sudo mount /tmp -o remount,exec
```

## Eliminar desde linux las carpetas @eaDir que crea synology

```bash
sudo find . -type d -name "@eaDir" -prune -exec rm -rf {} \;
```
