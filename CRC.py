def xor(a, b):
    result = ""
    for i in range(len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

data = "1101011011"
key = "10011"

print("Original Data: ", data)
codeword = encodeData(data, key)
print("Encoded Data (Data + CRC): ", codeword)
