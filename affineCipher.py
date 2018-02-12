'''
*********************************************************************************
* The affine cipher is a type of monoalphabetic substitution cipher, 
* wherein each letter in an alphabet is mapped to its numeric equivalent, 
* encrypted using a simple mathematical function, and converted back to a letter.
*********************************************************************************
'''
import sys, pyperclip, euclidean, random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front


def main():
    message = """"Your job is being a professor and researcher: That's one hell of a good excuse for some of the brain-damages of Minix." -Linus Torvalds"""
    key = 1901
    mode = 'encrypt' 

    if mode == 'encrypt':
        translated = encrypt(key, message)
    elif mode == 'decrypt':
        translated = decrypt(key, message)
    print('Key: %s' % (key))
    print('%sed text:' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (mode))


def getKeyParts(key):
    key_a = key // len(SYMBOLS)
    key_b = key % len(SYMBOLS)
    return (key_a, key_b)


def checkKeys(key_a, key_b, mode):
    if key_a == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if key_b == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(key_a, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (key_a, len(SYMBOLS)))


def encrypt(key, message):
    key_a, key_b = getKeyParts(key)
    checkKeys(key_a, key_b, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * key_a + key_b) % len(SYMBOLS)]
        else:
            ciphertext += symbol 
    return ciphertext


def decrypt(key, message):
    key_a, key_b = getKeyParts(key)
    checkKeys(key_a, key_b, 'decrypt')
    plaintext = ''
    modInverseOfkey_a = cryptomath.findModInverse(key_a, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - key_b) * modInverseOfkey_a % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext


def getRandomKey():
    while True:
        key_a = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(key_a, len(SYMBOLS)) == 1:
            return key_a * len(SYMBOLS) + key_b

# main() function.
if __name__ == '__main__':
    main()