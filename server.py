import socket
import threading

def handle_client(client_socket):
    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break

        # Enviar los datos a todos los clientes conectados
        for c in clients:
            c.send(data)

        # Imprimir el mensaje en el servidor
        print(f"Mensaje recibido: {data.decode('utf-8')}")

    # Cerrar la conexión del cliente
    client_socket.close()

# Configurar el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5556))
server.listen(5)

print("[*] Esperando conexiones en el puerto 5556")

# Lista para almacenar clientes conectados
clients = []

while True:
    client, addr = server.accept()
    print(f"[*] Conexión aceptada de {addr[0]}:{addr[1]}")

    # Agregar el cliente a la lista
    clients.append(client)

    # Iniciar un hilo para manejar la comunicación con el cliente
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
