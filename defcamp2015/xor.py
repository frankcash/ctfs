from binascii import hexlify, unhexlify

import re
import sys

ciphertexts = ["f363844fd41932070e24df7f6c2397b4f0ee4bc567c32e6f8be4665116657ff880756558fe63f47975fa94e8fa1efc6e97cf9c99931ce21d7b03ef4f61bdc6f74fc566cac6f0fe7b939237d3ab9e37adf9910cfc899ed3ff7b79ead95b8aced21ec1079c72409e878425fd61026fbf1e9319ff6dc4c75c356f04ffe204ce480c488ff34eb78034aa23d87309", "d12a9b49d446354e0020912f6f2297b7eaee4f8062c32479d2f66253016b6ab182723152ff69a46178ebd1e5e04ae760978b9c929319ab0a6018b70a5bf5d6b946d27ad8d9e3f9769b923dc9fb953db2b7d816f1889ecbf86a3cbec45e8aced213c44ebd5275cad3d72ef9631f72a15b8f57f123cac412742e03b6fb098b1c350d9bf25db78023ab3690751276f46d9e598a1f0b", "c4629107da0e38541937d43e6366dab7eaff1cc266c32879c5e06440106f63b18e7b7c41fc61a06871e694e8ed4ae760978b9c92930aab19614cf85e2ff1d6f85ec323dfc5f4bc6497df319ab7933cb8a1d958f59f9ec8f97b74eedc578680d61add53f3477ed687942bfe6a1972f2198519e170ced412786105bab618c309340d92f34cbf", "c4629d549106204c0836912b662397b1e0f848c56ec33979d9fc3642116765f49f677e5cf524a0623df6d9f9f50ff864979bd396dd5db21f680fed436cf89fb94cd9678bcce2bc76d6c031c9ae9a26ffa1d91db483d0d9bc6a3df3d5169f8fc65fcd46a0067eddd3d728f5611826a512845cf87a8bc541706a5bfff314c80d2a59ddfb40a88023ab36907b1475e8288f5f86131689d8606623e1629bca36e38a53608b88", "d12a8753c30e204a4d26d82f6623c5e2f4ea57c570c33a6fcea57947446b27fc98777911e369b56171fac6a9f804f1219480819a931ead037f09f7436af3c7b946d27a8bdee4ff7fd6d3279aeac46affb7d80ce7c29efef06d31fa905981ced617cc54f34d75cb8bd723e4241163bc1e9258e066d89053357e04bae308c41a3b4399f242facb32ba20c4641e67f1", "d12a8753c30e204a4d26d82f6623c5e2feee52c571823b79d8a56554076962e29e7d6754b061b86870fadafdea4afa67d99b9b9a9316a7147a18eb4f6ef093fb4cc466cf8dfef23797dc74d3b58237adbbd014b49fcadde57b", "d964d446911838490e2dc3306029c2b1b9f848d26682223cc8ec6649017827f0cd676543f565b92d72f994f9ea0fe06596c2819edd19ad002908f04d66e9c0b944c423ccc8fff96597c631defb9f3cbbb0c11dfa88dbd2e5722dbedf50cf9aca1a8557bf4779dcd39232e4241768b65b8350e46bcec246707603fffb09d81b3b4a98ee03fac139a773c47e1e68bc6b83408d0e118fdd2c312be57ad7d73de7de4a638492956d6ecc9d", "d96cd807d90436421b20c3732e2797a6f0ec55d4238a3c3cc8ea6453117a73f48934785fb070a66c73ecd9e0ea19fc6e97c3d38dd209aa087b4ced426ef393f849d366cf8dfeee379add27cef7d63db1b9c858f5cccdd5ff7938fb90528689cb0b854ebd0664dac2d73afc651f68a61e984db46ad89053736812bce209cf483b4399bd5bb2c577a621c2790926f867895ecf09109e997c342de17390c221e7de4e60c5948f716ec6c9c6322151f9dbb8fe9f411876eb04576524f3f4d6", "d1649b53d90e33070c35c12d6127d4aab9fe4fc570c33c79dde06440082a68f7cd607954b074a6686bf6dbfcea4adb219a868397d60fb6087118b94e66fadaed5e9777c48df2f37a86c720dffb823abaf5da1ded9fcacef47f39b090659a8dca5fd644bb437dd7d4d72be261566dbc149757b462d89041706211f2e515c50b325f92f346a0c939a473c3620963fd65cc4e8617178fcb7f", "d2639a46c31261541937d43e6366d4abe9e359d270c32e6ecea57947106f69b18e7b7f42e476a16e69fad0a9ec19fc6f9ecf9f96dd18a31f290afc4f6bffd2fa469770c3c4f7e83784d733d3a88237ada6911af18fdfc9e27b74ead85396cec11ecb07b14330d7c68423fc7d566fbf0b8c5cf966c5c457712e1eb1b604ca1a3e5a9cef4afac139a773d3771526fe6dcc5f8a061b83d5756623ff739bda26e79a1a62848f937c66d59ddf303249e682"]

target = "c7629149911e324e0322913e2e35c3b0fcea5180608a3f74cef73a010a6f71f49f346442f524a06578bfdfece04af86e8b8ad38bdb1cac4d6602fa4f2e"
# def xor(data, key):
#     return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))
#
#
#


line1 = "d12a8753c30e204a4d26d82f6623c5e2feee52c571823b79d8a56554076962e29e7d6754b061b86870fadafdea4afa67d99b9b9a9316a7147a18eb4f6ef093fb4cc466cf8dfef23797dc74d3b58237adbbd014b49fcadde57b"
line2 = "d12a8753c30e204a4d26d82f6623c5e2f4ea57c570c33a6fcea57947446b27fc98777911e369b56171fac6a9f804f1219480819a931ead037f09f7436af3c7b946d27a8bdee4ff7fd6d3279aeac46affb7d80ce7c29efef06d"


def xor(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def main(idx):
    x = strxor(unhexlify(ciphertexts[idx]), unhexlify(target))
    print "Ciphertext[%s] xor Target\n" % str(idx)
    # crib = raw_input("Enter Crib:>")
    crib = "when using "
    print "Crib\n~%s~" % crib

    # Crib Drag
    for i in range(len(x)):
        z = x[i:]
        print "\n[%d]" % i
        print "%s" % strxor(z, crib)


# def stream_cipher_attack():
#     res = xor(line1, line2)
#     print("res: " + res)
#     plaintext = str(res)
#     print("plaintext: " + plaintext)
#
#     print("xor line1 and res: " + xor(line1, res))
#
#     print("xor line1 and dctf:  " + xor(line1, "dctf{}"))
#
#     print("xor res and dctf:  " + xor(res, "dctf{}"))



if __name__ == "__main__":
    # stream_cipher_attack()
    for idx, cipher in enumerate(ciphertexts):
        main(idx)

    # main(9)
