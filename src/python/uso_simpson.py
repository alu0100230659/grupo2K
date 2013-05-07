#! /usr/bin/python

from simpson import *
from math import *

def integral(x):
  return 2*x*cos(x)+(x**2-2)*sin(x)

F=integral(3)-integral(1)
print '\nValor real= ',F

aprox=regla_simpson(lambda x:(x**2*cos(x)),1,3)
print '\nAproximacion por la regla de Simpson: ',aprox

print '\t\t\t\tError: ', abs(F-aprox)

print '\nAproximacion por la regla de Simpson compuesta: '
print '%25s %15s %15s' % ('Numero de subintervalos','Aproximacion','Error')
n=[2,6,10,50,100]
aprox=0
i=0
for l in n:
  aprox=regla_simpson_compuesta(lambda x:(x**2*cos(x)),1,3,l)
  print '%25d %15.10f %15.10f' %(n[i],aprox,abs(F-aprox))
  i=i+1
print "\n"