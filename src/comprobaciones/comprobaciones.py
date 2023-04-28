import numpy as np
from ..sympyfunctions import *
from ..exc.Exceptions import *


def detNoNulo(A: list):  # verificar que la matriz de entrada tenga determinante distinto del nulo
    if det_matriz(A) == 0:
        raise ExceptionDetZero('Error: el determinante de la matriz de coeficientes no puede ser nula.')


def esReal(a):
    return im(a) == 0


def matrizDiagonalizable(A):
    autoVec = autovectores(A)
    multiplicidad = autoVec[0][1]
    numVectores = len(autoVec[0][2])
    if len(autoVec) > 1 and autoVec[0][0] == autoVec[1][0]:
        multiplicidad = 2  # a veces no se da cuenta de que es el mismo autovalor

    return numVectores == multiplicidad


def comprobarCoeficientes(a, b, c, d):
    # Comprobación de que los coeficientes sean todos números reales.
    try:
        a, b, c, d = float(a), float(b), float(c), float(d)
    except:
        raise ExceptionInput('Error: por favor, introduzca números reales.')
    # Comprobación de que el determinante de la matriz no es nula.
    A = [[a, b], [c, d]]
    detNoNulo(A)

    return np.matrix(A)
