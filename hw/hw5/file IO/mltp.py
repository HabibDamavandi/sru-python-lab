f = open("mltp10.txt", "w")

for i in range(1,11):
    for j in range(1,11):
        f.write("%d\t"%(i*j))
    f.write("\n")

f.close()

   

  
