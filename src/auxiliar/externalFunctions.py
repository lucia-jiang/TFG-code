import sympy as sy
import numpy as np

'''---------------------FUNCIONES QUE LLAMAN A LIBRERÍA NUMÉRICAS  EXTERNAS----------------'''


def det_matriz(A):
    """
    :param A: matriz
    :return: determinante de una matriz
    """
    return sy.Matrix(A).det()


def autovectores(A):
    """
    :param A: matriz
    :return: Devuelve una lista de tuplas formado por (autovalor, multiplicidad y autovector)
    """
    return sy.Matrix(A).eigenvects()


def autovalores(A):
    """
    :param A: matriz
    :return: Retorna un diccionario con los autovalores como clave y multiplicidad como valores
    """
    return sy.Matrix(A).eigenvals()


# Exponencial
def exp(a):
    """
    :param a: número o variable
    :return: exponencial
    """
    return sy.exp(a)


def im(compl):
    """
    :param compl: número complejo
    :return: Parte imaginaria de un número complejo
    """
    return sy.im(compl)


def re(compl):
    """
    :param compl: número complejo
    :return: parte real de un número complejo
    """
    return sy.re(compl)


def cos(theta):
    """
    :param theta: función a evaluar en coseno
    :return: coseno de la función theta
    """
    return sy.cos(theta)


# Seno
def sen(theta):
    """
    :param theta:  función a evaluar en seno
    :return: coseno de la función theta
    """
    return sy.sin(theta)


def integrar(f, x):
    """
    :param f: función
    :param x: variable
    :return: integrar la función f en la variable x
    """
    return sy.integrate(f, x)


def deriv(f, x):
    """
    :param f: función
    :param x: variable
    :return: derivar la función f en la variable x
    """
    return sy.diff(f, x)


def Matrix(A: list):
    """
    :param A: matriz
    :return: matriz en forma de sympy
    """
    return sy.matrices.Matrix(A)


def symbols(a):
    """
    :param a: lista de variables
    :return: símbolos sympy
    """
    return sy.symbols(a)

def matrix(A: list):
    """
    :param A: lista de coeficientes
    :return: matriz numpy
    """
    return np.matrix(A)

def arange(inf, sup, prec):
    """
    :param inf: punto inferior
    :param sup: punto superior
    :param prec: distancia de la lista
    :return: lista repartida de numpy
    """
    return np.arange(inf, sup, prec)

def meshgrid(x,y):
    """
    :param x: lista eje x
    :param y: lista eje y
    :return: meshgrid numpy
    """
    return np.meshgrid(x,y)
