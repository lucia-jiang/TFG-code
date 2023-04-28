import numpy as np

import plotly.graph_objects as go
import plotly.figure_factory as ff

from .comprobaciones.comprobaciones import comprobarCoeficientes
from .resp.definirPasos import getResponseGraph


def diagramaFase(a, b, c, d, delta, xlimInf, xlimSup, ylimInf, ylimSup):
    """
    Diagrama de fases
    :param a: coeficiente 1ª fila 1ª columna
    :param b: coeficiente 1ª fila 2ª columna
    :param c: coeficiente 2ª fila 1ª columna
    :param d: coeficiente 2ª fila 2ª columna
    :param delta: precisión representación
    :param xlimInf: límite inferior del eje de abscisas
    :param xlimSup: límite superior del eje de abscisas
    :param ylimInf: límite inferior del eje de ordenadas
    :param ylimSup: límite superior del eje de ordenadas
    :return: gráfica en html
    """
    comprobarCoeficientes(a, b, c, d)

    xrange = np.arange(xlimInf, xlimSup + delta, delta)
    yrange = np.arange(ylimInf, ylimSup + delta, delta)
    X, Y = np.meshgrid(xrange, yrange)
    U, V = a * X + b * Y, c * X + d * Y

    fig = ff.create_quiver(X, Y, U, V, line=dict(width=0.75, color='dodgerblue'))  # campo

    fig.show()

    return getResponseGraph('x\'={a}x+{b}y, y\'={c}x+{d}y'.format(a,b,c,d), fig)
