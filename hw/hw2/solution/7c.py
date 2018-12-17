n = int(input("n:"))
line0 = [1]
pascal=[line0]
for i in range(n):
    line1 = [1]
    for j in range(i):
        line1 += [line0[j] + line0[j+1]]
    line1 += [1]
    line0 = line1
    pascal += [line0]

maxlen = len(' '.join(map(lambda x:"%-3d"%(x), pascal[-1])))

for l in pascal:
    print(' '.join(map(lambda x:"%-3d"%(x),l)).center(maxlen))
    

