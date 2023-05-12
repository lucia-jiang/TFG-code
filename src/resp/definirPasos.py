from latexifier import latexify
import plotly.graph_objects as go
from pytexit import py2tex

from .obj.Grafica import Grafica
from .obj.Paso import Paso
from ..auxiliar.externalFunctions import symbols


def matrix2latex(matrix) -> str:
    """
    Crea una string que representa la matriz en un formato LáTeX
    :param matrix: matriz en formato lista
    :return: matriz en formato LáTeX
    """
    res = "\\begin{pmatrix}\n"
    for row in matrix:
        for elem in row:
            res += latexify(elem) + ' & '
        res = res[:-3] + '\\\\\n'
    return res[:-3] + "\n\\end{pmatrix}"


def vector2latex(vector) -> str:
    """
    Crea un string que representa el vector en un fichero latex
    :param vector: vector en formato lista
    :return: vector en formato LáTeX
    """
    res = "\\begin{pmatrix}\n"
    for elem in vector:
        res += latexify(elem) + '\\\\\n'
    return res[:-3] + "\n\\end{pmatrix}"


def getPasoMatriz(item, descripcion: str) -> Paso:
    """
    Transforma el paso que está en forma de matriz y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    item = item.tolist()  # quitar el Matrix
    paso = str(item)
    pasoLatex = 'A=' + matrix2latex(item)
    return Paso(paso, pasoLatex, descripcion)


def getPaso(item, descripcion: str) -> Paso:
    """
    Transforma el paso y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    paso = str(item)
    pasoLatex = latexify(item)
    return Paso(paso, pasoLatex, descripcion)


def getPasoSFSMatrices(item, descripcion: str) -> Paso:
    """
    Transforma el paso de sfs y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    paso = '{'
    pasoLatex = '\\left\\{'
    for i in item:
        i = i.tolist()
        paso = paso + str(i) + ', '
        pasoLatex = pasoLatex + matrix2latex(i) + ', '
    paso = paso[2:-2] + '}'
    pasoLatex = pasoLatex[:-2] + '\\right\\}'
    return Paso(paso, pasoLatex, descripcion)


def getPasoAutovalores(item, descripcion: str) -> Paso:
    """
    Transforma el item y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    if len(item) == 2:
        pasoLatex = '\\lambda_1 = {}, \\quad \\lambda_2 = {}'.format(latexify(item[0]), latexify(item[1]))
    else:
        pasoLatex = '\\lambda = {} \\quad {}'.format(latexify(item[0]), '\\text{(doble)}')
    return Paso(str(item), pasoLatex, descripcion)


def getPasoAutovaloresComplejos(item, descripcion: str) -> Paso:
    """
    Transforma el paso de un complejo y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    # transformar I en 1j para que latexify entienda
    keys = [complex(str(s).replace('*I', 'j').replace(' ', '')) for s in item]
    autoval1 = latexify(keys[0]).replace('+ -', '-')  # fix bug de latexify
    autoval2 = latexify(keys[1]).replace('+ -', '-')  # fix bug de latexify
    pasoLatex = '\\lambda_1 = {}, \\quad \\lambda_2 = {}'.format(autoval1, autoval2)
    return Paso(str(item), pasoLatex, descripcion)


def getPasoSolExplicita(sol1, sol2, descripcion: str) -> Paso:
    """
    Transforma el paso de mostrar la solución explícita y la explicación en formato Paso
    :param sol1: primer elemento del sfs
    :param sol2: segundo elemento del sfs
    :param descripcion: explicación del paso
    :return: Paso
    """
    c1, c2 = symbols('c1, c2')
    paso = 'X(t) = c1 * ' + str(sol1) + ' + c2 * ' + str(sol2)

    pasoLatex = 'X(t)=' + latexify(c1) + vector2latex(list(sol1)) + '+' + latexify(c2) + vector2latex(list(sol2))
    return Paso(paso, pasoLatex, descripcion)


def getResponseGraph(func: str, figure: go.Figure):
    """
    Retorna una gráfica
    :param func: función a graficar
    :param figure: figura html
    :return: Grafica
    """
    figure = figure.to_html()
    return Grafica(func, figure).toJson()


def autovalList2latex(l: list, n: int):
    """
    Latexifica una lista de valores
    :param l: lista
    :return: formato LáTeX
    """
    pasoLatex = '\\lambda_1^{}={}, \\quad '.format(n, py2tex(str(l[0]))[2:-2])
    pasoLatex = pasoLatex + '\\lambda_2^{}={}'.format(n, py2tex(str(l[1]))[2:-2])
    # for elem in l:
    #     pasoLatex += py2tex(str(elem))[2:-2] + ', '
    return pasoLatex
