for a in range(1,10):
    for b in range(10):
        print(a*101+b*10, end="\t")
    print()


#aba = "\n".join(["\t".join([str(a*101+b*10) for b in range(10)]) for a in range(1,10)])
#print(aba)
