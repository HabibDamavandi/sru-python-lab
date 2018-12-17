from random import *
import numpy as np
x = np.random.rand(4,5)
y = np.random.rand(5,3)
z = np.matmul(x,y)
print(z)
print(np.sort(z,axis=0))


