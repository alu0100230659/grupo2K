########################################################################
# Fichero: simpson.py                                                 #
#                                                                     #
# Modulo: simpson                                                     #
#                                                                     #
# Contenido: Funciones de aplicacion de la regla de Simpson de        # 
#            integracion numerica.                                    #
#                                                                     #
# Autor/es: Adrian R. Mendioroz Morales                               #
#           Roberto C. Palenzuela Criado                              #
#                                                                     #
# Funciones:                                                          #
#   regla_simpson: Calcula una aproximacion a la integral de una      #
#                  funcion en un intervalo [a,b], aplicando la        #
#                  regla de Simpson.                                  #
#      Entrada:                                                       #
#         f: funcion que se va a aproximar                            #
#         a: limite inferior de integracion                           #
#         b: limite superior de integracion                           #
#      Salida:                                                        #
#         Aproximacion de la integral de f en [a,b]                   #
#                                                                     #
#   regla_simpson_compuesta: Calcula una aproximacion a la integral   #
#                            de una funcion en un intervalo [a,b],    #
#                            empleando n subintervalos y aplicando la #
#                            regla de Simpson compuesta.              #
#      Entrada:                                                       #
#         f: funcion que se va a aproximar                            #
#         a: limite inferior de integracion                           #
#         b: limite superior de integracion                           #
#         n: numero (par) de subintervalos                            #
#      Salida:                                                        #
#         Aproximacion de la integral de f en [a,b]                   #
#                                                                     #    
# Fecha de creacion: 06 de mayo de 2013                               # 
#                                                                     #      
########################################################################
from math import *

def regla_simpson(f,a,b):
  return (b-a)/6.0*(f(a)+4*f((a+b)/2.0)+f(b))
  
def regla_simpson_compuesta(f,a,b,n):
  h=(b-a)/float(n)
  aprox=0
  for l in range(0,n):
    aprox+=regla_simpson(lambda x:(x**2*cos(x)),a+l*h,a+(l+1)*h)
  return aprox