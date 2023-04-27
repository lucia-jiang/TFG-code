import sympy as sy
from latexifier import latexify
from pytexit import py2tex
from .obj.Paso import Paso
from .obj.Pasos import Pasos
from .obj.Grafica import Grafica


def matrix2latex(matrix) -> str:
    """
    Crea una string que representa la matriz en un fichero latex
    """
    res = "\\begin{pmatrix}\n"
    for row in matrix:
        for elem in row:
            res += latexify(elem) + ' & '
        res = res[:-3] + '\\\\\n'
    return res[:-3] + "\n\\end{pmatrix}"


def getPasoMatriz(item, descripcion: str) -> Paso:
    item = item.tolist()
    paso = str(item)
    pasoLatex = matrix2latex(item)
    return Paso(paso, pasoLatex, descripcion)


def getPaso(item, descripcion: str) -> Paso:
    paso = str(item)
    pasoLatex = latexify(item)
    return Paso(paso, pasoLatex, descripcion)


def getPasoSFSMatrices(item, descripcion: str) -> Paso:
    paso = '{'
    pasoLatex = '\\left\\{'
    for i in item:
        i = i.tolist()
        paso = paso + ', ' + str(i)
        pasoLatex = pasoLatex + ', ' + matrix2latex(i)
    return Paso(paso, pasoLatex, descripcion)


def getPasoAutovaloresComplejos(item, descripcion: str) -> Paso:
    paso = str(item)
    pasoLatex = ''
    for i in item:
        pasoLatex = pasoLatex + ', ' + latexify(i)
    return Paso(paso, pasoLatex, descripcion)


def getPasoSolExplicita(sol1, sol2, descripcion: str) -> Paso:
    c1, c2 = sy.symbols('c1, c2')
    paso = 'c1 * ' + str(sol1) + ' + c2 * ' + str(sol2)
    pasoLatex = latexify(c1) + latexify(sol1) + latexify(c2) + latexify(sol2)
    return Paso(paso, pasoLatex, descripcion)


