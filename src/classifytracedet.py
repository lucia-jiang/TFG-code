from .comprobaciones.comprobaciones import comprobarCoeficientes
from .resp.definirPasos import getPaso, getPasoMatriz
from .resp.obj.Paso import Paso
from .resp.obj.Pasos import Pasos

'''------------------CLASIFICAR PUNTO POR TRAZA Y DETERMINANTE----------------'''


def clasificar_traza(a, b, c, d):
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
