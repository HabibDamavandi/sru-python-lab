import numpy as np
a = np.array([[1,2],[3,4],[5,6]], dtype = np.float32)
b = np.arange(20)
c = b.reshape(4,5,order='F')
d = np.zeros(10, dtype = np.float32).reshape(5,2)
e = np.ones(10).reshape(5,2)
print(a,b,c,d,e,sep="\n")
