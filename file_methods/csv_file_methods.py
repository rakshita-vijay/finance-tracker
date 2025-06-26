import os, csv, sys
from crewai_toolkits_gem_2point0_flash.transform_csv_to_md_table import transformed_table

def extract_csv_content(curr_csv):
  csv_file = open(curr_csv, mode='r', encoding='utf-8')
  csv_data = csv.reader(csv_file)
  data_lines = list(csv_data)
  csv_file.close()
  return data_lines

def display_csv_content(curr_csv):
  data_lines = extract_csv_content(curr_csv)

  res = transformed_table(data_lines)
  print(res)

def find_csv_file_location():
  curr_csv = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-4 : len(file)] == '.csv':
        curr_csv = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_csv

# def add_lines_to_csv(<list of variables or cell values>):
#   pass
