from socket import socket
import math

PORT = 8000
HOST = ""

ADDR = (HOST, PORT)

_s = socket()
_s.bind(ADDR)

KEY = "ABCD"

_s.listen(1)

def decrypt(message):
    col = len(KEY)
    row = int(math.ceil(len(message)/col))

    msgIdx = 0
    kidx = 0
    keyList = sorted(list(KEY))

    mlist = list(message)

    decipher = []

    for _ in range(row):
        decipher +=  [[None] * col]

    for _ in range(col):
        currIdx = KEY.index(keyList[kidx])
        for j in range(row):
            decipher[j][currIdx] = mlist[msgIdx]
            msgIdx += 1
        kidx += 1

    msg = "".join(sum(decipher, []))

    nullCnt = msg.count("_")

    if(nullCnt > 0): return msg[:-nullCnt]

    return msg



def main():
    client, addr = _s.accept()
    message = client.recv(1024).decode()
    pt = decrypt(message)
    print(f"PT: {pt}")
    client.close()

main()