#! /usr/bin/python

from simpson import *
from math import *

def integral(x):
  return 2*x*cos(x)+(x**2-2)*sin(x)

F=2*integral(pi/2)-integral(1)-integral(3)
print 'Valor real= ',F

lista=[1,4,10,50,100]
for l in lista:
  aprox=0
  for n in range(1,l+1):
    aprox+=regla_simpson(lambda x:(x**2*cos(x)),1+(2*n-2)/float(l),1+((2*n)/float(l)))
  print 'La aproximacion de la integral es: ', aprox
  print 'El error es: ', abs(F-aprox)