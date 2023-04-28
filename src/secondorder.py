from latexifier import latexify
import sympy as sy

from .explicitSFS import sol_explicita
from .resp.obj.Paso import Paso

from .resp.obj.Pasos import Pasos

'''------------------ECUACIÓN DE SEGUNDO ORDEN----------------'''


# ax''+bx'+cx = 0
# Transformamos en  x' = y
#                   y' = -(c/a)x-(b/a)y
def segundo_orden(a, b, c, solve: bool):
    """Transforma una ecuación de segundo grado en un sistema de dos ecuaciones de primer orden"""
    x, y = sy.symbols('x, y')
    pasos = [Paso('x\'=y', 'x\'=y', "Introducimos el siguiente cambio de variable"),
             Paso('x\' = y, y\' = -(c/a)x-(b/a)y', 'x\' = y, \n y\' = ' + latexify(-(c / a) * x - (b / a) * y),
                  "Entonces x\'\'=y\' y despejando obtenemos el sistema:")]
    if solve:
        pasos = pasos + sol_explicita(0, 1, -c / a, -b / a, False)
    return Pasos(pasos).toJson()

