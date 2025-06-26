import csv

# def save_as_csv(<list of variables or cell values>):
#   pass

def display_csv_content(curr_csv):
  csv_file = open(curr_csv, mode='r', encoding='utf-8')
  csv_data = csv.reader(csv_file)
  data_lines = list(csv_data)
  print(data_lines)
  csv_file.close()
