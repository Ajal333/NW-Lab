import socket
from _thread import *
import sys

clientNames = {}
clientList = []

PORT = 3000
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

def sendToAll(message, sender):
    for client in clientList:
        if(client != sender):
            client.send(message.encode())

def handleClient(client, addr):
    name = client.recv(1024).decode()
    print(name)
    while True:
        message = client.recv(1024).decode()
        if message:
            print(message)
            sendToAll(message, client)


def main():
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _s.bind(ADDR)
    _s.listen(100)

    while True:
        client, addr = _s.accept()
        name = client.recv(1024).decode
        clientNames[addr[0]] = name
        clientList.append(client)

        print("Client connected")
        start_new_thread(handleClient, (client, addr))



main()