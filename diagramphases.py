import numpy as np

import plotly.graph_objects as go
import plotly.figure_factory as ff

def diagramaFase(a,b,c,d):
    #TODO: poner estos valores como parámetros de la funciñon
    delta = 0.25
    xlimInf = -2
    xlimSup = 2
    ylimInf = -2
    ylimSup = 2

    xrange = np.arange(xlimInf, xlimSup + delta, delta)
    yrange = np.arange(ylimInf, ylimSup + delta, delta)
    X, Y = np.meshgrid(xrange, yrange)

    U, V = a* X + b * Y, c * X + d * Y

    #TODO: cambiar F,G
    F = Y - X
    G = 1 / 2 * (X + Y) ** 2

    fig = ff.create_quiver(X, Y, U, V, line=dict(width=0.75, color='dodgerblue'))  # campo
    #TODO: cambiar asíntotas
    asint = go.Scatter(x=[-2, 2], y=[2, -2], mode="lines", line_color='orange')
    asint2 = go.Scatter(x=[-2, 2], y=[-2, 2], mode="lines", line_color='orange')


    #TODO: hallar parábolas
    parab = go.Contour(
        z=F - G,
        x=xrange,
        y=yrange,
        contours_coloring='lines',
        line_width=2,
        contours=dict(
            start=0,
            end=0,
            size=2,
        ),
    )

    parab2 = go.Contour(
        z=F + G,
        x=xrange,
        y=yrange,
        contours_coloring='lines',
        line_width=2,
        contours=dict(
            start=0,
            end=0,
            size=2,
        ),
    )

    fig.add_traces([asint, asint2, parab, parab2])
    fig.show()
    print('')