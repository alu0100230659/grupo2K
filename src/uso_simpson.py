#! /usr/bin/python
########################################################################
# Fichero: uso_simpson.py                                             #
#                                                                     #
# Modulo: simpson                                                     #
#                                                                     #
# Contenido: Comprobacion del error cometido al aplicar la regla      #
#            de Simpson al calculo de la integral de  la funcion      #
#            f(x)=x**2*cos(x), en el intervalo [a,b].                 #
#                                                                     #
# Autor/es: Adrian R. Mendioroz Morales                               #
#           Roberto C. Palenzuela Criado                              #
#                                                                     #    
# Fecha de creacion: 06 de mayo de 2013                               # 
#                                                                     #      
########################################################################
from simpson import regla_simpson
from math import *

F=(2*3*cos(3)+(3**2-2)*sin(3))-(2*1*cos(1)+(1**2-2)*sin(1))
print '\nValor real= ',F

aprox=regla_simpson(lambda x:(x**2*cos(x)),1,3)
print '\n Aproximacion por la regla de Simpson: ',aprox

print '\t\t       Error absoluto: ', abs(F-aprox)
print '\t\t       Error relativo: ', abs(F-aprox)/abs(F)
print '\t\tCifras significativas: ', int(-log10((abs(F-aprox)/abs(F))/5))
print '\n'