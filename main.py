# https://docs.python.org/es/3/library/ipaddress.html
import ipaddress

def get_info_ipaddress(id_red):
    ip = ipaddress.IPv4Network(id_red)
    print(f'La mascara de subred es: {ip.netmask}')
    print(f'La mascara de wildcard es: {ip.hostmask}')
    print(f'La primera direcion valida es: {ip.network_address + 1}')
    print(f'La ultima direcion valida es: {ip.broadcast_address - 1}')
    print(f'La direcion de broadcast es: {ip.broadcast_address}')
    print(f'Es una direcion Privada: {ip.is_private}')
    print(f'Cantidad de direciones IP Validas: {ip.num_addresses - 2}')

    resp = input("ingrese 'SI' si quiere conocer las IP validas: ")
    resp = resp.upper()

    if ( resp == 'SI' ):
        for i, host in enumerate(ip.hosts()):
            print(f'{i + 1}: {host}')

def print_subnet_list(ip_subnet):
    for i in ip_subnet:
        print(i)

def info_subnet(id_red):
    # ip = ipaddress.IPv4Network(id_red)
    num_subnets = int(input('Ingrese la cantidad de subredes: '))
    num_subnets = num_subnets - 2
    if (num_subnets <= 0):
        ip_subnet = ipaddress.IPv4Network(id_red).subnets()
    else:
        ip_subnet = ipaddress.IPv4Network(id_red).subnets(prefixlen_diff=num_subnets)

    # print_subnet_list(ip_subnet)

    for i in ip_subnet:
        resp = input(f"ingrese 'SI' si quiere conocer la information de la subred: {i} ")
        resp = resp.upper()
        if ( resp == 'SI' ):
            get_info_ipaddress(i)

if __name__ == '__main__':
    id_red = input('Ingrese la direcion de red y el prefijo: ')
    # info_subnet(id_red)
    get_info_ipaddress(id_red)

