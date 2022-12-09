# import socket

from socket import socket

PORT = 3000
HOST  = "127.0.0.1"

ADDR = (HOST, PORT)

sock = socket()

sock.connect(ADDR)

data = sock.recv(1024).decode()

print(f"The data recieved is: {data}")

sock.close()