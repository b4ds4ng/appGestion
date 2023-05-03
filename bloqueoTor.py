import socket
import requests

IP_SERVIDOR = '127.0.0.1'  # La dirección IP del servidor
PUERTO = 8080  # El puerto que se va a escuchar

# Obtener la lista de nodos de salida de la red Tor
TOR_EXIT_NODES_URL = 'https://check.torproject.org/exit-addresses'
TOR_EXIT_NODES = []

response = requests.get(TOR_EXIT_NODES_URL)
if response.status_code == 200:
    for line in response.text.splitlines():
        if line.startswith('ExitAddress'):
            tor_ip = line.split()[1]
            TOR_EXIT_NODES.append(tor_ip)

def main():
    # Crear un socket de tipo SOCK_STREAM para recibir conexiones TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asociar el socket con la dirección IP del servidor y el puerto que se va a escuchar
    servidor_socket.bind((IP_SERVIDOR, PUERTO))

    # Escuchar conexiones entrantes
    servidor_socket.listen()

    while True:
        # Aceptar la conexión entrante y obtener la dirección IP del cliente
        conexion_cliente, cliente_direccion = servidor_socket.accept()
        ip_cliente = cliente_direccion[0]

        # Verificar si la dirección IP del cliente se encuentra en la lista de nodos de salida de la red Tor
        if ip_cliente in TOR_EXIT_NODES:
            print(f'Conexión desde la red Tor bloqueada: {ip_cliente}')
            conexion_cliente.close()
        else:
            # Si la dirección IP del cliente no se encuentra en la lista de nodos de salida de la red Tor, procesar los datos normalmente
            print(f'Conexión aceptada desde {cliente_direccion}')
            data = conexion_cliente.recv(1024)
            print(f'Datos recibidos: {data.decode()}')
            conexion_cliente.close()

if __name__ == '__main__':
    main()