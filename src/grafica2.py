########################################################################
# Fichero: grafica2.py                                                 #
#                                                                      #
# Contenido: Representacion grafica de la funcion f(x)=x**2*cos(x)     #
#            y el polinomio de grado 2 que resulta de alicar el        #
#            metodo de la regla de Simpson.                            #
#                                                                      #
# Autor/es: Adrian R. Mendioroz Morales                                #
#           Roberto C. Palenzuela Criado                               #
#                                                                      #
# Fecha de creacion: 06 de mayo de 2013                                #
########################################################################
from math import cos
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
from matplotlib.pylab import *

def f1(t):
  return t**2*cos(t)

def f2(t):
  return -2.52*t**2+5.36*t-2.29

t=linspace(-1,3.5,51)
y1 = f1(t)
y2 = f2(t)
  
fig = plt.figure(1)
ax = fig.add_subplot(111) 
# set up axis
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
 
plot(t,y1,'r')
hold('on')
plot(t,y2,'b')
legend(['f(x)=x^2*cos(x)', 'P(x)= -2.52 x^2 + 5.36 x - 2.29'],'best')
axis([-1,3.5, -10, 2])  #[tmin, tmax, ymin, ymax]
savefig('grafica2.eps')
show()