from latexifier import latexify

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
    paso = 'disc={}'.format(latexify(disc))
    pasoLatex = '\\Delta = T^2-4D = {}'.format(latexify(disc))

    pasos = [Paso(paso, pasoLatex,
                  "El discriminante es $\\Delta = {} < 0$. Por lo que los autovalores son complejos".format(
                      latexify(disc)))]
    signo = "menor que" if T < 0 else ("mayor que" if T > 0 else "igual a")
    tipo = "foco estable" if T < 0 else ("foco inestable" if T > 0 else "centro estable")
    aVal = "negativa" if T < 0 else ("positiva" if T > 0 else "igual a 0")
    pasos.append(
        Paso('', '', "Como el determinante $T = {}$ es {} 0, la parte real del autovalor será {} y por tanto, \
              el punto $(0,0)$ es un {}.".format(latexify(T), signo, aVal, tipo)))
    return pasos


def clasif_reales_distintos(T: float, D: float, disc: float):
    """
    Clasificación para cuando los autovalores son reales y distintos
    :param T: traza
    :param D: determinante
    :param disc: discriminante
    :return: pasos
    """
    paso = 'disc={}'.format(latexify(disc))
    pasoLatex = '\\Delta = T^2-4D = {}'.format(latexify(disc))
    pasos = [Paso(paso, pasoLatex, "El discriminante es $\\Delta ={} > 0$. Por lo que los autovalores son reales \
                y diferentes".format(latexify(disc)))]
    signo = "el determinante $D={}$ es menor que 0".format(D) if D < 0 else (
        "el determinante $D={}$ y la traza $T={}$ son mayores que 0".format(D, T) if T > 0 else
        "el determinante $D={}$ es mayor que 0 y la traza $T={}$ negativa".format(D, T))
    tipo = "punto de silla" if D < 0 else (
        "punto inestable" if T > 0 else "punto estable")
    aVal = "de signo contrario" if D < 0 else (
        "positivos" if T > 0 else "negativos")
    pasos.append(Paso('', '', "Como {}, los autovalores son {}, el punto $(0,0)$ es un {}.".format(signo, aVal, tipo)))
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
    paso = 'disc={}'.format(latexify(disc))
    pasoLatex = '\\Delta = T^2-4D = {}'.format(latexify(disc))
    pasos = [
        Paso(paso, pasoLatex, "El discriminante $\\Delta {} = 0$. Por lo que los autovalores son reales e iguales."),
        getPasoMatriz(A, "Esta es la matriz de coeficientes y nos fijamos en los valores de la diagonal secundaria.")
    ]

    if b == 0 and c == 0:
        pasos.append(Paso('', '', "Como $b=c=0$, la matriz es diagonalizable y el punto $(0,0)$ es un punto estelar."))
    else:
        cond_b = "$b={}\\neq 0$".format(b) if b != 0 else ""
        cond_c = "$c={}\\neq 0$".format(c) if c != 0 else ""
        pasoLatex = cond_b + (' y ' if b != 0 and c != 0 else '') + cond_c
        tipo = "inestable" if T > 0 else "estable"

        Tsigno = '>0' if T > 0 else '<0'
        pasos.append(Paso('', '', "Como {} la matriz no es diagonalizable, y puesto que $T = {} {}$, el punto \
                        $(0,0)$ es un nodo impropio {}.".format(pasoLatex, T, Tsigno, tipo)))
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

    paso = 'T={}, D={}'.format(latexify(T), latexify(D))
    pasoLatex = 'T={}, \\quad D={}'.format(latexify(T), latexify(D))
    pasos = [Paso('lambda = T ** 2 - 4 * D', '\\lambda = \\dfrac{T \\pm \\sqrt{T^2-4D}}{2}',
                  "Recordemos que siendo $T$ la traza y $D$ el determinante, los autovalores se pueden expresar como:".format(
                      round(T, 3), round(D, 3))),
             Paso(paso, pasoLatex, "Los valores de la traza y el determinante son:")]

    disc = T ** 2 - 4 * D

    if disc < 0:
        pasos = pasos + clasif_complejos(T, disc)
    elif disc > 0:
        pasos = pasos + clasif_reales_distintos(T, D, disc)
    else:  # disc = 0
        pasos = pasos + clasif_reales_iguales(T, disc, b, c, A)
    return Pasos(pasos).toJson()
