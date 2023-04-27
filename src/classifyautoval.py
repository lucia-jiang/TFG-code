from sympyfunctions import *
from .aux import *


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
    if alpha < 0:
        print('El punto (0,0) es un foco estable')
    elif alpha > 0:
        print('El punto (0,0) es un foco inestable')
    else:  # alpha=0
        print('El punto (0,0) es un centro estable')


def c_p_a_doble(autoval, b, c):  # esto no está en los apuntes impresos, en los apuntes de Ec. Diferenciales
    if b == 0 and c == 0:
        print('El punto (0,0) es un punto estelar')  # autovalor > 0 -> se alejan del origen y vicerversa
    else:
        if autoval > 0:
            print('El punto (0,0) es un nodo impropio inestable')
        else:  # autoval < 0
            print('El punto (0,0) es un nodo impropio estable')


'''-----------------------------------------------------'''


# Los autovectores pintan los ejes
def clasificar_punto_autoval(a, b, c, d):
    A = [[a, b], [c, d]]
    autovec = autovectores(A)
    if detNoNulo(A):  # si uno no es complejo, entonces los dos son reales
        det = det_matriz(A)
        # print(autovec[0][0])
        # print(autovec[1][0])
        print('Como el det(A) = {}, existe un único punto de equilibrio, el origen (0,0)'.format(det))
        print('Estudiemos de qué tipo es')
        if parte_imaginaria(autovec[0][0]) == 0:
            if len(autovec) == 2:  # dos autovalores
                c_p_a_real_distinto(autovec)
            else:  # autovalor repetido
                c_p_a_doble(autovec[0][0], b, c)
        else:  # autovalores complejos
            c_p_a_complejo(autovec)
    return 0
