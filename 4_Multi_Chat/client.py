import socket
import _thread
import sys, select

PORT = 3000
HOST = "127.0.0.1"

ADDR = (HOST, PORT)



def main():
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.connect(ADDR)
    name = input("Enter you name")
    _s.send(name.encode())
    while True:
        socketList = [sys.stdin, _s]
        rList, wList, errList = select.select(socketList, [],[])
        for sock in rList:
            if(sock == _s):
                message = sock.recv(1024).decode()
                if message:
                    print(message)
            else:
                message = sys.stdin.readline()
                _s.send(message.encode())
                sys.stdout.write("You: ")
                sys.stdout.write(message)
                sys.stdout.flush()

main()
