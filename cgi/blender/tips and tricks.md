# Algunos tips Blender

## Atajos de teclado

### View y camara

Rotacion view - Apretando boton del medio y desplazando. Si pulsamos +alt se para en los views comunes.
Traslacion view - Boton del medio del raton + Shift
Zoom view - Boton del medio + Ctrl
Numpad +'/' - Centra el objeto seleccionado
Numpad *'.' - Centra el objeto seleccionado y hace zoom
Numpad + '0' - Cambia de camera de rodaje a camera del view y viceversa.
Numpad + '5'- Cambia de view ortoganal a perspectiva y viceversa.


### Interface
't' - mostrar ocultar paleta de herramientas
'n' - mostara ocultar opciones
Shift + s (con 3d cursor activo) desplazar el 3dcuror
Shift + a - Añadir cosas segun el modo activo (objeto, componentes, etc)
SpaceBar - Permite mover las selecciones realizadas con box lasso etc. Se activará la selección al soltar                                                                                   
Ctrl + a - Apply transformations to geometry (cuando se escala, por ejemplo) like Freeze Transformationss
Ctrl + j - Join unifica en una dos geometrias poligonales.


### Modelado
Tab - Cambia de modo activo (de objeto a componentes y viceversa)
Tab + pulsacion larga - Permite escoger el modo activo entre los existentes, siempre que se haya configurado en Edit-> Preferences-> Keymap-> Tab for Pie Menu

'1' (Sin Numpad) - Activa para selección de vertices
'2' (Sin Numpad) - Activa para selección de edges
'3' (Sin Numpad) - Activa para selección de faces

#### Modo sculpt
Space Bar - Muestra los atajos de teclado de los brushes
Ctrl + mouse - Cambia la orientación del brush (hacia adentro o hacia afuera)
Shift + mouse - Smooth
'f' - En modo escultura permite regular el tamaño del brush

MASK
'a' - Muestra las opciones de Mask en menú flotante.
Ver menu 'Mask' también (Clear Mask etc.)
Box Hide - Oculta la zona del recuedro.
Alt + 'h' - Operación inversa, muestra lo oculto.

FACE SET
'h' (Solamente si se pinto algun Face Set) - Oculta todo excepto el face set activo.
Alt + 'h' - Operación inversa, muestra lo oculto.
Ctrl + mouse (Si estamos sobre un Face Set) - Continua pintando con el color del  face set seleccionado
Ctrl + mouse (Si estamos sobre un Face Set) - Continua pintando con el color del  face set seleccionado
Ver mnu 'Face set', para eliminar los sets pintados 'Face from visible', para crear a partir de la máscara 'Face from Mask', etc.

Multires Displacement recupera la forma original.
Box Trim - Recorta la geometría  (pone tapas)
Line Project - aplica un plano de corte por donde se marca la línea. Hace un trim y recalcula las faces.

Dyntopo y Remesh sirven para retopologizar la geometria.
Shift + r (en este modo) Permite regular el grid para remesh (tamaño polígonos)
Ctrl + r (en este modo) Ejecuta remesh

### Programación

Basado en el tuorial de blender Blender 2.9 Python Addon Programming Tutorial
https://www.youtube.com/watch?v=yNdjdmepMMQ


StudioCode
You will need the extension Blender Development
Once installed Ctrl+Shift+P can be used for commands like:
- Blender: new AddOn 
- Blender: Start