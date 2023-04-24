from sympyfunctions import *
from .aux import *

t, c1, c2, c3, x, y = sy.symbols('t, c1, c2, c3, x, y', real=True)

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

'''-------------------------------------'''

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