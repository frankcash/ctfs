line1 = "d12a8753c30e204a4d26d82f6623c5e2feee52c571823b79d8a56554076962e29e7d6754b061b86870fadafdea4afa67d99b9b9a9316a7147a18eb4f6ef093fb4cc466cf8dfef23797dc74d3b58237adbbd014b49fcadde57b"
line2 = "d12a8753c30e204a4d26d82f6623c5e2f4ea57c570c33a6fcea57947446b27fc98777911e369b56171fac6a9f804f1219480819a931ead037f09f7436af3c7b946d27a8bdee4ff7fd6d3279aeac46affb7d80ce7c29efef06d"

def xor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))


def stream_cipher_attack():
    res = xor(line1, line2)
    print("res: " + res)
    plaintext = str(res)
    print("plaintext: " + plaintext)

    print("xor line1 and res: " + xor(line1, res))

    print("xor line1 and dctf:  " + xor(line1, "dctf{}"))

    print("xor res and dctf:  " + xor(res, "dctf{}"))



if __name__ == "__main__":
    stream_cipher_attack()
