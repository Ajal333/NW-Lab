from socket import socket

PORT =  3003
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

_s = socket()

_s.connect(ADDR)

def xor(a,b):
    result = []
    for i in range(1, len(b)):
        if(a[i] == b[i]):
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


def mod2div(message, key):
    keyLen = len(key)
    b = message[0:keyLen]
    while keyLen < len(message):
        if(b[0] == "1"):
            b = xor(key, b) + message[keyLen]
        else:
            b = xor("0"*(keyLen), b) + message[keyLen]
        keyLen += 1
    if(b[0] == "1"):
            b = xor(key, b) 
    else:
            b = xor("0"*(keyLen), b) 
            
    return b



def encode(message, key):
    keyLen = len(key)
    newMessage = message + "0"*(keyLen-1)
    rem = mod2div(newMessage, key)
    ct = message + rem
    return ct

def main():
    key = "1001"
    message = input("Enter the string: ")
    fMessage = "".join(format(ord(i), "b") for i in message)
    ct = encode(fMessage, key)
    _s.send(ct.encode())
    result = _s.recv(1024).decode()
    print(f"result: {result}")

main()