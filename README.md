# Test API and Behave

## Descripción

Proyecto para la prueba de desarrollo de una API y testing mediante Behave.

## Pruebas

Para facilitar la ejecución de las pruebas se creado un [Makefile](./Makefile) con los comandos necesarios.
Se puede comprobar el catálogo de comandos con:

```bash
    make help
```

Como pre-requisito se necesita tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/).

### Tratamiento de datos en API

El código Python que se ha desarrollado para la prueba de la `petstore` se encuentra en la carpeta [apis](./apis/).

- En la carpeta de [petstore](./apis/petstore) se encuentra el código para hacer las llamadas a la api de `petstore` con las distintas clases y métodos necesarios.
- El fichero [test.py](./apis/test.py) contiene el código con el flujo de llamadas para probar la primera API.

Para ejecutar el código se puede hacer con los siguientes comandos:

```bash
    make build-apis
    make run-apis
```

Para terminar se puede limpiar el entorno con:

```bash
    make clean-apis
```

### Desarrollo de una API (CRUD)

En la carpeta [crud](./crud/) se encuentra el código para el desarrollo de una API con las operaciones CRUD.
Concretamente, el código está en el fichero [backend.py](./crud/backend.py).
Para crear la API se ha utilizar [Flask](https://flask.palletsprojects.com/en/2.0.x/) y como base de datos se ha utilizado [MongoDB](https://www.mongodb.com/).

Para levantar el servicio se ha montado un entorno con [Docker Compose](https://docs.docker.com/compose/) que tiene los siguientes servicios:

- backend: servicio con la API desarrollada en Python.
- mongo: base de datos MongoDB.
- mongo-express: interfaz web para la base de datos MongoDB.
- test: servicio para ejecutar los tests de aceptación de la API con [Behave](https://behave.readthedocs.io/en/stable/).

Para levantar el entorno se puede hacer con los siguientes comandos:

```bash
    make build-crud
    make run-crud
```

Con docker-compose se expone la api en el puerto `8888` de localhost:

- `http://localhost:8888`

Los endpoints asociados son:

- GET /health
- GET /products
- GET /products/{id}
- POST /products
- PUT /products/{id}
- DELETE /products/{id}

Si se quiere ejecutar los tests de aceptación se puede hacer con:

```bash
    make run-crud-tests
```

Finalmente, si se quiere limpiar el entorno se puede hacer con:

```bash
    make clean-crud
```

De esta manera se ejecuta la feature [crud.feature](./crud/tests/features/crud.feature) que contiene un set básico (happy path) de tests de aceptación de la API.
