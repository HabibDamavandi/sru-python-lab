a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
Max = a
if b > Max:
    Max = b
if c > Max:
    Max = c

print("Max is:", Max)

#in python
print("Max is:", max(a,b,c))
