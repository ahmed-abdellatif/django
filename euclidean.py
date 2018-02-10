'''
* Euclid's Algorithm & finding modular inverse
* gcd(m, n) = gcd(n, m mod n)
*-------------------------------------------------
* Euclid's Algorithm:-> def Euclid
* Here we use modular arithmetic 
* for choosing valid keys
*--------------------------------------------------
* Reversing Euclid's Algorithm:-> def ReverseEuclid
* For the purpose of decrypting
* 
*-------------------------------------------------
'''


''' Euclid's algorithm: Computes the gcd(m, n) 
*-- by using Euclid’s algorithm 
*-- Output: Greatest common divisor of m and n
'''
def Euclid(m, n):
	while m != 0:
		m, n = n % m, m
	return n


''' Euclid's Extended Algorithm: ax + by = gcd(a,b)
*-- can be viewed as the reciprocal of modular exponentiation
*-- we are reversing the steps in the Euclidean algorithm
'''
def ReverseEuclid(m, x):

    if Euclid(m, x) != 1:
        return None 

    q1, q2, q3 = 1, 0, m
    r1, r2, r3 = 0, 1, x
    while r3 != 0:
        u = q3 // r3 
        r1, r2, r3, q1, q2, q3 = (q1 - u * r1), 
        (q2 - u * r2), (q3 - u * r3), r1, r2, r3
    return q1 % x

