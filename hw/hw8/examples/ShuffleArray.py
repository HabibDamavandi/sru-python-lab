from random import *
from array import *

array1 = array('i',list(range(10)))

for x in array1:
    print(x,end=",")

print("\nAfter Shuffle")

shuffle(array1)
for x in array1:
    print(x,end=",")
