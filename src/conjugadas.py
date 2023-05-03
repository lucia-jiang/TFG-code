from latexifier import latexify

from .resp.obj.Paso import Paso
from .resp.obj.Pasos import Pasos
from .auxiliar.externalFunctions import Matrix, autovalores, re

"""Determina si dos sistemas son conjugados topológicamente"""


def notHyperbolic(aVals) -> bool:
    """
    Determina si una matriz es hiperbólica
    :param aVals: lista de autovalores
    :return: True si se encuentra algún autovalor con parte real nula
    """
    return any(re(n) == 0 for n in aVals)


def countNegativeEigenValues(aVals) -> int:
    """
    Cuenta el número de autovalores negativos
    :param aVals: lista de autovalores
    :return: número de autovalores negativos
    """
    return sum(1 for i in aVals if float(i) < 0)


def conjugates(a1: float, b1: float, c1: float, d1: float, a2: float, b2: float, c2: float, d2: float):
    """
    Determina si dos sistemas son conjugados topológicos
    :param a1: coeficiente 1ª fila 1ª columna del primer sistema
    :param b1: coeficiente 1ª fila 2ª columna del primer sistema
    :param c1: coeficiente 2ª fila 1ª columna del primer sistema
    :param d1: coeficiente 2ª fila 2ª columna del primer sistema
    :param a2: coeficiente 1ª fila 1ª columna del segundo sistema
    :param b2: coeficiente 1ª fila 2ª columna del segundo sistema
    :param c2: coeficiente 2ª fila 1ª columna del segundo sistema
    :param d2: coeficiente 2ª fila 2ª columna del segundo sistema
    :return: JSON
    """
    paso = 'x_1\'={a}x_1+{b}y_1, y_1\'={c}x_1+{d}y_1. '.format(a=a1, b=b1, c=c1, d=d1)
    paso = paso + 'x_2\'={a}x_2 + {b}y_2, y_2\'={c}x_2+{d}y_2'.format(a=a2, b=b2, c=c2, d=d2)

    pasoLatex = 'x_1\'={a}x_1+{b}y_1, \\quad y_1\'={c}x_1+{d}y_1'.format(a=a1, b=b1, c=c1, d=d1)
    pasoLatex = pasoLatex + '\\\\' + 'x_2\'={a}x_2 + {b}y_2, y_2\'={c}x_2+{d}y_2'.format(a=a2, b=b2, c=c2, d=d2)

    pasos = [Paso(paso, pasoLatex,
                  "Dos sistemas son conjugados topológicamente si las matrices son hiperbólicas y tiene mismo número de autovalores negativos.")]
    A1, A2 = Matrix([[a1, b1], [c1, d1]]), Matrix([[a2, b2], [c2, d2]])
    aVals1, aVals2 = list(autovalores(A1).keys()), list(autovalores(A2).keys())
    notHyperbolic1, notHyperbolic2 = notHyperbolic(aVals1), notHyperbolic(aVals2)

    paso = 'Autovalores de la primera matriz = {}. Autovalores de la segunda matriz = {}'.format(aVals1, aVals2)
    pasoLatex = '\\text{{Autovalores de la primera matriz : }} {} \\\\ \\text{{Autovalores de la segunda matriz : }} {}'.format(
        latexify(aVals1), latexify(aVals2))

    negativos1, negativos2 = countNegativeEigenValues(aVals1), countNegativeEigenValues(aVals2)

    explNoHip = "Alguna de estas matrices no es hiperbólica, luego los sistemas no son conjugados."
    explConj = "Observamos que ambas matrices tienen el mismo número de autovalores negativos: {}, " \
               "luego los sistemas son conjugados topológicos.".format(negativos1)
    explNoConj = "Observamos que las dos matrices no tienen el mismo número de autovalores negativos." \
                 "Mientras que el primer sistema tiene {} autovalores negativos, el segundo tiene {}," \
                 "luego los dos sistemas no son conjugados topológicos.".format(negativos1, negativos2)

    expl = explNoHip if notHyperbolic1 or notHyperbolic2 else (explConj if negativos1 == negativos2 else explNoConj)

    pasos.append(Paso(paso, pasoLatex, expl))

    return Pasos(pasos).toJson()
