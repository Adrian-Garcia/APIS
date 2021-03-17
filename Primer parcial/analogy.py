from file_reader import *
import math

class Analogia():
  def help():
    read_file("help_analogy.txt")

  def distance(target_param1, source_param1, target_param2, source_param2):
    return math.sqrt(pow(target_param1 - source_param1, 2) + pow(target_param2 - source_param2, 2))
