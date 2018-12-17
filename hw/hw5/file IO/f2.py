from math import sqrt

f1 = open("f1.txt", "r")
f2 = open("f2.txt", "w")

for st in f1:
    x = float(st)
    f2.write("%0.10f\n"%(sqrt(x)/(x+1)))

f2.close()
f1.close()
