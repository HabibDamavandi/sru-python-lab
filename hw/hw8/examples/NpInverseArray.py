import numpy as np
a = np.linspace(1,10,16)
b = a.reshape(4,4)
c = np.linalg.inv(b)
print(a)
print(b)
print(c)
