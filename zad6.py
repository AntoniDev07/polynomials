from sympy import *
from sympy.plotting import plot

x = symbols('x')
f = x**3 - 3*x

plot(f, (x, -4, 4), ylim=(-10, 10))
