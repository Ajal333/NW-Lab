from socket import socket, gethostname, gethostbyname
import threading

PORT = 3002
HOST = ""

ADDR = (HOST, PORT)

sock = socket()

sock.bind(ADDR)

HOSTADDR = gethostname()
HOST_IP = gethostbyname(HOSTADDR)

print(f"User address: {HOSTADDR}")
print(f"Your ip: {HOST_IP}")


name = input("Enter you name: ")
sock.listen(1)

client, addr = sock.accept()

client.send(name.encode())

clientName = client.recv(1024)
print(f"Client connected: {clientName.decode()}")

def sendMessage():
    while True:
        message = input(f"\n<{name}: ")
        if(message == "exit"):
            client.close()
        else:
            client.send(message.encode())

def recieveMessage():
    while True:
        message = client.recv(1024).decode()
        print(f"<{clientName}>: {message}")
        if(message == "exit"):
            client.close()

thread1 = threading.Thread(target=sendMessage)
thread1.start()

thread2 = threading.Thread(target=recieveMessage)
thread2.start()


