n = 12
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%-3d"%(j), end="")
    for j in range(2*(n-i)-1):
        print("   ", end="")
    if i!=n:
        for j in range(i,0,-1):
            print("%-3d"%(j), end="")
    else:
        for j in range(i-1,0,-1):
            print("%-3d"%(j), end="")
        
    print()



