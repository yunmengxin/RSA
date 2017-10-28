# coding:utf-8
import random
import Prime


# encryption ,according to the formula:m^e = c (mod n) , calculate c ,c == secret,m == message
def encryption(message, puk):
    return Prime.quick_pow_mod(message, puk[1], puk[0])


# decryption ,according to the formula:c^d = m (mod n),  calculate m ,
def decryption(secret, prk):
    return Prime.quick_pow_mod(secret, prk[1], prk[0])


def get_RSAKey():
    RSAKey = {}
    prime_arr = Prime.get_rand_prime_arr(2)
    p = prime_arr[0]
    q = prime_arr[1]
    while p == q:
        q = random.choice(prime_arr)
    n = p * q
    s = (p - 1) * (q - 1)
    e = 65537
    d = Prime.mod_inverse(e, s)
    print "p = ", p, ",q = ", q
    print "n = ", n
    print "e = ", e, ",d = ", d
    puk = [n, e]
    prk = [n, d]
    RSAKey['puk'] = puk
    RSAKey['prk'] = prk
    return RSAKey


if __name__ == '__main__':
    RSAKey = get_RSAKey()
    print "Enter a number less and shorter than ", len(str(RSAKey['puk'][0])), ",", RSAKey['puk'][0], ":"
    # only encrypt a number type
    message = int(input())
    secret = encryption(message, RSAKey['puk'])
    print "After the encryption data :", secret
    print len(str(secret))
    message = decryption(secret, RSAKey['prk'])
    print "After the decryption data :", message
    print len(str(message))