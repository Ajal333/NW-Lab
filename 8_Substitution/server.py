from socket import socket
from string import ascii_lowercase

PORT = 3000
HOST = ''

ADDR = (HOST, PORT)

_s = socket()

_s.bind(ADDR)

_s.listen(1)

def decrypt(message, key):
    alph = ascii_lowercase
    decodedMessage = ""
    for i in message:
        if i == " ":
            decodedMessage += i
        else:
            decodedMessage += alph[(alph.index(i) - key) % 26]
    return decodedMessage


def main():
    while True:
        client, addr = _s.accept()

        pt = client.recv(1024).decode()
        if(not pt): break
        message, key = pt.split(";")

        print(f"DecryptedMessage: {decrypt(message, int(key))}")

        client.close()
        break

main()