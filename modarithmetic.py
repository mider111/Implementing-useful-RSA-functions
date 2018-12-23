from random import randint

# function extGCD
# inputs: two integers x,y
# outputs: three integers: d,s,t such that
#   d = gcd(x,y)
#   sx + ty = d
def extGCD(x, y):
    s, x1, t, y1 = 1, 0, 0, 1
    while y != 0:
        q, x, y = x // y, y, x % y
        s, x1 = x1, s - q * x1
        t, y1 = y1, t - q * y1
    return  x, s, t


# function expMod
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
def expMod(b,e,n):
    B = b
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            B = (B * B) % n
            E = E/2
        else:
            Y = (B * Y) % n
            E = E - 1
    return Y


# function expModSlow
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
def expModSlow(b,e,n):
    x = 1
    for i in range(e):
        x *= b
        x %= n
    return x


# function isprime(p,k)
# input: a positive integer p and a positive integer k
# output: true if p is (probably) prime, false otherwise.
def isprime(p,k):
    if p == 2:
        return True

    if p % 2 == 0:
        return False

    for i in xrange(k):
        a = random.randint(1, p-1)

        if pow(a, p-1) % p != 1:
            return False
    return True
