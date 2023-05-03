import psutil

def count_connections(port):

    # Obtenemos todas la conexiones de red
    connections = psutil.net_connections()

    # Contamos el número de conexiones recibidas en el puerto
    count = sum( 1 for c in connections if c.status == 'ESTABLISHED' and c.laddr.port == port)
 
    # Mostramos el resultado
    print(f'El puerto {port} está recibiendo {count} conexiones')

# Pedimos ingresar el puerto a escanear
port = int(input('Ingresa el puerto: '))

# Contamos el número de conexiones recibidas en el puerto
count_connections(port)
