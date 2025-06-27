import os, csv, sys, datetime
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

def get_trans_line_details():
  csv_file_loc = find_csv_file_location() # gives full path
  csv_file_lines = extract_csv_content() # gives list of lists

  tran_done = csv_file_lines - 1 # because heading also exists
  curr_tran = tran_done + 1 # current transaction

  fields = ['S.NO', 'DATE', 'DESCRIPTION', 'AMOUNT', 'NOTES']
  responses = []
  responses.append(curr_tran)

  # formet: ['int', 'MM/DD/YYYY', 'text (<70 characters)', 'float', 'text (<70 characters)']

  # DATE
  thro_err = True
  while thro_err == True:
    try:
      resp = input("Enter the date in MM/DD/YYYY format: ")
      stripped_resp = resp.strip()

      if len(stripped_resp) > len('MM/DD/YYYY'):
        raise Exception

      # frmt_to_srch = r'(\d{2})(\D)(\d{2})(\D)(\d{2}\d{2}?)'

      if len(stripped_resp) == len('MM/DD/YYYY'):
        frmt_to_srch = r'(\d{2})(\D)(\d{2})(\D)(\d{4})'
      elif len(stripped_resp) == len('MM/DD/YY'):
        frmt_to_srch = r'(\d{2})(\D)(\d{2})(\D)(\d{2})'
      else:
        raise Exception

      if re.search(frmt_to_srch, stripped_resp) == None:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("Invalid date format. Retry.")

  responses.append(stripped_resp)

  # DESCRIPTION
  thro_err = True
  while thro_err == True:
    try:
      resp = input("Enter the description as text (<70 characters): ")
      stripped_resp = resp.strip()

      if len(stripped_resp) > 70:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("Message is too long. Retry.")

  responses.append(stripped_resp)

  # AMOUNT
  thro_err = True
  while thro_err == True:
    try:
      resp = float(input("Enter the amount as a float number (xx.yyy): "))
      thro_err = False

    except Exception as ex:
      # thro_err = True
      print("Invalid amount format. Retry.")

  responses.append(resp)

  # NOTES
  thro_err = True
  while thro_err == True:
    try:
      resp = input("Enter notes (if there are any) as text (<70 characters): ")
      stripped_resp = resp.strip()

      if len(stripped_resp) > 70:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("Message is too long. Retry.")

  responses.append(stripped_resp)

  return responses

def add_to_csv(list_or_listOfLists, list_len):
  csv_file = open(curr_csv, mode='a', encoding='utf-8')
  csv_wrtr = csv.writer(csv_file)

  if list_len == 1:
    csv_wrtr.writerow(list_or_listOfLists[0])
  else:
    csv_wrtr.writerows(list_or_listOfLists)

  csv_file.close()


# def add_lines_to_csv(<list of variables or cell values>):
#   pass
