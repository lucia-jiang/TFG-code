from sympyfunctions import *
from aux import *
from explicit import *

'''------------------ECUACIÓN DE SEGUNDO ORDEN----------------'''
#TODO: pasar ecuaciones lineales de segundo orden a un sistema (incluso cualquier orden y solo poner como sistema)

# ax''+bx'+cx = 0
# Transformamos en  x' = y
#                   y' = -(c/a)x-(b/a)y
def segundo_orden(a,b,c):
    print('Podemos escribir la ecuación como un sistema')
    print('x\' = y, y\' = -(c/a)x-(b/a)y')
    sol_explicita(0, 1, -c/a, -b/a)
    return 0
