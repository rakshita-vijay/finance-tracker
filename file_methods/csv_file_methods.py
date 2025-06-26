import csv, sys
from file_methods.transform_to_table import transformed_table

def display_csv_content(curr_csv):
  csv_file = open(curr_csv, mode='r', encoding='utf-8')
  csv_data = csv.reader(csv_file)
  data_lines = list(csv_data)
  csv_file.close()

  res = transformed_table(data_lines)
  print(res)

# def save_as_csv(<list of variables or cell values>):
#   pass
