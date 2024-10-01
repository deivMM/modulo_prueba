- Para actualizar un modulo en tu ordenador:
    Ir al directorio y -> pip install --upgrade .
    o  si el módulo está instalado desde GitHub
    pip install --upgrade git+https://github.com/usuario/repositorio.git

- Para instalar un modulo en tu ordenador desde GitHub:

    pip install git+https://github.com/usuario/repositorio.git


## Para crear un modulo en python
- Estructura del proyecto:
```
mi_modulo/
│
├── mi_modulo/                # Carpeta del módulo
│   ├── __init__.py           # Archivo para hacer que Python trate esta carpeta como un paquete
│   └── mi_script.py          # Script con funciones/clases
│
├── tests/                    # Carpeta opcional para tests
│   └── test_mi_script.py
│
├── setup.py                  # Script de instalación
└── README.md                 # Archivo de descripción del proyecto
```
