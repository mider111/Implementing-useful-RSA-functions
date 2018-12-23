# Implementing-useful-RSA-functions
Implementation of the following five functions:
modarithmetic.py 
• gcd(a,b) takes two positive integers of input, and returns a tuple of three integers (d,s,t) where
d is the gcd of a and b, and sa+tb=d.
• expMod(b,x,n) computes bx mod n.
• isPrime(p,k) performs k iterations of Fermat’s primality test on the input p

keygen.py 
• randprime(mn,mx) returns a random prime between mn and mx
• keygen(mn,mx) return a tuple of three integers that makes up an RSA key: (n,e,d), where n
is the product of two different primes between mn and mx, e is the public exponent, and d is
the secret key.

