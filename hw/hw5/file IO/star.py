f = open("star.txt", "w")

for i in range(50):
    f.write(("*"*(2*i+1)).center(100))
    f.write("\n")

f.close()

   

  
