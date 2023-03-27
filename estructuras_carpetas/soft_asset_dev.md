
# Estructura de carpetas para asset de desarrollo

Este es el esquema de un projecto

```lua
projects_root/
    |
    projname/
        |-- dev/
        |-- assets/
            |
            assetname/
                |-- docs/
                |   |-- api/
                |   |-- user/
                |   |-- design/
                |   |-- requirements/
                |-- src/
                |   |-- app/
                |   |   |-- __init__.py
                |   |   |-- main.py
                |   |   |-- modules/
                |   |-- tests/
                |   |   |-- __init__.py
                |   |   |-- test_main.py
                |-- config/
                |   |-- settings.py
                |-- logs/
                |-- README.md
                |-- LICENSE
```
Aquí hay una breve descripción de cada carpeta:

docs/: Contiene la documentación del proyecto, que se puede dividir en subcarpetas según el tipo de documentación. Por ejemplo, api/ podría contener documentación sobre la API del proyecto, user/ podría contener documentación del usuario y requirements/ podría contener los requisitos del proyecto. La carpeta design/ podría contener diagramas de diseño y otras representaciones visuales del proyecto.

src/: Contiene el código fuente del proyecto. La carpeta app/ contiene el código de la aplicación principal, que puede dividirse en subcarpetas según los módulos o características de la aplicación. La carpeta tests/ contiene los casos de prueba para la aplicación. Cada subcarpeta debe contener un archivo __init__.py para que Python la reconozca como un paquete.

config/: Contiene archivos de configuración para el proyecto. Por ejemplo, settings.py podría contener variables de configuración globales para la aplicación.

logs/: Contiene los registros generados por la aplicación. Es posible que desee dividir los registros en subcarpetas según su nivel de severidad o según el componente de la aplicación que los generó.

README.md: Un archivo de texto que describe el proyecto, su propósito y cómo usarlo.
