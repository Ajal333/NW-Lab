# import socket
from socket import socket

PORT = 3000

ADDR = ('', PORT)

sock = socket()

sock.bind(ADDR)

sock.listen(3)

while True:
    client, addr = sock.accept()

    print(f"Connected to {addr}")

    client.send("Thank you for connecting.".encode())

    client.close()

    break