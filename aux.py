from sympyfunctions import *

t, c1, c2, c3, x, y = sy.symbols('t, c1, c2, c3, x, y', real=True)

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