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
    pasos = [Paso('x\'=y', 'x\'=y', "Introducimos el cambio de variable"),
             Paso('x\'\' = -(c/a)x-(b/a)y', 'x\'\'=-\\dfrac{c}{a}x-\\dfrac{b}{a}x\'',
                  'Entonces, $x\'\'=y\'$, y despejando $x\'\'$')]

    sist = latexify(-(c / a) * x - (b / a) * y)
    pasoLatex = '\\begin{cases} x\'=y \\\\ y\'= ' + sist + '\\end{cases}'

    pasos.append(
        Paso('x\' = y, y\' = -(c/a)x-(b/a)y', pasoLatex, 'El sistema equivalente a la ecuación de segundo grado es'))
    if solve:
        pasos = pasos + sol_explicita(0, 1, -c / a, -b / a, False)
    return Pasos(pasos).toJson()
