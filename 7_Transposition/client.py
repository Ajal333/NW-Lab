from socket import socket
import math

PORT = 8000
HOST = "127.0.0.1"

ADDR = (HOST, PORT)

_s = socket()
_s.connect(ADDR)

KEY = "ABCD"

def encrypt(message):
    col = len(KEY)

    ct = ""
    kidx = 0
    keyList = sorted(list(KEY))
    mlen = float(len(message))
    row = int(math.ceil(mlen/col))
    mlist = list(message)

    nullChar = int((row*col) - mlen)
    mlist.extend("_"*nullChar)
    matrix = [mlist[i:i+col] for i in range(0, len(mlist), col)]

    for _ in range(col):
        currIdx = KEY.index(keyList[kidx])
        ct += "".join([row[currIdx] for row in matrix])
        kidx += 1

    return ct



def main():
    message = input("Enter the string: ")
    ct = encrypt(message).encode()
    print(f"CT: {encrypt(message)}")
    _s.send(ct)
    _s.close()

main()