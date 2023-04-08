import numpy as np
from aux import *

import plotly.graph_objects as go
import plotly.figure_factory as ff

def diagramaFase(a,b,c,d):
    #TODO: poner estos valores como parámetros de la función
    delta = 0.25
    xlimInf = -2
    xlimSup = 2
    ylimInf = -2
    ylimSup = 2

    xrange = np.arange(xlimInf, xlimSup + delta, delta)
    yrange = np.arange(ylimInf, ylimSup + delta, delta)
    X, Y = np.meshgrid(xrange, yrange)
    U, V = a* X + b * Y, c * X + d * Y

    fig = ff.create_quiver(X, Y, U, V, line=dict(width=0.75, color='dodgerblue'))  # campo

    fig.show()
