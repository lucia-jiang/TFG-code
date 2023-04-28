import sympy as sy
from latexifier import latexify
from .obj.Paso import Paso


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
    pasoLatex = matrix2latex(item)
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
        paso = paso + ', ' + str(i)
        pasoLatex = pasoLatex + ', ' + matrix2latex(i)
    return Paso(paso, pasoLatex, descripcion)


def getPasoAutovaloresComplejos(item, descripcion: str) -> Paso:
    """
    Transforma el paso de un complejo y la explicación en formato Paso
    :param item: paso en formato Python
    :param descripcion: explicación del paso
    :return: Paso
    """
    paso = str(item)
    pasoLatex = ''
    for i in item:
        pasoLatex = pasoLatex + ', ' + latexify(i)
    return Paso(paso, pasoLatex, descripcion)


def getPasoSolExplicita(sol1, sol2, descripcion: str) -> Paso:
    """
    Transforma el paso de mostrar la solución explícita y la explicación en formato Paso
    :param sol1: primer elemento del sfs
    :param sol2: segundo elemento del sfs
    :param descripcion: explicación del paso
    :return: Paso
    """
    c1, c2 = sy.symbols('c1, c2')
    paso = 'c1 * ' + str(sol1) + ' + c2 * ' + str(sol2)

    pasoLatex = latexify(c1) + vector2latex(list(sol1)) + latexify(c2) + vector2latex(list(sol2))
    return Paso(paso, pasoLatex, descripcion)
