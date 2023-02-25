import sympy as sy
import plotly.figure_factory as ff
import plotly.graph_objects as go

t, c1, c2, c3, x, y = sy.symbols('t, c1, c2, c3, x, y', real=True)
#TODO: linkear con la calculadora
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

'''-------------------AUXILIARES----------------'''
def detNoNulo(A):
    if det_matriz(A)==0: # TODO: mensaje de error
        print('El determinante de la matriz de coeficientes es nula, por favor, introduzca una con única solución')
        return False
    return True

# Método de Variación de los Parámetros
# sol: ecuación a la que aplicamos MVP
# otra_ec: ecuación en la que sustituir para obtener la relación de coeficientes
# var: x o y
def mvp(sol, otra_ec, var, a, b, c, d):
    print('sol: {}'.format(sol))
    print('otra_ec: {}'.format(otra_ec))
    print('var: {}'.format(var))
    print('a = {}, b = {}, c = {}, d = {}'.format(a,b,c,d))
    # Derivamos la solución y sustituimos en la ecuación
    soldiff = deriv(sol, t)
    print('derivada = {}'.format(soldiff))
    if var == x:
        print('Resolver la ecuación: {} = {}'.format(soldiff, a * sol + b * otra_ec))
        coeff = sy.solve(soldiff - a*sol+b*otra_ec, c3)[0]
        print('Entonces, c3 = {}'.format(coeff))
        ec = sol.subs(c3, coeff)
        print('Sustituyendo, obtenemos que la solución es x = {}, y = {}'.format(ec, otra_ec))
        return [ec, otra_ec]
    elif var == y:
        print('Resolver la ecuación: {} = {}'.format(soldiff, c * otra_ec + d * sol))
        coeff = sy.solve(soldiff - (c * otra_ec + d * sol), c3)[0]
        print('Entonces, c3 = {}'.format(coeff))
        ec = sol.subs(c3, coeff)
        print('Sustituyendo, obtenemos que la solución es x = {}, y = {}'.format(otra_ec, ec))
        return [otra_ec, ec]

    return 0
'''------------------EXPLÍCITAMENTE------------'''

def sol_explicita_real_distintas(autovec):
    # TODO: en la teoría, demostrar que la suma de estos son las únicas soluciones (junto con el 0)
    sol1 = exp(autovec[0][0] * t) * sy.matrices.Matrix(autovec[0][2])
    sol2 = exp(autovec[1][0] * t) * sy.matrices.Matrix(autovec[1][2])
    # print(sol1)
    # print(sol2)
    print('Todas las soluciones vienen dadas como (x,y) = {}, con c1,c2 números reales'.format(c1 * sol1 + c2 * sol2))
    return c1 * sol1 + c2 * sol2

def sol_explicita_real_igual(autovec, a, b, c, d):
    # TODO: en la teoría, demostrar que la suma de estos son las únicas soluciones (junto con el 0)
    print(autovec[0][2])
    autoval = autovec[0][0]
    res = None
    if b == 0 and c == 0:
        xdiff, ydiff = a*x, d*y
        print('Tenemos que resolver el sistema x\' = {}, y\' = {}'.format(xdiff, ydiff))
        xsol, ysol = c1*exp(autoval*t), c2*exp(autoval*t)
        print('Todas las soluciones vienen dadas como x = {}, y = {}, con c1 y c2 números reales'.format(xsol, ysol))
    elif b == 0:
        xdiff, ydiff = a*x, c*x+d*y
        print('Tenemos que resolver el sistema x\' = {}, y\' = {}'.format(xdiff, ydiff))
        xsol = c1 * exp(autoval*t)
        print('Resolvemos la primera ecuación: x = {}'.format(xsol))
        ydiff = c*xsol+d*y
        print('Entonces la ecuación a resolver es y\' = {}'.format(ydiff))
        ysol = c2*exp(autoval*t)+c3*t*exp(autoval*t)
        print('El resultado es x = {}, y = {}'.format(xsol, ysol))
        print('Para hallar las constantes c2 y c3, aplicaremos el Método de Variación de los Parámetros')
        # Método de Variación de los Parámetros
        res = mvp(ysol, xsol, y, a, b, c, d)
    elif c == 0:
        xdiff, ydiff = a * x + b * y, d * y
        print('Tenemos que resolver el sistema x\' = {}, y\' = {}'.format(xdiff, ydiff))
        ysol = c1 * exp(autoval * t)
        print('Resolvemos la primera ecuación: y = {}'.format(ysol))
        xdiff = a * x + b * ysol
        print('Entonces la ecuación a resolver es x\' = {}'.format(xdiff))
        xsol = c2 * exp(autoval * t) + c3 * t * exp(autoval * t)
        print('El resultado es x = {}, y = {}'.format(xsol, ysol))
        print('Para hallar las constantes c2 y c3, aplicaremos el Método de Variación de los Parámetros')
        # Método de Variación de los Parámetros
        res = mvp(xsol, ysol, x, a, b, c, d)
    return res

def sol_explicita_compleja(autovec):
    print(autovec)
    alpha = parte_real(autovec[0][0])
    beta = parte_imaginaria(autovec[0][0])
    print(beta)
    sol = exp((alpha+ num_imaginario()*beta) * t) * sy.matrices.Matrix(autovec[0][2])
    print('La segunda ecuación es redundante puesto que i{}x={}y, por lo que {} es una solución del sistema'.format('{beta}','{beta}',sol)) #TODO: cambiar {beta}
    print('Recordamos la fórmula de Euler: ') #TODO: insertar fórmula de Euler
    X = [coseno(beta*t)+num_imaginario()*seno(beta*t), -seno(beta*t)+num_imaginario()*coseno(beta*t)]
    X_real = sy.matrices.Matrix([parte_real(x) for x in X])
    X_im = sy.matrices.Matrix([parte_imaginaria(x) for x in X])
    # print('X_real={}'.format(X_real))
    # print('X_im={}'.format(X_im))
    res = c1*exp(alpha*t)*X_real+c2*exp(alpha*t)*X_im
    print('Todas las soluciones del sistema vienen dadas como X(t) = {}'.format(res))
    return res

# 2.4. Planar Linear Systems
# TODO: escribir pasos
# TODO: preguntar para escribir en LáTeX en la calculadora
def sol_explicita(a,b,c,d):
    A = [[a,b],[c,d]]
    res = None
    if detNoNulo(A):
        autovec = autovectores(A) #suponiendo 2 diferentes
        if parte_imaginaria(autovec[0][0]) == 0:
            if len(autovec) == 2: # dos autovalores
                res = sol_explicita_real_distintas(autovec)
            else: #autovalor repetido
                res = sol_explicita_real_igual(autovec, a, b, c, d)
        else: #autovalores complejos
            res = sol_explicita_compleja(autovec)
        print('')

    return res


'''------------------CLASIFICAR PUNTO POR AUTOVALORES----------------'''

def c_p_a_real_distinto(autovec):
    # TODO: planos de fase
    # TODO: explicación
    if (autovec[0][0] < 0 and autovec[1][0] > 0) or (autovec[0][0] > 0 and autovec[1][0] < 0):
        print('El punto (0,0) es un punto de silla')
    elif autovec[0][0] < 0 and autovec[1][0] < 0:
        print('El punto (0,0) es un punto estable')
    elif autovec[0][0] > 0 and autovec[1][0] > 0:
        print('El punto (0,0) es un punto inestable')
    return 0

def c_p_a_complejo(autovec):
    alpha = parte_real(autovec[0][0])
    if alpha<0:
        print('El punto (0,0) es un foco estable')
    elif alpha>0:
        print('El punto (0,0) es un foco inestable')
    else: #alpha=0
        print('El punto (0,0) es un centro estable')

def c_p_a_doble(autoval, b, c): #esto no está en los apuntes impresos, en los apuntes de Ec. Diferenciales
    if b == 0 and c == 0:
        print('El punto (0,0) es un punto estelar') #autovalor > 0 -> se alejan del origen y vicerversa
    else:
        if autoval > 0:
            print('El punto (0,0) es un nodo impropio inestable')
        else: #autoval < 0
            print('El punto (0,0) es un nodo impropio estable')

#Los autovectores pintan los ejes
def clasificar_punto_autoval(a,b,c,d):
    A = [[a, b], [c, d]]
    autovec = autovectores(A)
    if detNoNulo(A): #si uno no es complejo, entonces los dos son reales
        det = det_matriz(A)
        # print(autovec[0][0])
        # print(autovec[1][0])
        print('Como el det(A) = {}, existe un único punto de equilibrio, el origen (0,0)'.format(det))
        print('Estudiemos de qué tipo es')
        if parte_imaginaria(autovec[0][0]) == 0:
            if len(autovec) == 2: # dos autovalores
                c_p_a_real_distinto(autovec)
            else: #autovalor repetido
                c_p_a_doble(autovec[0][0], b, c)
        else: #autovalores complejos
            c_p_a_complejo(autovec)
    return 0


'''------------------CLASIFICAR PUNTO POR TRAZA Y DETERMINANTE----------------'''



'''------------------ECUACIÓN DE SEGUNDO ORDEN----------------'''
#TODO: pasar ecuaciones lineales de segundo orden a un sistema (incluso cualquier orden y solo poner como sistema)

# ax''+bx'+cx = 0
# Transformamos en  x' = y
#                   y' = -(c/a)x-(b/a)y
def segundo_orden(a,b,c):
    print('Podemos escribir la ecuación como un sistema')
    print('x\' = y, y\' = -(c/a)x-(b/a)y')
    sol_explicita(0, 1, -c/a, -b/a)
    return 0


'''----------------PRUEBAS------------'''
# SOLUCIÓN EXPLÍCITA
# sol_explicita(1,3,1,-1) #ejemplo de la documentación
# sol_explicita(1,1,1,1) #ejemplo determinante nulo
# sol_explicita(-1,0,0,-2) #punto estable
# sol_explicita(1,0,0,2) #punto inestable
# sol_explicita(0,1,-1,0) #autovalores complejos puro
# sol_explicita(2,1,-1,2) #autovalores complejos mixto
# sol_explicita(-2,1,-1,-2) #autovalores complejos mixo
# sol_explicita(2,0,0,2) #autovalor repetido
# sol_explicita(1,0,0,1) #autovalor real repetido
# sol_explicita(2,0,3,2) #autovalor real repetido
# sol_explicita(3,2,0,3) #autovalor real repetido

# SEGUNDO ORDEN PASADO A SISTEMA
# segundo_orden(1,-2,-3)

# CLASIFICAR PUNTOS
# clasificar_punto_autoval(1,1,1,1)  #ejemplo determinante nulo
# clasificar_punto_autoval(1,3,1,-1) #punto de silla
# clasificar_punto_autoval(-1,0,0,-2) #punto estable
# clasificar_punto_autoval(1,0,0,2) #punto inestable
# clasificar_punto_autoval(0,1,-1,0) #autovalores complejos puro y centro estable
# clasificar_punto_autoval(2,1,-1,2) #autovalores complejos mixto y foco inestable
# clasificar_punto_autoval(-2,1,-1,-2) #autovalores complejos mixo y foco estable
# clasificar_punto_autoval(1,0,0,1) #autovalor real repetido
# clasificar_punto_autoval(2,0,3,2) #autovalor real repetido
# clasificar_punto_autoval(3,2,0,3) #autovalor real repetido

# print(autovalores([[0,1],[-1,0]]))