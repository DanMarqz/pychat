# Pychat (Sockets)

Este repositorio contiene una simple aplicación de chat implementada en Python utilizando sockets. La aplicación consta de un **servidor** *(server.py)* y un **cliente** *(client.py)* que permiten la comunicación entre diferentes clientes conectados a través de una red local.


## Instalación de dependencias

La aplicación no requiere de dependencias externas más allá de las bibliotecas estándar de Python.


## Funcionamiento de la aplicación

### Servidor *(server.py)*

El servidor se encarga de aceptar conexiones entrantes de clientes y gestionar la comunicación entre ellos. Cada vez que un cliente envía un mensaje, el servidor lo retransmite a todos los demás clientes conectados.

### Cliente *(client.py)*

El cliente se conecta al servidor y proporciona una interfaz simple para que el usuario pueda enviar y recibir mensajes en el chat. El cliente utiliza dos hilos separados para manejar la entrada del usuario (enviar_mensajes()) y la recepción de mensajes del servidor (recibir_mensajes()).
Ejecución

Ejecuta el servidor en una terminal:

```bash
python server.py
```

El servidor estará escuchando en el puerto 5556.

Ejecuta el cliente en otra terminal:

```bash
python client.py
```

Asegúrate de reemplazar 'IP_SERVIDOR' con la dirección IP del servidor.

A partir de este momento, puedes enviar y recibir mensajes en el chat.

## Notas adicionales

Asegúrate de que el firewall de tu sistema permita la comunicación en el puerto 5556.
La aplicación es básica y no cuenta con medidas avanzadas de seguridad o manejo de errores. No se recomienda su uso en un entorno de producción sin mejoras adicionales.

