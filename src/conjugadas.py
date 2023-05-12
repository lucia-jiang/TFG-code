from .resp.definirPasos import autovalList2latex
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
    return sum(1 for i in aVals if re(i) < 0)


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
    paso = 'A1 = [[{},{}], [{},{}]], '.format(a1, b1, c1, d1) + 'A2 = [[{},{}], [{},{}]]'.format(a2, b2, c2, d2)
    pasoLatex = 'A_1 = \\begin{{pmatrix}} {} & {} \\\\ {} & {} \\end{{pmatrix}}, \\quad '.format(a1, b1, c1, d1)
    pasoLatex = pasoLatex + 'A_2 = \\begin{{pmatrix}} {} & {} \\\\ {} & {} \\end{{pmatrix}}'.format(a2, b2, c2, d2)

    pasos = [Paso(paso, pasoLatex, "Dos sistemas son conjugados topológicamente si las matrices son hiperbólicas \
                y tiene mismo número de autovalores negativos. Las matrices asociadas a los sistemas son:")]
    A1, A2 = Matrix([[a1, b1], [c1, d1]]), Matrix([[a2, b2], [c2, d2]])

    aVals1, aVals2 = autovalores(A1), autovalores(A2)

    l_aVals1, l_aVals2 = [], []
    for a in aVals1.keys():
        l_aux = [a] * aVals1[a]
        l_aVals1 = l_aVals1 + l_aux

    for a in aVals2.keys():
        l_aux = [a] * aVals2[a]
        l_aVals2 = l_aVals2 + l_aux

    notHyperbolic1, notHyperbolic2 = notHyperbolic(l_aVals1), notHyperbolic(l_aVals2)

    paso = 'Autovalores de la primera matriz = {}. Autovalores de la segunda matriz = {}'.format(l_aVals1, l_aVals2)
    pasoLatex = '\\text{{Autovalores de la primera matriz : }} {} \\\\ \\text{{Autovalores de la segunda matriz : }} {}'.format(
        autovalList2latex(l_aVals1, 1), autovalList2latex(l_aVals2, 2))
    pasos.append(Paso(paso, pasoLatex, 'Obtenemos los autovalores de ambas matrices: '))

    if notHyperbolic1 and notHyperbolic2:
        pasos.append(Paso(paso, pasoLatex, 'Ninguna de las matrices son hiperbólicas, luego no podemos hablar de \
                        conjugaciones topológicas.'))
        return Pasos(pasos).toJson()
    elif notHyperbolic1:
        pasos.append(Paso(paso, pasoLatex, 'La primera matriz no es hiperbólica, luego no podemos hablar de \
                        conjugaciones topológicas.'))
        return Pasos(pasos).toJson()
    elif notHyperbolic2:
        pasos.append(Paso(paso, pasoLatex, 'La segunda matriz no es hiperbólica, luego no podemos hablar de \
                        conjugaciones topológicas.'))
        return Pasos(pasos).toJson()

    negativos1, negativos2 = countNegativeEigenValues(l_aVals1), countNegativeEigenValues(l_aVals2)

    explConj = "Ambas matrices tienen el mismo número de autovalores negativos: ${}$, " \
               "luego los sistemas son conjugados topológicos.".format(negativos1)
    explNoConj = "Las dos matrices tienen diferente número de autovalores negativos. " \
                 "Mientras que el primer sistema tiene ${}$ autovalores negativos, el segundo tiene ${}$, " \
                 "luego los dos sistemas no son conjugados topológicos.".format(negativos1, negativos2)

    expl = explConj if negativos1 == negativos2 else explNoConj
    pasos.append(Paso('', '', expl))

    return Pasos(pasos).toJson()
