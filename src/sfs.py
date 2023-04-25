from src.comprobaciones.comprobaciones import *
from src.resp.obj.Pasos import Pasos
from sympyfunctions import *
import sympyfunctions as sf
import resp.definirPasos as resp

'''Sistema fundamental de soluciones'''

c1, c2, t = sf.symbols('c1, c2, t')

def autovaloresRealesDiagonalizable(aVect):
    sol1 = sf.exp(aVect[0][0] * t) * sf.Matrix(aVect[0][2])
    sol2 = sf.exp(aVect[1][0] * t) * sf.Matrix(aVect[1][2])
    return [sol1, sol2]

def autovalorNoDiagonalizable(aVect):
    sol1 = sf.exp(aVect[0][0]*t) * sf.Matrix(aVect[0][2])
    sol2 = sf.exp(aVect[0][0]*t) * sf.Matrix(aVect[0][2]) * (1+t)
    return [sol1, sol2]

def autovalorComplejo(aVect):
    p = sf.re(aVect[0][0])
    q = sf.I(aVect[0][0])
    u = list(map(sf.re, aVect[0][2]))
    w = list(map(sf.I, aVect[0][2]))
    sol1 = exp(p*t)*(sf.cos(q*t)*u-sf.sen(q*t)*w)
    sol2 = exp(p*t)*(sf.sen(q*t)*u+sf.cos(q*t)*w)
    return [sol1, sol2]
def sfs(a,b,c,d):
    A = comprobarCoeficientes(a,b,c,d)
    pasos = []
    pasos.append(resp.getPasoMatriz(A, "Esta es la matriz de coeficientes"))

    aVal = autovalores(A)
    aVect = autovectores(A)
    aVal1 = next(iter(aVal)) #primer autovalor

    pasos.append(resp.getPaso(list(aVal.keys()), "Hallamos los autovalores asociados al sistema y buscamos el Sistema Fundamental de Soluciones"))
    if esReal(aVal1): #real
        if aVal[aVal1] == 1: #autovalor simple
            res = autovaloresRealesDiagonalizable(aVect)
            pasos.append(resp.getPasoSFSMatrices(res, "Como los autovalores son reales y distintos, el Sistema Fundamental de Soluciones es:"))
        else:
            if matrizDiagonalizable(aVect):
                res = autovaloresRealesDiagonalizable(aVect)
                pasos.append(resp.getPasoSFSMatrices(res,
                                                     "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones se calcula igual que en el caso de autovalores reales distintos:"))
            else:
                res = autovalorNoDiagonalizable(aVect)
                pasos.append(resp.getPasoSFSMatrices(res,
                                                     "Como el autovalor es doble y la matriz no es diagonalizable, el Sistema Fundamental de Soluciones es:"))
    else: #complejo
        res = autovalorComplejo(aVect)
        pasos.append(resp.getPasoSFSMatrices(res,
                                             "Como los autovalores son complejos, el Sistema Fundamental de Soluciones es:"))

    #print(res)
    return Pasos(pasos).toJson()



print(sfs(-1,0,0,-2))