from aux import *
from classifyautoval import *
from classifytracedet import *
from diagramphases import *
from explicit import *
from secondorder import *
from sympyfunctions import *



import plotly.figure_factory as ff
import plotly.graph_objects as go

from flask import Blueprint
from flask import Response

#TODO: linkear con la calculadora


'''----------------PRUEBAS------------'''
# SOLUCIÓN EXPLÍCITA
# sol_explicita(1,3,1,-1) #ejemplo de la documentación
# sol_explicita(1,1,1,1) #ejemplo determinante nulo
# sol_explicita(-1,0,0,-2) #punto estable
# sol_explicita(1,0,0,2) #punto inestable
# sol_explicita(0,1,-1,0) #autovalores complejos puro
# sol_explicita(2,1,-1,2) #autovalores complejos mixto
# sol_explicita(-2,1,-1,-2) #autovalores complejos mixo
# sol_explicita(2,0,0,2) #autovalor repetido
# sol_explicita(1,0,0,1) #autovalor real repetido
# sol_explicita(2,0,3,2) #autovalor real repetido
# sol_explicita(3,2,0,3) #autovalor real repetido

# SEGUNDO ORDEN PASADO A SISTEMA
# segundo_orden(1,-2,-3)

# CLASIFICAR PUNTOS
# clasificar_punto_autoval(1,1,1,1)  #ejemplo determinante nulo
# clasificar_punto_autoval(1,3,1,-1) #punto de silla
# clasificar_punto_autoval(-1,0,0,-2) #punto estable
# clasificar_punto_autoval(1,0,0,2) #punto inestable
# clasificar_punto_autoval(0,1,-1,0) #autovalores complejos puro y centro estable
# clasificar_punto_autoval(2,1,-1,2) #autovalores complejos mixto y foco inestable
# clasificar_punto_autoval(-2,1,-1,-2) #autovalores complejos mixto y foco estable
# clasificar_punto_autoval(1,0,0,1) #autovalor real repetido
# clasificar_punto_autoval(2,0,3,2) #autovalor real repetido
# clasificar_punto_autoval(3,2,0,3) #autovalor real repetido

# print(autovalores([[0,1],[-1,0]]))