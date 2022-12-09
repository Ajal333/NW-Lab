from socket import socket

PORT =  3001
HOST = ""

ADDR = (HOST, PORT)

_s = socket()

_s.bind(ADDR)

_s.listen(1)

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



def decode(message, key):
    keyLen = len(key)
    newMessage = message + "0"*(keyLen-1)
    rem = mod2div(newMessage, key)
    return rem

def main():
    client, _ = _s.accept()
    key = "1001"
    message = client.recv(2048).decode()
    rem = decode(message, key)
    print(f"rem: {rem}")
    if(rem == ("0"*(len(key) -1))):
        client.send("Accepted".encode())
    else: 
        client.send("Rejected".encode())

main()