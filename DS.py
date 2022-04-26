'''
Developer : Aminah Abdullah Albuainain
ID : 219003367
This code build for course requirement " Applied Cryptography " Assignment 1
Note that I use multiple source to build this code
So best thank for them to share their knowledge
Credit :
(1) https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html
(2) https://www.ques10.com/p/33840/rsa-digital-signature-scheme/?#:~:text=RSA%20idea%20is%20also%20used,called%20RSA%20digital%20signature%20scheme.&text=Sender%20uses%20her%20own%20private,function%2C%20but%20with%20different%20parameters.
(3) https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/digital-signatures/rsa-sign-verify-examples.html



'''

from Cryptodome.PublicKey.RSA import *
from hashlib import sha512
import textwrap
from colorama import Fore, Back, Style

def digitalSign ():
    # Genrate pair of RSA key with len 1024
    keyPair = generate(bits=1024)

    # jsut we wrapp output to have good view
    # print public pair (n, e) and private pair (n , d)

    wrapper = textwrap.TextWrapper(width=65)
    warpN = wrapper.wrap(text=str(hex(keyPair.n)))
    wrapD= wrapper.wrap(text=str(hex(keyPair.d)))
    print(f"Public key: n=")
    for i in warpN :
        print(i)
    print(f"Public key : e = {hex(keyPair.e)} ")

    print("")
    print(65*"-")
    print(f"Private key: n=")
    for i in warpN :
        print(i)
    print(f"Private key: d=")
    for i in wrapD :
        print(i)

    # Input message to hash then encrypted
    plain = input("ENTER MESSAGE TO SIGN IN  ")
    msg =plain.encode()

    # create hash with SHA512
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

    # Signing throughout encrypt hash with ** PRIVATE KEY (d)**
    sign = pow(hash, keyPair.d, keyPair.n)
    warpSign = wrapper.wrap(text=str(hex(sign)))
    print(65*"-")
    print("Signature:")
    for i in warpSign :
        print(i)

    print(65*"-")


    # Vefier will decrypt Sign using ** PUBLIC KEY (e) *** and compare it with message hash
    plain = input("ENTER MESSAGE TO VERIFY  ")

    msg =plain.encode()


    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    # Encrypt
    hashFromSignature = pow(sign, keyPair.e, keyPair.n)

    # Compare
    if (hash == hashFromSignature) :
        print(Fore.GREEN+"Signature valid:")
    else :
        print(Fore.RED+"Signature not valid:")
