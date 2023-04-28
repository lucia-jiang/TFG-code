import sympy as sy

'''---------------------FUNCIONES QUE LLAMA SYMPY----------------'''


# Determinante de una matriz
def det_matriz(A):
    return sy.Matrix(A).det()


# Autovectores
# Devuelve una lista de tuplas formado por (autovalor, multiplicidad y autovector)
def autovectores(A):
    return sy.Matrix(A).eigenvects()


# Autovalores
# Retorna un diccionario con los autovalores como clave y multiplicidad como valores
def autovalores(A):
    return sy.Matrix(A).eigenvals()


# Exponencial
def exp(a):
    return sy.exp(a)


# Obtener la parte imaginaria de un número
def im(compl):
    return sy.im(compl)


def re(compl):
    return sy.re(compl)


# Número imaginario i
def im(compl):
    return sy.im(compl)


# Coseno
def cos(theta):
    return sy.cos(theta)


# Seno
def sen(theta):
    return sy.sin(theta)


# Integrar
def integrar(f, x):
    return sy.integrate(f, x)


# Derivar
def deriv(f, x):
    return sy.diff(f, x)


def Matrix(A):
    return sy.matrices.Matrix(A)


def symbols(a):
    return sy.symbols(a)
