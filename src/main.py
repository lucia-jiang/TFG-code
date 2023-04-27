# TODO: linkear con la calculadora

'''----------------PRUEBAS------------'''
from src.explicitSFS import sol_explicita
from .sfs import sfs

'''SOLUCIÓN EXPLÍCITA'''
'''Falta especificar los resp'''
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

'''CLASIFICAR PUNTO DE EQUILIBRIO (0,0) POR AUTOVALORES'''
'''Falta especificar los resp'''
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

'''CLASIFICAR PUNTO DE EQUILIBRIO (0,0) POR TRAZA Y DETERMINANTE'''
'''Falta especificar los resp'''
# clasificar_punto_autoval(1,1,1,1)  #ejemplo determinante nulo
# clasificar_traza(1,3,1,-1) #punto de silla
# clasificar_traza(-1,0,0,-2) #punto estable
# clasificar_traza(1,0,0,2) #punto inestable
# clasificar_traza(0,1,-1,0) #autovalores complejos puro y centro estable
# clasificar_traza(2,1,-1,2) #autovalores complejos mixto y foco inestable
# clasificar_traza(-2,1,-1,-2) #autovalores complejos mixto y foco estable
# clasificar_traza(1,0,0,1) #autovalor real repetido
# clasificar_traza(2,0,3,2) #autovalor real repetido
# clasificar_traza(3,2,0,3) #autovalor real repetido
# print(autovalores([[0,1],[-1,0]]))

'''Diagrama de fases'''
# diagramaFase(-3,1,1,-3) #nodo estable
# diagramaFase(2,1,0,-1) #punto de silla
# diagramaFase(1,0,0,2) #nodo inestable
# diagramaFase(2,0,0,2) #punto estelar
# diagramaFase(-4,1,-1,-2) #nodo impropio
# diagramaFase(-2,4,-2,2) #centro estable
# diagramaFase(-2,-3,3,-2) #foco estable
# diagramaFase(2,3,-3,2) #foco inestable


'''Sistema Fundamental de Soluciones'''
# sfs(1,3,1,-1) #ejemplo de la documentación
# sfs(1,1,1,1) #ejemplo determinante nulo
# sfs(-1,0,0,-2) #punto estable
sfs(1,0,0,2) #punto inestable
# sfs(0,1,-1,0) #autovalores complejos puro
# sfs(2,1,-1,2) #autovalores complejos mixto
# sfs(-2,1,-1,-2) #autovalores complejos mixo
# sfs(2,0,0,2) #autovalor repetido
# sfs(1,0,0,1) #autovalor real repetido
# sfs(2,0,3,2) #autovalor real repetido
# sfs(3,2,0,3) #autovalor real repetido