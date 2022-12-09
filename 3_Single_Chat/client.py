from socket import socket, gethostname, gethostbyname
import threading

PORT = 3002
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

HOSTADDR = gethostname()
HOST_IP = gethostbyname(HOSTADDR)

sock = socket()

sock.connect(ADDR)

print(f"User address: {HOSTADDR}")
print(f"Your ip: {HOST_IP}")

name = input("Enter you name: ")
sock.send(name.encode())

serverName = sock.recv(1024).decode()

def sendMessage():
    while True:
        message = input(f"\n<{name}: ")
        if (message == "exit"):
            sock.close()
        else:
            sock.send(message.encode())

def recieveMessage():
    while True:
        message = sock.recv(1024).decode()
        print(f"\n<{serverName}>: {message}")
        if(message == "exit"):
            sock.close()

thread1 = threading.Thread(target=sendMessage)
thread1.start()

thread2 = threading.Thread(target=recieveMessage)
thread2.start()


