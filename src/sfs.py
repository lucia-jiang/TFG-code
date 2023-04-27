# from src.comprobaciones.comprobaciones import esReal, comprobarCoeficientes, matrizDiagonalizable
# from src.sympyfunctions import *
# from src.resp.definirPasos import *

from .comprobaciones.comprobaciones import esReal, comprobarCoeficientes, matrizDiagonalizable
from .sympyfunctions import *
from .resp.definirPasos import getPaso, getPasoMatriz, getPasoSFSMatrices, getPasoAutovaloresComplejos, Pasos

'''Sistema fundamental de soluciones'''

c1, c2, t = symbols('c1, c2, t')


def autovaloresRealesDiagonalizable(aVect):
    sol1 = exp(aVect[0][0] * t) * Matrix(aVect[0][2])
    sol2 = exp(aVect[1][0] * t) * Matrix(aVect[1][2])
    return [sol1, sol2]


def autovalorNoDiagonalizable(aVect):
    sol1 = exp(aVect[0][0] * t) * Matrix(aVect[0][2])
    sol2 = exp(aVect[0][0] * t) * Matrix(aVect[0][2]) * (1 + t)
    return [sol1, sol2]


def autovalorComplejo(aVect):
    p = re(aVect[0][0])
    q = im(aVect[0][0])
    u = Matrix(list(map(re, aVect[0][2])))
    w = Matrix(list(map(im, aVect[0][2])))
    sol1 = exp(p * t) * (cos(q * t) * u - sen(q * t) * w)
    sol2 = exp(p * t) * (sen(q * t) * u + cos(q * t) * w)
    return [sol1, sol2]


def sfs(a, b, c, d, solExplicita):
    """El último parámetro se utiliza para devolver los pasos al método de solución explícita"""
    A = comprobarCoeficientes(a, b, c, d)
    pasos = [getPasoMatriz(A, "Esta es la matriz de coeficientes")]

    aVal = autovalores(A)
    aVect = autovectores(A)
    aVal1 = next(iter(aVal))  # primer autovalor

    keys = list(aVal.keys())

    if esReal(aVal1):  # real
        pasos.append(getPaso(keys,
                             "Hallamos los autovalores asociados al sistema y buscamos el Sistema Fundamental de Soluciones"))
        if aVal[aVal1] == 1:  # autovalor simple
            res = autovaloresRealesDiagonalizable(aVect)
            pasos.append(getPasoSFSMatrices(res,
                                            "Como los autovalores son reales y distintos, el Sistema Fundamental de Soluciones es:"))
        else:
            if matrizDiagonalizable(aVect):  # autovalor doble diagonalizable
                res = autovaloresRealesDiagonalizable(aVect)
                pasos.append(getPasoSFSMatrices(res,
                                                "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones se calcula igual que en el caso de autovalores reales distintos:"))
            else:  # autovalor doble, no diagonalizable
                res = autovalorNoDiagonalizable(aVect)
                pasos.append(getPasoSFSMatrices(res,
                                                "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones es:"))
    else:  # complejo
        keys = [str(s).replace('*I', 'j') for s in list(aVal.keys())]
        keys = [complex(s) for s in keys]
        pasos.append(getPasoAutovaloresComplejos(keys,
                                                 "Hallamos los autovalores asociados al sistema y buscamos el Sistema Fundamental de Soluciones"))
        res = autovalorComplejo(aVect)
        pasos.append(getPasoSFSMatrices(res,
                                        "Como los autovalores son complejos, el Sistema Fundamental de Soluciones es:"))

    return (pasos, res) if solExplicita else Pasos(pasos).toJson()
