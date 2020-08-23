[![Build Status](https://travis-ci.com/eryxcoop/mora-backend.svg?branch=master)](https://travis-ci.com/eryxcoop/mora-backend)

### Pre-requisites
Es necesario tener instalado docker, docker-compose, mongo y python3


### Bootstrapping
Crear un entorno virtual de python y instalar las dependencias que se encuentran en la carpeta requirements ejecutando 
el comando:

```pip install -r requirements/requirements.txt```

Estando en el directorio root

### Running
Copiar el contenido del archivo **.env.example** y pegarlo en un archivo **.env**. El valor de environment puede ser 
**testing**, **development** o **production** según corresponda. 

En el directorio root ejecutar ```docker-compose up```.


### Testing
Desde la línea de comandos y seteando la variable de entorno **environment** en **testing**:
```python -m unittest discover tests```

También se puede configurar un runner de python unittest en el IDE setenado las variables de entorno correctas. 

### Deploy
