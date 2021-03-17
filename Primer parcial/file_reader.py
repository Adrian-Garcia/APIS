def read_file(file_name):
  file = open(file_name)
  print(file.read())
  file.close()