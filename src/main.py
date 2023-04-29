"""----------------PRUEBAS------------"""

"""
RUTAS PARA PROBAR: SFS
/sist/sfs/<a>&<b>&<c>&<d>
http://127.0.0.1:5000/ecsdif/sist/sfs/1&3&1&-1
http://127.0.0.1:5000/ecsdif/sist/sfs/1&1&1&1
http://127.0.0.1:5000/ecsdif/sist/sfs/-1&0&0&2
http://127.0.0.1:5000/ecsdif/sist/sfs/0&1&-1&0 
http://127.0.0.1:5000/ecsdif/sist/sfs/2&1&-1&2
http://127.0.0.1:5000/ecsdif/sist/sfs/2&0&0&2
http://127.0.0.1:5000/ecsdif/sist/sfs/1&0&0&1
http://127.0.0.1:5000/ecsdif/sist/sfs/2&0&3&2
http://127.0.0.1:5000/ecsdif/sist/sfs/3&2&0&3
"""

"""
RUTAS PARA PROBAR: SOLUCIÓN EXPLÍCITA
/sist/sfs/explicit/<a>&<b>&<c>&<d>
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/1&3&1&-1
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/1&1&1&1
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/-1&0&0&2
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/0&1&-1&0 
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/2&1&-1&2
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/2&0&0&2
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/1&0&0&1
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/2&0&3&2
http://127.0.0.1:5000/ecsdif/sist/sfs/explicit/3&2&0&3
"""

"""
RUTAS PARA PROBAR: TRANSFORMAR SEGUNDO ORDEN
/second-order/transform/<a>&<b>&<c>
http://127.0.0.1:5000/ecsdif/second-order/transform/0&3&1
http://127.0.0.1:5000/ecsdif/second-order/transform/1&3&1
http://127.0.0.1:5000/ecsdif/second-order/transform/-1&4&0
http://127.0.0.1:5000/ecsdif/second-order/transform/2&1&-1
"""

"""
RUTAS PARA PROBAR: RESOLVER SEGUNDO ORDEN
/second-order/solve/<a>&<b>&<c>
http://127.0.0.1:5000/ecsdif/second-order/solve/0&3&1
http://127.0.0.1:5000/ecsdif/second-order/solve/1&3&1
http://127.0.0.1:5000/ecsdif/second-order/solve/-1&4&0
http://127.0.0.1:5000/ecsdif/second-order/solve/2&1&-1
"""

"""
RUTAS PARA PROBAR: CLASIFICAR PUNTOS DE EQUILIBRIO POR AUTOVALORES
/classify/eigenvalues/<a>&<b>&<c>&<d>
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/1&3&1&-1 -> pto silla
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/1&1&1&1 -> det nulo
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/-1&0&0&-2 -> punto estable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/1&0&0&2 -> punto inestable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/0&1&-1&0 -> centro estable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/2&1&-1&2 -> foco inestable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/-2&1&-1&-2 -> foco estable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/2&0&0&2 -> punto estelar
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/2&0&3&2 -> nodo impropio inestable
http://127.0.0.1:5000/ecsdif/classify/eigenvalues/-2&0&-3&-2 -> nodo impropio estable
"""

"""
RUTAS PARA PROBAR: CLASIFICAR PUNTOS DE EQUILIBRIO POR TRAZA Y DETERMINANTE
/classify/trace-det/<a>&<b>&<c>&<d>
http://127.0.0.1:5000/ecsdif/classify/trace-det/1&3&1&-1 -> pto silla
http://127.0.0.1:5000/ecsdif/classify/trace-det/1&1&1&1 -> det nulo
http://127.0.0.1:5000/ecsdif/classify/trace-det/-1&0&0&-2 -> punto estable
http://127.0.0.1:5000/ecsdif/classify/trace-det/1&0&0&2 -> punto inestable
http://127.0.0.1:5000/ecsdif/classify/trace-det/0&1&-1&0 -> centro estable
http://127.0.0.1:5000/ecsdif/classify/trace-det/2&1&-1&2 -> foco inestable
http://127.0.0.1:5000/ecsdif/classify/trace-det/-2&1&-1&-2 -> foco estable
http://127.0.0.1:5000/ecsdif/classify/trace-det/2&0&0&2 -> punto estelar
http://127.0.0.1:5000/ecsdif/classify/trace-det/2&0&3&2 -> nodo impropio inestable
http://127.0.0.1:5000/ecsdif/classify/trace-det/-2&0&-3&-2 -> nodo impropio estable
"""

"""
RUTAS PARA PROBAR: CONJUGACIONES TOPOLÓGICAS
/topological-conjugacy/<a1>&<b1>&<c1>&<d>1&<a2>&<b2>&<c2>&<d2>
http://127.0.0.1:5000/ecsdif/topological-conjugacy/1&3&1&-1&1&3&1&-1
http://127.0.0.1:5000/ecsdif/topological-conjugacy/1&1&1&1&1&3&1&-1
http://127.0.0.1:5000/ecsdif/topological-conjugacy/-1&0&0&-2
http://127.0.0.1:5000/ecsdif/topological-conjugacy/1&0&0&2
http://127.0.0.1:5000/ecsdif/topological-conjugacy/0&1&-1&0
"""

