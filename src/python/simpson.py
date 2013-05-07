#-------------------------------------------------------------------------------
#Modulo: simpson
#
#Autor: Adrian R. Mendioroz Morales y Roberto C. Palenzuela Criado
#
#-------------------------------------------------------------------------------
# Contenido
# Funcion: regla_simpson
#
#   entrada:
#     f: funcion que se va a aproximar
#     a: limite inferior de integracion
#     b: limite superior de integracion
#   salida:
#     Aproximacion de la integral de f en [a,b]
#
# -------------------------------------------------------------------------------

from math import *

def regla_simpson(f,a,b):
  return (b-a)/6.0*(f(a)+4*f((a+b)/2.0)+f(b))
  
def regla_simpson_compuesta(f,a,b,n):
  h=(b-a)/float(n)
  aprox=0
  for l in range(0,n):
    aprox+=regla_simpson(lambda x:(x**2*cos(x)),a+l*h,a+(l+1)*h)
  return aprox
  