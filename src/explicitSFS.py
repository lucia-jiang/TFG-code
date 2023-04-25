from .aux import *
from src.comprobaciones.comprobaciones import detNoNulo, esReal
from .sfs import *

t, c1, c2, c3, x, y = sy.symbols('t, c1, c2, c3, x, y', real=True)

'''------------------EXPLÍCITAMENTE------------'''

# 2.4. Planar Linear Systems
# TODO: escribir resp
def sol_explicita(a, b, c, d):
    comprobarCoeficientes(a,b,c,d)
    sols = sfs(a,b,c,d)
    res = c1*sols[0]+c2*sols[1]
    print('la solución explícita es: ', res)
    return res