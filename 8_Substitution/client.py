from socket import socket
from string import ascii_lowercase

PORT = 3000
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

_s = socket()

_s.connect(ADDR)

def encrypt(message, key):
    alph = ascii_lowercase
    encodedMessage = ""
    for i in message:
        if i == " ":
            encodedMessage += i
        else:
            encodedMessage += alph[(alph.index(i) + key) % 26]
    return encodedMessage


def main():
    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    print(f"Sending message after encryption: {encrypt(message, key)};{key}")
    _s.send(f"{encrypt(message, key)};{key}".encode())
    _s.close()

main()