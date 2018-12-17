def digisum(n):
    s=0
    while(n!=0):
        s = s + n%10
        n //= 10
    return s

def reverse(n):
    s=0
    while(n!=0):
        s = s *10 + n%10
        n //= 10
    return s

n = int(input("Enter n:"))

print("Sum of digits of %d = %d" % (n, digisum(n)))

print("Reverse of %d = %d" % (n, reverse(n)))


