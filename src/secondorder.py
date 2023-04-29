from latexifier import latexify
import sympy as sy

from .explicitSFS import sol_explicita
from .resp.obj.Paso import Paso

from .resp.obj.Pasos import Pasos

'''------------------ECUACIÓN DE SEGUNDO ORDEN----------------'''

def segundo_orden(a: float, b: float, c: float, solve: bool):
    """
    Dada la ecuación: ax''+bx'+cx = 0
    Transformamos en el sistema  x' = y
                                 y' = -(c/a)x-(b/a)y

    :param a: coeficiente acompañando al término x''
    :param b: coeficiente acompañando al término x'
    :param c: coeficiente acompañando al término x
    :param solve: True si se quiere resolver el sistema
    :return: JSON con pasos
    """
    x, y = sy.symbols('x, y')
    pasos = [Paso('x\'=y', 'x\'=y', "Introducimos el siguiente cambio de variable"),
             Paso('x\' = y, y\' = -(c/a)x-(b/a)y', 'x\' = y, \n y\' = ' + latexify(-(c / a) * x - (b / a) * y),
                  "Entonces x\'\'=y\' y despejando obtenemos el sistema:")]
    if solve:
        pasos = pasos + sol_explicita(0, 1, -c / a, -b / a, False)
    return Pasos(pasos).toJson()
