from math import sqrt

def isPrime(n):
    prime = True
    i = 2
    while(i <= sqrt(n)):
        if(n%i == 0):
            prime = False
            break
        i += 1
    return prime


n = int(input("n:"))

if isPrime(n):
    print(n,"is prime.")
else:
    print(n,"is not prime.")
