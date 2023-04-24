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
def parte_imaginaria(compl):
    return sy.im(compl)

def parte_real(compl):
    return sy.re(compl)

# Número imaginario i
def num_imaginario():
    return sy.I

# Coseno
def coseno(theta):
    return sy.cos(theta)

# Seno
def seno(theta):
    return sy.sin(theta)

# Integrar
def integrar(f,x):
    return sy.integrate(f, x)

# Derivar
def deriv(f, x):
    return sy.diff(f, x)
