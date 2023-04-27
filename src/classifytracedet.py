from .sympyfunctions import *
from .aux import *

'''------------------CLASIFICAR PUNTO POR TRAZA Y DETERMINANTE----------------'''
def clasificar_traza(a,b,c,d):
    T = a+d #traza
    D = a*d-b*c #determinante
    if T**2-4*D < 0:
        print('Autovalores complejos')
        if T < 0:
            print('El punto (0,0) es un foco estable')
        elif T > 0:
            print('El punto (0,0) es un foco inestable')
        else:  # T=0
            print('El punto (0,0) es un centro estable')
    elif T**2-4*D > 0:
        print('Autovalores reales y distintos')
        if D<0:
            print('El punto (0,0) es un punto de silla')
        elif T>0 and D>0:
            print('El punto (0,0) es un punto inestable')
        elif T<0 and D>0:
            print('El punto (0,0) es un punto estable')
        elif D==0 and T!=0:
            print('Un autovalor 0')
        elif D==0 and T==0:
            print('Los dos autovalores 0')
    else: # T**2-4*D = 0
        print('Autovalores reales y repetidos')

        if b == 0 and c == 0: #TODO: revisar
            print('El punto (0,0) es un punto estelar') #autovalor > 0 --> se alejan del origen y vicerversa
        else:
            if T > 0:
                print('El punto (0,0) es un nodo impropio inestable')
            else: #autoval < 0
                print('El punto (0,0) es un nodo impropio estable')