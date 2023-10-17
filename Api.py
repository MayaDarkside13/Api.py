import redis

# Crea una instancia de Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Implementa la operación de creación
def create(key, value):
    redis_client.set(key, value)

# Implementa la operación de lectura
def read(key):
    return redis_client.get(key)

# Implementa la operación de actualización
def update(key, value):
    redis_client.set(key, value)

# Implementa la operación de eliminación
def delete(key):
    redis_client.delete(key)

# Ejecuta la API
if __name__ == "__main__":
    # Crea una nueva clave
    create("key1", "valor1")

    # Lee el valor de la clave
    value = read("key1")
    print(value)

    # Actualiza el valor de la clave
    update("key1", "valor2")

    # Elimina la clave
    delete("key1")
