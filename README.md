Puedes probar la API de Redis sin un servidor utilizando un cliente HTTP local, como cURL o Postman.

Por ejemplo, para crear una nueva clave, puedes enviar la siguiente solicitud utilizando cURL

Curl -X POST http://localhost:8080/keys -d key=key1 -d value=value1

Esta solicitud creará una nueva clave con la clave `key1` y el valor `value1`.

Para leer el valor de una clave, puedes enviar la siguiente solicitud utilizando cURL:

Curl http://localhost:8080/keys/key1

Esta solicitud devolverá el valor de la clave `key1`.

Para actualizar el valor de una clave, puedes enviar la siguiente solicitud utilizando

cURL:

Curl -X PUT http://localhost:8080/keys/key1 -d value=value2

Esta solicitud actualizará el valor de la clave `key1` a `value2`.

Para eliminar una clave, puedes enviar la siguiente solicitud utilizando cURL:

Curl -X DELETE http://localhost:8080/keys/key1

Esta solicitud eliminará la clave `key1`.

Puedes usar el IDE de Python, PyCharm, proporciona una herramienta llamada “REST Client” que se puede utilizar para enviar solicitudes HTTP a APIs.

