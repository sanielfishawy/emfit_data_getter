#pylint: disable=invalid-name
from socket import socket, AF_INET, SOCK_DGRAM

class EmfitIpFinder:

    UDP_PORT = 30371
    TIMEOUT = 20 # seconds

    def __init__(self):
        pass


    def get_ip(self):
        udp_sock = socket(AF_INET, SOCK_DGRAM)
        udp_sock.bind(('', EmfitIpFinder.UDP_PORT))
        udp_sock.settimeout(EmfitIpFinder.TIMEOUT)

        try:
            message = udp_sock.recvfrom(1024)
        except OSError as error:
            print(error)
            raise DeviceNotFoundError('Emfit not found on local network.')

        udp_sock.close()
        return message[1][0]

class DeviceNotFoundError(Exception):
    '''Raised when Emfit not found on the network'''

if __name__ == '__main__':
    eif = EmfitIpFinder()
    try:
        ip = eif.get_ip()
    except DeviceNotFoundError as error:
        print(error)
    else:
        print(f'ip: {ip}')
