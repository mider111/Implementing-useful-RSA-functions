from random import randint
from modarithmetic import *

# function randprime(mn,mx)
# inputs: two integers mn,mx 
# outputs: a random prime between mn and mx
# Generates random integers over and over using the randint
# method, and test if each one is prime or not.
def randprime(mn,mx):
  rand = randint(mn,mx)
  while(not(isprime(rand, 100))):
    rand = randint(mn,mx)
  
  return rand


# function keygen(mn,mx):
# inputs: two integers mn, mx
# outputs: (n,e,d) which are the keys needed for the RSA algorithm. Then
# primes used are different and between the ranges mn and mx.
def keygen(mn,mx):
  a = randint(mn, mx)
  b = randint(mn, mx)
  while (b == a):
    b = randint(mn, mx)
  
  n = a*b
  l = (a-1)*(b-1)
  e = randint(2, l-1)
  while (extGCD(e , l)[0]!=1):
    e = randint(2, l-1)
  d= (extGCD(e,l))[1]
  return (n, e, d)
