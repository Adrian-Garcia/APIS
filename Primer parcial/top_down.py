from file_reader import *

class TopDown():
  def help():
    read_file("help_top_down.txt")

  def effort(system_size, productivity_rate):
    return system_size * productivity_rate

  def productivity_rate(effort, system_size):
    return effort / system_size

  def system_size(effort, productivity_rate):
    return effort / productivity_rate
