'''
COCOMO RESOLVER

Un proveedor de software tiene que producir una aplicación que controle una máquina en una fábrica. Se requiere un alto grado de confiabilidad, pues una falla podría dañar a los operadores. Los algoritmos para controlar la maquinaria también son complejos. La confiabilidad y complejidad del producto son muy altas. A la compañía le interesa tomar la oportunidad de aprovechar completamente la inversión que han hecho en el proyecto, reutilizando el sistema de control con algunas modificaciones en futuros contratos. El requerimiento de reutilización es muy alto. Los desarrolladores están familiarizados con la plataforma, así que la posibilidad de problemas potenciales es muy baja. El equipo actual es muy capaz, pero el proyecto es nuevo de alguna manera para todos, por lo que no son tan experimentados. Las herramientas disponibles para los desarrolladores son las típicas para el tamaño de la compañía, y la presión por cumplir con el calendario para llegar a la deadline es lo normal.


Se estima que el tamaño de la aplicación es de 70 puntos de función (FP). 

Considerando por analogía que 1 FP = 1,000 LOC, calcular lo siguiente:

1. Estimar el esfuerzo, tiempo y personal requerido.
2. Indica qué factores (FAE) utilizaste, y el valor de cada factor.
'''

from functools import reduce
import math

organico = { 'aBasico': 2.4, 'aIntermedio': 3.2, 'b': 1.05, 'C': 2.5, 'd': 0.38 }
semiacoplado = { 'aBasico': 3.0, 'aIntermedio': 3.0, 'b': 1.12, 'C': 2.5, 'd': 0.35 }
empotrado = { 'aBasico': 3.6, 'aIntermedio': 2.8, 'b': 1.2, 'C': 2.05, 'd': 0.32 }
tipo_de_sistema = { 'organico': organico, 'semiacoplado': semiacoplado, 'empotrado': empotrado }

tamanio = 70 # Puntos de funcion
unidad_punto_de_funcion = 1000 # LOC
salario_promedio_por_recurso = 4000 # Precio en USD

tipo = 'semiacoplado'
sistema_seleccionado = tipo_de_sistema[tipo]

FAEs_seleccionadas = { 'RELY': 1.4, 'CPLX': 1.65, 'AEXP': 1.13, 'PACAP': 0.7, 'LEXP': 0.95 }
FAE_final = reduce((lambda x, y: x * y), FAEs_seleccionadas.values())

esfuerzo = sistema_seleccionado['aBasico'] * pow(tamanio, sistema_seleccionado['b']) * FAE_final
tiempo = sistema_seleccionado['aBasico'] 
personal_requerido = None

print('FAE final: {}'.format(FAE_final))
print('Esfuerzo: {} pers-mes'.format(esfuerzo))
print('Tiempo: {} meses'.format(tiempo))
print('Personal requerido: {} personas'.format(personas))
