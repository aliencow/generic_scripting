## Como configurar en DSM un puerto externo con proxy inverso.

Estas son las opciones en el panel de control para esta configuración

* Acceso externo > Configuración del enrutador > crear

  Ahí abrimos el puerto. Si no funciona el test hay que abrirlo en el router.
  Si tenemor del `docker-compose` en up, el servicio ya aparecerá para ponerle puerto.
  Hay que tener el subdominio configurado en la sección DDNS para activar el proxy inverso.

* Seguridad. 
  
  Hay que apuntar los certificados ssl del subdominio correctamente.
  
* Portal de inicio de sesion > Avanzado > Proxy inverso

  Ahí configuramos para que el proxy inverso proporcione el servicio seguro.
  Hay que apuntar el origen al subdominio configurado en el punto 1 y el destino al puerto escogido.
