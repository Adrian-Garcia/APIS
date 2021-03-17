from file_reader import *

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
    read_file("help_function_points.txt")

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
    f1 = kwargs.get('f1', None)
    factor = kwargs.get('factor', None)

    if conteo_total:
      return conteo_total * (0.65 + 0.01 * f1)

    else:
      if PuntosDeFuncion.conteo_total == 0:
        PuntosDeFuncion.__get_conteo_total(conteo, factor)

      return PuntosDeFuncion.conteo_total * (0.65 + 0.01 * f1)

  def productivity_rate(days, fp, function_points):
    return days / ((fp * function_points) / 1000)

  def __pretty_print_fp(result):
    s = [[str(e) for e in row] for row in result]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

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
    PuntosDeFuncion.__pretty_print_fp(result)

    f1 = kwargs.get('f1', None)
    days = kwargs.get('days', None)
    fp = kwargs.get('fp', None)

    print("Conteo total: {}".format(conteo_total))

    if f1 and days and fp:
      function_points = PuntosDeFuncion.function_points(conteo_total=conteo_total, f1=f1)
      productivity_rate = PuntosDeFuncion.productivity_rate(days, fp, function_points)

      print("PF (Puntos de Funcion) : {}".format(function_points))
      print("Tasa de productividad: {}".format(productivity_rate))
