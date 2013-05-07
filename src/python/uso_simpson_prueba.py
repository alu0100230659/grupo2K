#! /usr/bin/python

from simpson import *
from math import *

def integral(x):
  return 2*x*cos(x)+(x**2-2)*sin(x)

F=2*integral(pi/2)-integral(1)-integral(3)
print 'Valor real= ',F

aprox = regla_simpson(lambda x:(x**2*cos(x)),1,pi/2)
aprox += regla_simpson(lambda x:(x**2*cos(x)),pi/2,3)
print 'La aproximacion de la integral es: ', aprox
print 'El error es: ', abs(F-aprox)