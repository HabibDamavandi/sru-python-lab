"""
Create Spirograph curves made by one circle of radius r2 rolling 
around the inside (or outside) of another of radius r1.  The pen
is a distance r3 from the center of the first circle.
"""
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, linspace
from math import gcd

r1 = 290
r2 = 170
r3 = 140

ncycle = r2/gcd(r1,r2)

alfa1 = linspace(0, ncycle*2*pi, 10000)
alfa2 = (-(r1/r2)*alfa1)
x = (r1-r2)*cos(alfa1)+r3*cos(alfa2)
y = (r1-r2)*sin(alfa1)+r3*sin(alfa2)

plt.plot(x,y)
fig = plt.gcf()
fig.gca().set_aspect('equal')
plt.show()
