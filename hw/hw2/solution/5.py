import math

def primelist(n):
    plist = []
    for i in range(2,n+1):
        isprime = True
        for p in plist:
            if (i%p == 0):
                isprime = False
                break
            if p > math.sqrt(i):
                break
        if isprime:
            plist += [i]
            print(i)                       


primelist(100)
