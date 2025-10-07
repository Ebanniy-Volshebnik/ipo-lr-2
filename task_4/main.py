import math
x = int(input('x = '))
y = int(input('y = '))
u = pow((8+(math.fabs((x-y)*(x-y))+1)),1/3) / (x*x+y*y+2) - pow(math.e,math.fabs(x-y))
print('u =', u)