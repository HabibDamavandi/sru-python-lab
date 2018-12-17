def fx(n, r):
    x0 = 0.2
    for i in range(n):
        x1 = r * x0 * (1 - x0)        
        x0 = x1
    return x0

# main #####################
f = open('output.txt', 'w')
r = 2.0
while r <= 4:
    f.write("%0.8f\n" % fx(500, r))
    r += 0.01
f.close()
