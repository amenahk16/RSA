'''
Developer : Aminah Abdullah Albuainain
ID : 219003367
This code build for course requirement " Applied Cryptography " Assignment 1
Note that I use multiple source to build this code
So best thank for them to share their knowledge
Credit :
(1) https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html
(2) https://inventwithpython.com/rabinMiller.py

'''


import random
import math
import textwrap
import DS
from colorama import Fore, Back, Style

def fillEculidanTable (a,b ) :

   # Here I have already built this code same as solving EEA in table

        flag = True
        table = []

        a = a
        b = b
        r = a % b
        q = math.floor(a / b)
        templist = [a, b, r, q]
        table.append(templist)
        i = 0

        u=[1,0]
        v=[0,1]

        while (flag == True) :
            if (r==0) :
                flag =False
            else:
                v.append(v[i] - (v[i + 1] * q))
                u.append(u[i] - (u[i + 1] * q))
                i+=1
                a=b
                b=r
                r=a%b
                q = math.floor(a / b)
                templist = [a, b, r, q]
                table.append(templist)

        return v[len(v)-1]
def millerRaben(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False  # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than millerRaben().
    quickPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                   59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                   127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                   191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                   257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                   331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                   401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
                   467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
                   563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
                   631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                   709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                   877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953,
                   967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031,
                   1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
                   1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171,
                   1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291,
                   1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373
        , 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493,
                   1499, 1511
        , 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627,
                   1637, 1657
        , 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789,
                   1801, 1811
        , 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973,
                   1979, 1987
        , 1993, 1997, 1999, 2003, 2011]

    if num in quickPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in quickPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    return millerRaben(num)
def generatePrime(bit=1024):
    # Return a random prime number of keysize bits in size.
    while True:
        num = random.randrange(pow(2,(bit-1)), pow(2,(bit)))
        if isPrime(num):
            return num
def extendEculidAlgo (n, e):
# We fill table by calling function
    result = fillEculidanTable(n, e)
# If result is negative then take mod of n
    if result < 0:
        result = result % n
# Verfiy it's inverse
    if (math.gcd(n, e) == 1):
       print("")

# Else given number have no inverse
    else:
        print("Inverse not applicable ")

    return result
def findExpo(phi):
    for i in range(2, phi):
        if (math.gcd(i, phi) == 1):
            return i

        # Ask user the length required for prime number
def encDec() :
    # ensure no zero given try and catch block
    bit = input("Enter the Length of the Prime Number that would be Generated"
                + " \nNote: The higher length the more secure and time consuming")
    bit = int(bit)
    #validate user input
    while (bit <1 ):
        bit = input("Enter the Length of the Prime Number that would be Generated"
        + " \nNote: The higher length the more secure and time consuming")
        bit = int(bit)
    #genrate two prime number
    p = generatePrime(bit)
    q = generatePrime(bit)

    # ensure p ! = q otherwise try again to find different q
    while (q == p): q = generatePrime(bit)

    #find n, phi , e, d by calling previous function that explained
    n = p * q
    phi = (q - 1) * (p - 1)
    e = findExpo(phi)
    d = extendEculidAlgo(phi, e)

    # wrap output to have nice look
    wrapper = textwrap.TextWrapper(width=43)
    wrappP = wrapper.wrap(text=str(p))
    wrappQ = wrapper.wrap(text=str(q))
    wrappPhi = wrapper.wrap(text=str(phi))
    wrappN = wrapper.wrap(text=str(n))


    #start Bob dialog
    print(20 * "-" + " Bob (Owner) " + 20 * "-")
    print("Genrated p = ")
    for i in wrappP:
        print("  " + i)
    print("")
    print("Genrated q = ")
    for i in wrappQ:
        print("  " + i)

    print("")
    print("Genrated Φ phi  =(p-1)*(q-1) ")
    for i in wrappPhi:
        print("  " + i)
    print("choos e = ")
    print(str(e))
    print("generated d =" + str(d))

    print("")
    print("Transmit e , n to Alice to use it in encryption" + " ." * 8)
    print("")

    # start Alice dialog
    print(20 * "-" + " Alice " + 20 * "-")
    print("received n = ")
    for i in wrappN:
        print("  " + i)

    print("")
    print("received e = ")
    print(str(e))

    #Give user chance to enc/dec
    plain = input("Assume you are Alice what kind of message to you want to encrypt ? ")
    cipher = []

    for i in plain:
        cipher.append(str(pow(ord(i), e) % n))

    print("Generated Cipher : ")
    print("".join(cipher))

    print(20 * "-" + " Bob (Owner) " + 20 * "-")
    print("Now Bob want to verify and decrypt message from Alice")
    print("He received this cipher text")
    print("".join(cipher))

    plainAfterEnc = []
    for i in cipher:
        plainAfterEnc.append(chr((pow(int(i), d)) % n))
    print("Decrypted Message :  ")
    print("".join(plainAfterEnc))




##########################################################################################
# Main dialogue will contain all RSA usage and let user choose
    # 1) Encrypt / Decrypt
    # 2) Signing And Verifying
    # 0) Exit

##########################################################################################
print("-"*65)
c = input("Hello to RSA world, We have many usage for RSA which would you like to try ?\n1)Encrypt/Decrypt \n2)Signing And Verfiying \n0)Exit")
#Ensure valid entery
try :
    c = int(c)
    while(c!=0) :
        if(c==1):
            encDec()
        elif(c==2):
            DS.digitalSign()
        else:
            print("not valid entery ! ")

        c = input(Style.RESET_ALL+"Hello to RSA world, We have many usage for RSA which would you like to try ?\n1)Encrypt/Decrypt \n2)Signing And Verfiying \n0)Exit")
        c=int(c)

except :
    print("not valid entery ! ")







