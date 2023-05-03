from .comprobaciones.comprobaciones import comprobarCoeficientes, float2int
from .resp.definirPasos import getPaso, getPasoMatriz
from .resp.obj.Paso import Paso
from .resp.obj.Pasos import Pasos

'''------------------CLASIFICAR PUNTO POR TRAZA Y DETERMINANTE----------------'''


def clasif_complejos(T: float, disc: float):
    """
    Clasificación para cuando los autovalores son complejos
    :param T: traza
    :param disc: discriminante
    :return: pasos
    """
    pasos = [getPaso(disc, "El discriminante es {} < 0. Por lo que sabemos que los autovalores son complejos".format(
        round(disc, 3)))]
    signo = "menor que" if T < 0 else ("mayor que" if T > 0 else "igual a")
    tipo = "foco estable" if T < 0 else ("foco inestable" if T > 0 else "centro estable")
    pasos.append(
        Paso('T={}'.format(round(T,3)), 'T={}'.format(round(T,3)), "Como el determinante T {} es {} 0, el punto (0,0) es un {}".format(round(T, 3), signo, tipo)))
    return pasos


def clasif_reales_distintos(T: float, D: float, disc: float):
    """
    Clasificación para cuando los autovalores son reales y distintos
    :param T: traza
    :param D: determinante
    :param disc: discriminante
    :return: pasos
    """
    pasos = [getPaso(disc,
                     "El discriminante es {} > 0. Por lo que sabemos que los autovalores son reales y diferentes".format(
                         round(disc, 3)))]
    signo = "el determinante es menor que 0" if D < 0 else (
        "el determinante y la traza son mayores que 0" if T > 0 else "el determinante es mayor que 0 y la traza negativa")
    tipo = "punto de silla" if D < 0 else (
        "punto inestable" if T > 0 else "punto estable")
    pasos.append(Paso('T={}, D={}'.format(T, D), 'T={}, D={}'.format(T, D),
                      "Como {}, el punto (0,0) es un {}.".format(signo, tipo)))
    return pasos


def clasif_reales_iguales(T: float, disc: float, b: float, c: float, A):
    """
    Clasificación para cuando los autovalores son reales e iguales
    :param T: traza
    :param disc: discriminante
    :param b: coeficiente fila 1 columna 2
    :param c: coeficiente fila 2 columna 1
    :param A: matriz
    :return: pasos
    """
    pasos = [
        getPaso(disc, "El discriminante es {} = 0. Por lo que sabemos que los autovalores son reales e iguales".format(
            round(disc, 3))),
        getPasoMatriz(A, "Esta es la matriz de coeficientes y nos fijamos en los valores de la diagonal secundaria.")
    ]

    if b == 0 and c == 0:
        pasos.append(Paso('b = 0, c = 0', 'b = 0, c = 0',
                          "Como b=c=0, la matriz es diagonalizable y el punto (0,0) es un punto estelar"))
    else:
        cond_b = "b!=0" if b != 0 else ""
        cond_c = "c!=0" if c != 0 else ""
        cond = cond_b + ' y ' if b != 0 and c != 0 else '' + cond_c
        tipo = "inestable" if T > 0 else "estable"
        paso = cond.replace(' y ', ', ')
        pasoLatex = cond.replace('!=', '\\neq')
        Tsigno = str(T) + '>0' if T > 0 else '<0'
        pasos.append(Paso(paso, pasoLatex,
                          "Como {} la matriz no es diagonalizable, y puesto que T = {}, el punto (0,0) es un nodo impropio {}".format(
                              cond, Tsigno, tipo)))
    return pasos


def clasificar_traza_det(a: float, b: float, c: float, d: float):
    """
    Indica el tipo de punto de equilibrio que es el origen en función de la traza y el determinante de la matriz
    :param a: coeficiente 1ª fila 1ª columna
    :param b: coeficiente 1ª fila 2ª columna
    :param c: coeficiente 2ª fila 1ª columna
    :param d: coeficiente 2ª fila 2ª columna
    :return: JSON
    """
    A = comprobarCoeficientes(a, b, c, d)
    T = a + d  # traza
    D = a * d - b * c  # determinante

    pasos = [Paso('lambda = T ** 2 - 4 * D', '\\lambda = \\dfrac{T \\pm \\sqrt{T^2-4D}}{2}',
                  "Recordemos que siendo T la traza y D el determinante, los autovalores se pueden expresar como:".format(
                      round(T, 3), round(D, 3))),
             getPaso([T, D], "La traza y el determinante son respectivamente {} y {}".format(round(T, 3), round(D, 3)))
             ]
    disc = T ** 2 - 4 * D

    if disc < 0:
        pasos = pasos + clasif_complejos(T, disc)
    elif disc > 0:
        pasos = pasos + clasif_reales_distintos(T, D, disc)
    else:  # disc = 0
        pasos = pasos + clasif_reales_iguales(T, disc, b, c, A)
    return Pasos(pasos).toJson()
