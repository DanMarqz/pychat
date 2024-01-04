import socket
import threading

def enviar_mensajes():
    while True:
        # Enviar mensajes al servidor
        message = input(35.)
        client.send(message.encode('utf-8'))

def recibir_mensajes():
    while True:
        # Recibir mensajes del servidor
        data = client.recv(1024)
        print(data.decode('utf-8'))

# Configurar el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('IP_SERVIDOR', 5556))  # Reemplaza 'IP_SERVIDOR' con la IP del servidor

# Iniciar hilos para enviar y recibir mensajes simultáneamente
enviar_thread = threading.Thread(target=enviar_mensajes)
recibir_thread = threading.Thread(target=recibir_mensajes)

enviar_thread.start()
recibir_thread.start()
