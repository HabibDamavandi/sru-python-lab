def fact1(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

def fact2(n):
    if(n<=1):
        return 1
    else:
        return n * fact2(n-1)


n = int(input("n:"))

print("factorial =",fact1(n))
