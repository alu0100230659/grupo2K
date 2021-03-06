########################################################################
# Fichero: grafica.py                                                  #
#                                                                      #
# Contenido: Representacion grafica de la funcion f(x)=x**2*cos(x)     #
#                                                                      #
# Autor/es: Adrian R. Mendioroz Morales                                #
#           Roberto C. Palenzuela Criado                               #
#                                                                      #
# Fecha de creacion: 06 de mayo de 2013                                #
########################################################################
from math import cos
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
from matplotlib.pylab import *

def f(t):
  return t**2*cos(t)

t = linspace(-1, 3.5, 51)  # 51 puntos entre 0 y 3
y = zeros(len(t))       # reserva memoria para y con elementos flotantes
for i in xrange(len(t)):
  y[i] = f(t[i])

fig = figure(1)
ax = fig.add_subplot(111) 
# set up axis
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
 
plot(t,y)
xlabel('x')
ylabel('y')
legend(['f(x)=x^2*cos(x)'],'best')
axis([-1,3.5, -10, 2])  #[tmin, tmax, ymin, ymax]
savefig('grafica.eps')
show()
