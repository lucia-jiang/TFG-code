from .aux import *
from .sfs import *

from .resp.definirPasos import getPasoSolExplicita

t, c1, c2, c3, x, y = sy.symbols('t, c1, c2, c3, x, y', real=True)

'''------------------EXPLÍCITAMENTE------------'''


# 2.4. Planar Linear Systems
# TODO: escribir resp
def sol_explicita(a, b, c, d):
    """Función que obtiene las soluciones explícitas en función de unas constantes.
    Para ello utiliza el método que obtiene los Sistemas Fundamentales de Soluciones"""
    sistfs = sfs(a, b, c, d, True)  # pasamos coeficientes e indicamos que buscamos la sol. explícita
    pasos, sols = sistfs[0], sistfs[1]
    pasos.append(getPasoSolExplicita(sols[0], sols[1]),
                 "La solución explícita es la combinación lineal de los elementos en el Sistema Fundamental de Soluciones")
    return Pasos(pasos).toJson()
