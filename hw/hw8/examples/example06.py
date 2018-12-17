#آموزش بدست آوردن دترمینان یک ماتریس در پایتون

from numpy import array

from numpy.linalg import det

A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 0]])

B = det(A)

print(B)
