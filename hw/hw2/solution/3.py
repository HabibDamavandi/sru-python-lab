def ex(x):
    sg = 1
    a = 1
    b = 1
    s = 0.0
    for i in range(1,50):
        s += sg * a / b
        sg = -sg
        a *= x
        b *= i
    return s

print("e = %2.10f"%(ex(-1)))



