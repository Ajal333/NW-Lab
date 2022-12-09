from socket import socket, AF_INET, SOCK_DGRAM

PORT = 3000
HOST = ''

ADDR = (HOST, PORT)

_s = socket(AF_INET, SOCK_DGRAM)
_s.bind(ADDR)

while True:
    data, client = _s.recvfrom(1024)

    print(f"message from {client}: {data.decode()}")
