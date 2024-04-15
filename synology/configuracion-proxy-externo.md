## Como configurar en DSM un puerto externo.

En panel de control hay dos opciones para esta configuración.
1- Acceso externo - Configuración del enrutador - crear
  Ahí abrimos el puerto. Si no funciona el test hay que abrirlo en el router.
  Si tenemor del docker-compose en up, el servicio ya aparecerá para ponerle puerto.
  Hay que tener el subdominio configurado en la sección DDNS para activar el proxy inverso.
3- Seguridad. Hay que apuntar los certificados ssl del subdominio correctamente.
3- Portal de inicio de sesion - Avanzado - Proxy inverso
  Ahí configuramos para que el proxy inverso proporcione el servicio seguro.
  Hay que apuntar el origen al subdominio configurado en el punto 1 y el destino al puerto escogido.
