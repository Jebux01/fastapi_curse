# Usuarios by Jebux
## Ejemplo de Microservicio con FastAPI, Pydantic, SQLAlchemy y MariaDB

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Build Status](https://img.shields.io/badge/build-develop-blue.svg)](https://shields.io/)


## Caracteristicas
- Alta de un usuario, lista de usuarios


## Datos tecnicos
proyectos utilizados:

- [Python] - Tecnologia de alto nivel multiparadigma!
- [FastAPI] - utilizada para el consumo de datos
- [Pydantic] - Manejo de Modelos
- [SQLAlchemy] - Serializacion, Modelos y ORM

## Preparacion de trabajo
Esto asegurará que el código sea linter antes de que termine en la canalización; de lo contrario, la canalización se rechazará automáticamente si se encuentra algún error.

## Uso en windows (Descargar pip)
## [pip](https://bootstrap.pypa.io/get-pip.py) <- este link se utilizara para descargar pip
```cmd
(carpeta donde se descargo el archivo .py)
python get-pip.py
```

## Uso en linux 
```sh
sudo apt-get install python3-pip
```

- [PIP] - En caso de que sea linux solo recordar utilizar pip3
```
pip install --user virtualenv
pip install -r requirements.txt
```
Esto descargará todas las dependencias necesarias para ejecutar el proyecto, nada más.

## Comandos Utiles
- Para ejecutar linter en archivos organizados: pre-commit run
- Para ejecutar linter en todos los archivos: pre-commit run --all-files

## Como ejecutar el server

# Windows 

```cmd
pip3 install virtualenv
virtualenv cc_env
source cc_env/bin/activate
deactivate
```

# Linux ubuntu/debian
```sh
cd proyecto
pip3 install virtualenv
virtualenv cc_env
source cc_env/bin/activate
deactivate
```

## License
MIT

