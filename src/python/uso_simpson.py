#! /usr/bin/python

from simpson import regla_simpson, regla_simpson_compuesta
from math import *

F=(2*3*cos(3)+(3**2-2)*sin(3))-(2*1*cos(1)+(1**2-2)*sin(1))
print '\nValor real= ',F

aprox=regla_simpson(lambda x:(x**2*cos(x)),1,3)
print '\nAproximacion por la regla de Simpson: ',aprox

print '\t\t      Error absoluto: ', abs(F-aprox)
print '\t\t      Error relativo: ', abs(F-aprox)/abs(F)

print '\nAproximacion por la regla de Simpson compuesta: '
print '%25s %15s %15s %15s' % ('Numero de subintervalos','Aproximacion','Error absoluto','Error relativo')
n=[2,6,10,50,100]
aprox=0
i=0
for l in n:
  aprox=regla_simpson_compuesta(lambda x:(x**2*cos(x)),1,3,l)
  print '%16d %24.10f %15.10f %15.10f' %(n[i],aprox,abs(F-aprox),abs(F-aprox)/abs(F))
  i=i+1
print "\n"