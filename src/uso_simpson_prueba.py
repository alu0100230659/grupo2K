#! /usr/bin/python

from simpson import *
from math import *

def integral(x):
  return 2*x*cos(x)+(x**2-2)*sin(x)

F=integral(3)-integral(1)
print 'Valor real= ',F

aprox=regla_simpson(lambda x:(x**2*cos(x)),1,3)
print '\nAproximacion por la regla de Simpson: ',aprox
print '\tError: ', abs(F-aprox)

aprox=regla_simpson_compuesta(lambda x:(x**2*cos(x)),1,3,10)
print "\nAproximacion por la regla de Simpson compuesta: ",aprox
print '\tError: ', abs(F-aprox)