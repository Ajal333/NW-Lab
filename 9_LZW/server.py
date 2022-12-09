

def compress(message):
    tableSize = 256
    table = {chr(i):i for i in range(tableSize)}
    p = ""
    result = []
    for c in message:
        d = p+c
        if(d in table):
            p = d
        else:
            result.append(table[p])
            table[d] = tableSize
            tableSize += 1
            p = c
    if(p): 
        result.append(table[p])
    return result

def decrypt(message):
    tableSize = 256
    table = {i:chr(i) for i in range(tableSize)}
    p = ""
    result = ""
    for code in message:
        if(not(code in table)):
            table[code] = p + p[0]
        result += table[code]
        if(not(len(p) == 0)):
            table[tableSize] = p + table[code][0]
            tableSize += 1
        p = table[code]
    return result


def main():
    str = input("Enter a string: ")
    compressedValue = compress(str)
    print(f"Compressed: {compressedValue}")
    d = decrypt(compressedValue)
    print(f"Decompressed: {d}")

main()