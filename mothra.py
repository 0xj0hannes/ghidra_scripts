from struct import unpack

N = 8
def KSA(key):
    index = 0
    ISV = range(2**N) #The initial state vector array

    for i in range(len(ISV)):
        index = (index + ISV[i] + key[i % len(key)]) & 0xFF
        ISV[i], ISV[index] = ISV[index], ISV[i]

    return ISV

def PRGA_and_XOR(enc, ISV):
    x = 0
    y = 0
    index = 0

    for i in range(len(enc)):
        x = (x + 1) & 0xFF
        y = (y + ISV[x]) & 0xFF
        ISV[x], ISV[y] = ISV[y], ISV[x]
        index = (ISV[x] + ISV[y]) & 0xFF
        enc[i] ^= ISV[index]

    return bytearray(enc)

def rc4(enc, key):
    ISV = KSA(key)
    return PRGA_and_XOR(enc, ISV)

key = getBytes(toAddr(0x00416000), 0x4)
enc = bytearray(getBytes(toAddr(0x00416008), 0x146))

data = rc4(enc, key)

print("decrypted data: {}".format(repr(data)))
print("hostname: {}".format(data[:128]))
print("port: {}".format(unpack("<h", str(data[128:130]))[0]))
print("path: {}".format(data[130:258]))
print("rc4key: {}".format(data[258:322]))
print("sleep_sec: {}".format(unpack("<i", str(data[322:326]))[0]))

    



