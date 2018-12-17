for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print()

#ixj = "\n".join(["\t".join([str(i*j) for j in range(1,11)]) for i in range(1,11)])
#print(ixj)
