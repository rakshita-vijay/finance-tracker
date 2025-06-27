# import pypdf

import os

def find_pdf_file_location():
  curr_pdf = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-4 : len(file)] == '.pdf':
        curr_pdf = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_pdf

# def save_as_pdf(<list of variables or cell values>):
#   pass
#   csv to pdf, basically
#   import, then call this function from pdf_file_saving.py
