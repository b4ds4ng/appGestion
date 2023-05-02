import nmap 
import json
# Escaneamos una IP para obtener los puertos abiertos 
# i los servicios que corren en cada puerto
def scan_ip(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-sS -O -v -T4 -p 1-65535')
# Creamos un diccionario para guardar la información del escaneo
results = {}
# Recorremos los puertos y guardamos la información en el diccionario
for host in nm.all_host():
    results[host] = {}
    for port in nm[host]['tcp']:
        state = nm[host]['tcp'][port]['state']
        service = nm[host]['tcp'][port]['name']
        results[host][port] = {'state': state, 'service':service}
# Guardamos el resultado en un archivo json
with open('scan_results_json', 'w') as f:
    json.dump(results, f)
# Mostramos los resultados por consola y lo guardamos en un archivo txt
with open('scan_results.txt', 'w') as f:
    for host in results:
        print(f'host: {host}\n')
        f.write(f'host: {host}\n')
        for port in results[host]:
            state = results[host][port]['status ']
            service = results[host][port]['service']
            print(f' Puerto {port}: {state} {{service}}\n')
            f.write(f' Puerto {port}: {state} {{service}}\n')

# Pedimos que se introduzca una IP
ip = input('Introduce la IP: ')

# Escaneamos la IP, mostramos y guardamos
scan_ip(ip)