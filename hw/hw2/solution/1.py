#Recursive GCD
def gcd1(a,b):
    if b==0:
        return a
    else:
        return gcd1(b,a%b)

#Non Recursive GCD
def gcd2(a,b):
    while(b!=0):
        a,b = b,a%b
    return a

print("Recursive GCD of (21,35) =", gcd1(21,35))
print("Non Recursive GCG of (21,35) =", gcd2(21,35))



