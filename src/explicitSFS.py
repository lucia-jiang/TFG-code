from .comprobaciones.comprobaciones import comprobarCoeficientes
from .resp.obj.Pasos import Pasos
from .sfs import sfs
from .resp.definirPasos import getPasoSolExplicita

'''------------------EXPLÍCITAMENTE------------'''


def sol_explicita(a: float, b: float, c: float, d: float, finished: bool):
    """
    Función que obtiene las soluciones explícitas en función de unas constantes.
    Para ello utiliza el método que obtiene los Sistemas Fundamentales de Soluciones
    :param a: coeficiente 1ª fila 1ª columna
    :param b: coeficiente 1ª fila 2ª columna
    :param c: coeficiente 2ª fila 1ª columna
    :param d: coeficiente 2ª fila 2ª columna
    :param finished: False si es un paso intermedio
    :return: JSON si finished==True, y Pasos en caso contrario, ya que se
    """

    comprobarCoeficientes(a, b, c, d)
    sistfs = sfs(a, b, c, d, False)  # pasamos coeficientes e indicamos que buscamos la sol. explícita
    pasos, sols = sistfs[0], sistfs[1]
    pasos.append(getPasoSolExplicita(sols[0], sols[1],
                                     "La solución explícita es la combinación lineal de los elementos en el Sistema Fundamental de Soluciones"))
    return Pasos(pasos).toJson() if finished else (pasos, sols)
