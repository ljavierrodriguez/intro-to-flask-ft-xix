## Workspace MySQL Gitpod and Docker

### To install on Docker (Windows, Linux or Mac)

    $ docker-compose up -d


### Crear el entorno virtual usando "pipenv"

```shell
$ pipenv --python=3.x
```
###  Crear y/o Activar el entorno virtual usando "pipenv"

```shell
$ pipenv shell
```

### Instalar librerias en nuestra aplicacion usando "pipenv"

```shell
$ pipenv install <paquete>
```
Ejemplo:
```shell
$ pipenv install flask
```

### Crear el siguiente archivo ***src/main.py*** y escribir el siguiente codigo:

```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

```

### Para iniciar nuestra aplicacion en el terminal ejecutar la siguiente instruccion:

```shell
$ python src/main.py
```

### Configurar nuestra aplicacion en modo desarrollo:

```python
# src/main.py
...
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
...
```

### Crear una ruta o endpoint en nuestra aplicacion usando ***"@app.route()"***

```python
# src/main.py
...
# Method By Default = GET
@app.route('/', methods=['GET'])
def main():
    return "Hola Mundo" 
...

```