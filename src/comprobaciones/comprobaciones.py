import numpy as np

from src.sympyfunctions import *
from src.exc.Exceptions import *

def detNoNulo(A: list): #verificar que la matriz de entrada tenga determinante distinto del nulo
    if det_matriz(A)==0:
        raise ExceptionDet('Error: el determinante de la matriz de coeficientes no puede ser nula.')


def esReal(a):
    return parte_imaginaria(a)==0

def matrizDiagonalizable(autoVec):
    multiplicidad = autoVec[0][1]
    numVectores = len(autoVec[0][2])
    return numVectores == multiplicidad

def comprobarCoeficientes(a,b,c,d):
    # Comprobación de que los coeficientes sean todos números reales.
    try:
        a, b, c, d = float(a), float(b), float(c), float(d)
    except:
        raise ExceptionInput('Error: por favor, introduzca números reales.')
    # Comprobación de que el determinante de la matriz no es nula.
    A = [[a, b], [c, d]]
    detNoNulo(A)

    return np.matrix(A)