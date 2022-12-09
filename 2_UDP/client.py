from socket import socket, AF_INET, SOCK_DGRAM

PORT = 3000
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

for i in range(10):
    _s = socket(AF_INET, SOCK_DGRAM)

    message = f"Hello from client {i}".encode()

    _s.sendto(message, ADDR)

    print(f"Message sent to server {i}")

    try:
        data, server = _s.recvfrom(1024)
        print(f"Server send back: {data.encode()}")
    except:
        print(f"Request timeout for {i}")