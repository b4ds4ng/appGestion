import psutil

def count_connections(port):

    # Obtenemos todas la conexiones de red
    connections = psutil.net_connections()

    # Creamos un diccionario para contar el número de conexiones por puerto
    port.counts = {}

    # Contamos el número de conexiones recibidas en cada puerto
    for c in connections:
        if c.status == 'ESTABLISHED':
            port = c.laddr.port
            if port not in port.counts:
                port_counts[port] = 1
            else:
                port_counts[por] += 1

# Mostramos el resultado por puerto
for port, count in port_counts.items():
    print(f'El puerto {port} está recibiendo {count} conexiones')

# Contamos el número de conexiones recibidas en todos los puertos
count_connections()
