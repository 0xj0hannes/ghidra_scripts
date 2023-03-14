n = 8 # the logarithm of 256 base 2 is 8

def KSA(key):
    index = 0
    ISV = range(2**n) #The initial state vector array

    for i in range(len(ISV)):
        index = (index + ISV[i] + key[i % len(key)]) & 0xFF
        ISV[i], ISV[index] = ISV[index], ISV[i]

    return ISV

def PRGA(ISV, enc):
    key_stream = []
    x = 0
    y = 0
    index = 0

    for i in range(len(enc)):
        x = (x + 1) & 0xFF
        y = (y + ISV[x]) & 0xFF
        ISV[x], ISV[y] = ISV[y], ISV[x]
        index = (ISV[x] + ISV[y]) & 0xFF
        key_stream.append(ISV[index])

    return key_stream

def decrypt(encrypted_text, key_stream):
    for i in range(len(encrypted_text)):
        encrypted_text[i] ^= key_stream[i]

    return bytes(encrypted_text)

def input():
    global key
    global enc
    key_addr = askAddress('what is the key address?', 'address')
    enc_addr = askAddress('what is the encrypted text address?', 'address')
    key_size = askInt('what is the key size?', 'size in decimal')
    enc_size = askInt('what is the encrypted text size?', 'size in decimal')
    key = getBytes(key_addr, key_size)
    enc = bytearray(getBytes(enc_addr, enc_size))
    print("key: {}".format(key))
    print("enc: {}".format(enc))

def rc4():
    input()
    ISV = KSA(key)
    key_stream = PRGA(ISV, enc)
    data = decrypt(enc, key_stream)

    return data

def main():
    data = rc4()
    print("decrypt row data: {}".format(repr(data)))
    print("decrypted data: {}".format(data))

if __name__ == '__main__':
    main()

    



