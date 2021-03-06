#! /usr/bin/python
########################################################################
# Fichero: uso_simpson.py                                             #
#                                                                     #
# Modulo: simpson                                                     #
#                                                                     #
# Contenido: Comprobacion de los errores cometidos al aplicar la      #
#            regla de Simpson compuesta al calculo de la integral     #
#            de la funcion f(x)=x**2*cos(x), en el intervalo [a,b].   #
#                                                                     #
# Autor/es: Adrian R. Mendioroz Morales                               #
#           Roberto C. Palenzuela Criado                              #
#                                                                     #    
# Fecha de creacion: 06 de mayo de 2013                               # 
#                                                                     #      
########################################################################
from simpson import regla_simpson_compuesta
from math import *

F=(2*3*cos(3)+(3**2-2)*sin(3))-(2*1*cos(1)+(1**2-2)*sin(1))
print '\nValor real= ',F

print '\nAproximacion por la regla de Simpson compuesta: '
print '%25s %15s %15s %15s' % ('Numero de subintervalos','Aproximacion','Error absoluto',
'Error relativo')
n=[2,6,10,50,100]
aprox=0
i=0
for l in n:
  aprox=regla_simpson_compuesta(lambda x:(x**2*cos(x)),1,3,l)
  print '%16d %24.10f %15.10f %15.10f' %(n[i],aprox,abs(F-aprox),abs(F-aprox)/abs(F))
  i=i+1
print "\n"