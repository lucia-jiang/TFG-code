from ..auxiliar.externalFunctions import im, autovectores, matrix, det_matriz
from ..exc.Exceptions import ExceptionDetZero, ExceptionInput, ExceptionNotANumber


def detNoNulo(A: list):
    """
    Verificar que la matriz de entrada tenga determinante distinto del nulo
    :param A: matriz en forma de lista
    :return: bool
    """
    if det_matriz(A) == 0:
        raise ExceptionDetZero('Error: el determinante de la matriz de coeficientes no puede ser nula.')


def esReal(a) -> bool:
    """
    Determina si un número es complejo
    :param a: número
    :return: bool
    """
    return im(a) == 0


def matrizDiagonalizable(A) -> bool:
    """
    Determina si una matriz es diagonalizable. Comprueba que la multiplicidad algebraica y geométrica es igual
    :param A: matriz
    :return: bool
    """
    autoVec = autovectores(A)
    multiplicidad = autoVec[0][1]
    numVectores = len(autoVec[0][2])
    if len(autoVec) > 1 and autoVec[0][0] == autoVec[1][0]:
        multiplicidad = 2  # a veces no se da cuenta de que es el mismo autovalor

    return numVectores == multiplicidad


def comprobarCoeficientes(a, b, c, d):
    """
    Comprobación de que los coeficientes sean todos números reales.
    :param a: coeficiente 1ª fila 1ª columna
    :param b: coeficiente 1ª fila 2ª columna
    :param c: coeficiente 2ª fila 1ª columna
    :param d: coeficiente 2ª fila 2ª columna
    :return: matriz si los coeficientes son todos números
    """
    try:
        a, b, c, d = float(a), float(b), float(c), float(d)
    except:
        raise ExceptionInput('Error: por favor, introduzca números reales.')

    A = [[a, b], [c, d]]
    detNoNulo(A)  # Comprobación de que el determinante de la matriz no es nula.

    return matrix(A)


def string2float(frac_str):
    """
    Transforma un string en float, si es posible
    :param frac_str: número a transformar, las fracciones se pasan como a:b
    :return: float
    """
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split(':')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)
        try:
            if float(leading) < 0:
                sign_mult = -1
            else:
                sign_mult = 1
        except Exception:
            raise ExceptionNotANumber("Error: introduzca números reales")
        return float(leading) + sign_mult * (float(num) / float(denom))
