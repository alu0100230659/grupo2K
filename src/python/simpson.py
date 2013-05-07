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
#     a: limite izquierdo de integracion
#     b: limite derecho de integracion
#   salida:
#     Aproximacion de la integral de f en [a,b]
#
# -------------------------------------------------------------------------------

from math import *

def regla_simpson(f,a,b):
  return (b-a)/6.0*(f(a)+4*f((a+b)/2.0)+f(b))