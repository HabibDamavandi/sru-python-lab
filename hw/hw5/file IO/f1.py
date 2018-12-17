f = open("f1.txt", "w")

for x in range(10001):
    f.write("%0.2f\n"%(x**3-2*x**2+4))

f.close()
