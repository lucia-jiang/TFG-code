from latexifier import latexify
from pytexit import py2tex
from .obj.Paso import Paso
from .obj.Pasos import Pasos
from .obj.Grafica import Grafica


def matrix2latex(matrix) -> str:
    """
    Crea una string que representa la matriz en un fichero latex
    """
    #print('matrix', matrix)
    res = "\\begin{pmatrix}\n"
    for row in matrix:
        for elem in row:
            res += latexify(elem) + ' & '
        res = res[:-3] + '\\\\\n'
    return res[:-3] + "\n\\end{pmatrix}"

def getPasoMatriz(item, descripcion: str):
    item = item.tolist()
    paso = str(item)
    # print('paso',paso)
    pasoLatex = matrix2latex(item)
    return Paso(paso, pasoLatex, descripcion)

def getPaso(item, descripcion: str):
    paso = str(item)
    pasoLatex = latexify(item)
    return Paso(paso, pasoLatex, descripcion)

def getPasoSFSMatrices(item, descripcion: str):
    paso = '{'
    pasoLatex = '\\left\\{'
    for i in item:
        i = i.tolist()
        paso = paso + ', ' + str(i)
        pasoLatex = pasoLatex + ', ' + matrix2latex(i)
    return Paso(paso, pasoLatex, descripcion)
