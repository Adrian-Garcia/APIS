# from repaso_parcial import *
import math

def read_file(file_name):
  return open(file_name).read()

help = read_file("help.txt")

class TopDown():
  def help():
    print("--------------------------------TOP DOWN-------------------------------")
    print("Calcula atributos basados en lienas de código\n")
    
    print("Atributos disponibles para calcular:")
    print("  System size: Cuanto trabajo se requiere realizar")
    print("  Productivity rate: La tasa de trabajo en la que se realiza la actividad")
    print("  Productivity rate: Tamanio del sistema en lineas de código (LOC)\n")
    
    print("Funciones disponibles: ")
    print("  effort(system_size, productivity_rate)")
    print("  productivity_rate(effort, system_size)")
    print("  system_size(effort, productivity_rate)\n")

  def effort(system_size, productivity_rate):
    return system_size * productivity_rate

  def productivity_rate(effort, system_size):
    return effort / system_size

  def system_size(effort, productivity_rate):
    return effort / productivity_rate

class Analogia():
  def help():
    print("--------------------------------ANALOGIA-------------------------------")
    print("")

  def distance(target_param1, source_param1, target_param2, source_param2):
    return math.sqrt(pow(target_param1 - source_param1, 2) + pow(target_param2 - source_param2, 2))

class PuntosDeFuncion():
  factorDePonderacion = [
    [3,  4,  6],    # EE  Número de entradas externas
    [4,  5,  7],    # SE  Número de salidas externas
    [3,  4,  6],    # CE  Número de consultas externas
    [7,  10, 15],   # ALI Número de archivos lógicos internos
    [5,  7,  10]    # AIE Número de archivos de interfaz externos
  ]

  valorDelDominioDeInformacion = [
    "EE", "SE", "CE", "ALI", "AIE"
  ]

  conteo_total = 0

  def help():
    print("----------------------------PUNTOS DE FUNCION--------------------------")

  def __factor_index(factor):
    if factor.lower() == "simple":
      return 0
    elif factor.lower() == "promedio":
      return 1
    elif factor.lower() == "complejo":
      return 2
    else:
      return -1

  def __get_conteo_total(conteo, factor):
    index_factor = PuntosDeFuncion.__factor_index(factor)

    if index_factor == -1:
      print("Factor desconocido")
      return

    conteo_total = 0

    for i in range(5):
      conteo_total += conteo[i] * PuntosDeFuncion.factorDePonderacion[i][index_factor]

    PuntosDeFuncion.conteo_total = conteo_total

  def function_points(**kwargs):
    conteo_total = kwargs.get('conteo_total', None)
    conteo = kwargs.get('conteo', None)
    scenario = kwargs.get('scenario', None)
    factor = kwargs.get('factor', None)

    if conteo_total != None:
      return conteo_total * (0.65 + 0.01 * scenario)

    else:
      if PuntosDeFuncion.conteo_total == 0:
        PuntosDeFuncion.__get_conteo_total(conteo, factor)

      return PuntosDeFuncion.conteo_total * (0.65 + 0.01 * scenario)

  def function_points_analysis(conteo, factor, **kwargs):
    index_factor = PuntosDeFuncion.__factor_index(factor)

    if index_factor == -1:
      print("Factor desconocido")
      return

    conteo_total = 0
    result = [["ValorDominio", "Conteo", "Simple", "Promedio", "Complejo", "Total"]]
    factorDePonderacion = PuntosDeFuncion.factorDePonderacion
    valorDelDominioDeInformacion = PuntosDeFuncion.valorDelDominioDeInformacion

    for i in range(5):
      valor = valorDelDominioDeInformacion[i]
      cont = conteo[i]
      simple = factorDePonderacion[i][0]
      promedio = factorDePonderacion[i][1]
      complejo = factorDePonderacion[i][2]
      total = cont * factorDePonderacion[i][index_factor]
      result.append([valor, cont, simple, promedio, complejo, total])
      conteo_total += total

    PuntosDeFuncion.conteo_total = conteo_total

    s = [[str(e) for e in row] for row in result]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("conteo_total: {}".format(conteo_total))

    scenario = kwargs.get('scenario', None)    
    if scenario:
      print("PF (Puntos de Funcion) : {}".format(PuntosDeFuncion.function_points(conteo_total=conteo_total, scenario=scenario)))

  def productivity_rate():
    pass

# print(PuntosDeFuncion.function_points(conteo=[4,2,1,2,2], scenario=44, factor="promedio"))
# print(PuntosDeFuncion.function_points_analysis([4,2,1,2,2], "promedio", scenario=44))