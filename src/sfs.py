from .auxiliar.externalFunctions import symbols, exp, Matrix, re, im, cos, sen, autovalores, autovectores
from .comprobaciones.comprobaciones import esReal, comprobarCoeficientes, matrizDiagonalizable
from .resp.obj.Pasos import Pasos
from .resp.definirPasos import getPaso, getPasoMatriz, getPasoSFSMatrices, getPasoAutovaloresComplejos

'''Sistema fundamental de soluciones'''

c1, c2, t = symbols('c1, c2, t')


def autovaloresRealesDiagonalizable(aVect):
    """
    El sfs es {e^{lambda_1*t}u, 2^{lambda_2}v}
    siendo u, v los autovectores asociados a los autovalores lambda_1 y lambda_2 respectivamente.
    :param aVect:
    :return:
    """
    sol1 = exp(aVect[0][0] * t) * Matrix(aVect[0][2])
    sol2 = exp(aVect[1][0] * t) * Matrix(aVect[1][2])
    return [sol1, sol2]


def autovalorNoDiagonalizable(aVect):
    """
    El sfs es {e^{lambda*t}*u, e^{lambda*t}(1+t)u}
    siendo u el autovector asociado al autovalor lambda (doble)
    :param aVect: autovector
    :return: sfs
    """
    sol1 = exp(aVect[0][0] * t) * Matrix(aVect[0][2])
    sol2 = exp(aVect[0][0] * t) * Matrix(aVect[0][2]) * (1 + t)
    return [sol1, sol2]


def autovalorComplejo(aVect):
    """
    El sfs es {e^{pt}(cos(qt)u-sin(qt)w), e^{pt}(sin(qt)u+cos(qt)w)}
    siendo aVect = p+iq y u,v autovectores asociados
    :param aVect: autovector
    :return: sfs
    """
    p = re(aVect[0][0])
    q = im(aVect[0][0])
    u = Matrix(list(map(re, aVect[0][2])))
    w = Matrix(list(map(im, aVect[0][2])))
    sol1 = exp(p * t) * (cos(q * t) * u - sen(q * t) * w)
    sol2 = exp(p * t) * (sen(q * t) * u + cos(q * t) * w)
    return [sol1, sol2]


def sfs(a, b, c, d, finished):
    """
    Función que dada una matriz retorna el Sistema Fundamental de Soluciones
    :param a: coeficiente 1ª fila 1ª columna
    :param b: coeficiente 1ª fila 2ª columna
    :param c: coeficiente 2ª fila 1ª columna
    :param d: coeficiente 2ª fila 2ª columna
    :param finished: False si es un paso intermedio
    :return: JSON del sfs si finished==True, si no, Pasos para hallar sfs
    """
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
        else:  # autovalor doble
            if matrizDiagonalizable(A):  # autovalor doble diagonalizable
                res = autovaloresRealesDiagonalizable(aVect)
                pasos.append(getPasoSFSMatrices(res,
                                                "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones se calcula igual que en el caso de autovalores reales distintos:"))
            else:  # autovalor doble, no diagonalizable
                res = autovalorNoDiagonalizable(aVect)
                pasos.append(getPasoSFSMatrices(res,
                                                "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones es:"))
    else:  # complejo
        # transformar número imaginario I en j
        keys = [str(s).replace('*I', 'j').replace(' ', '') for s in list(aVal.keys())]
        keys = [complex(s) for s in keys]
        pasos.append(getPasoAutovaloresComplejos(keys,
                                                 "Hallamos los autovalores asociados al sistema y buscamos el Sistema Fundamental de Soluciones"))
        res = autovalorComplejo(aVect)
        pasos.append(getPasoSFSMatrices(res,
                                        "Como los autovalores son complejos, el Sistema Fundamental de Soluciones es:"))

    return Pasos(pasos).toJson() if finished else (pasos, res)
