

def compressor(message):
    tableSize = 256
    table = {chr(i):i for i in range(tableSize)}
    p=""
    result = []
    for c in message:
        d = p + c
        if(d in table):
            p = d
        else:
            result.append(table[p])
            table[d] = tableSize
            tableSize += 1
            p=c

    if p: 
        result.append(table[p])
    return result

def decompressor(message):
    tableSize = 256
    table = {i: chr(i) for i in range(tableSize)}
    p = ""
    result = ""
    for code in message:
        if not (code in table):
            table[code] = p + p[0]
        result += table[code]
        if(not(len(p) == 0)):
            table[tableSize] = p + table[code][0]
            tableSize += 1
        p = table[code]
    return result

def main():
    st = input("Enter the string: ")
    c = compressor(st)
    d = decompressor(c)
    print(f"Compressed: {c}")
    print(f"Decompressed: {d}")

main()



