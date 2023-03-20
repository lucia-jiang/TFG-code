import numpy as np
from aux import *

import plotly.graph_objects as go
import plotly.figure_factory as ff

def eval_matrix(xrange, yrange, ec_xy,c1,c2):
    X, Y = np.meshgrid(xrange, yrange)
    coords = np.dstack((X, Y))
    z = np.zeros((len(X), len(X[0])))
    for i in range(len(z)):
        for j in range(len(z[0])):
            z[i][j] = ec_xy.subs({'x': coords[i][j][0], 'y': coords[i][j][1], 'c1': c1, 'c2': c2})
    return z


def asintotas(c1,c2,xrange,yrange, ec_xy):
    parab = go.Contour(
        z = eval_matrix(xrange, yrange, ec_xy,c1,c2),
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
    return parab
    return 0

def diagramaFase(a,b,c,d,l):
    #l: lista de tuplas de coeficientes
    #TODO: poner estos valores como parámetros de la función
    delta = 0.25
    xlimInf = -2
    xlimSup = 2
    ylimInf = -2
    ylimSup = 2

    #TODO: optimizar esto
    A = [[a, b], [c, d]]
    autovec = autovectores(A)

    x,y,c1,c2,xi1,xi2=sy.symbols('x,y,c1,c2,xi1,xi2')
    #TODO: terminar clasificación para representar órbitas
    T = a + d  # traza
    D = a * d - b * c  # determinante
    if T**2-4*D > 0: #autovalores reales y distintos
        autoval1, autoval2 = (autovec[1][0], autovec[0][0]) if (autovec[1][0]>autovec[0][0]) else (autovec[0][0],autovec[1][0])
        razon = autoval2/autoval1
        ec = xi2 -c2*(xi1/c1)**(razon)
        print('ec: {}'.format(ec))
        P = autovec[1][2][0].col_insert(1, autovec[0][2][0])
        Pinv = P.inv()
        print('P: {} P^(-1): {}'.format(P, Pinv))
        xi1_sus = sy.Matrix(Pinv[0:2]).dot(sy.Matrix([[x],[y]]))
        xi2_sus = sy.Matrix(Pinv[2:4]).dot(sy.Matrix([[x],[y]]))
        print(xi1_sus)
        print(xi2_sus)
        ec_xy = ec.subs(xi1,xi1_sus)
        ec_xy = ec_xy.subs(xi2, xi2_sus)
        print('ec_xy: {}'.format(ec_xy))

    xrange = np.arange(xlimInf, xlimSup + delta, delta)
    yrange = np.arange(ylimInf, ylimSup + delta, delta)
    X, Y = np.meshgrid(xrange, yrange)
    U, V = a* X + b * Y, c * X + d * Y

    fig = ff.create_quiver(X, Y, U, V, line=dict(width=0.75, color='dodgerblue'))  # campo

    parab = [asintotas(l[i][0],l[i][1],xrange,yrange, ec_xy) for i in range(len(l))]


    fig.add_traces(parab)
    fig.show()
    print('')
