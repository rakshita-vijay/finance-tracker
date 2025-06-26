import os, sys, math, re, csv, pypdf, datetime

from core.budget import changeBudget
# from types_of_methods.csv_saver import save_as_csv
# from types_of_methods.pdf_saver import save_as_pdf

from file_methods.csv_file_methods import display_csv_content

def get_budgets_list():
  with open("core/default_budget.txt", 'r') as f:
    f.seek(0)
    fr = f.read()
  frs = fr.split(', ')
  return frs

def main():
  frs = get_budgets_list()

  mb = re.search(r'monthly = (\d+)', frs[0].strip()).group(1)
  yb = re.search(r'yearly = (\d+)', frs[1].strip()).group(1)

  ch = 'd'
  while ch.lower()[0] != 'y' and ch.lower()[0] != 'n':
    ch = input(f"Do you wish to keep your pre-saved monthly and yearly budgets ({mb} and {yb})? Enter 'y' for yes and 'n' for no: ")

  choice = ch.lower()[0]

  if choice == 'n':
    changeBudget()

  frs = get_budgets_list()

  budgets = {
    'monthly': frs[0].strip('monthly = '),
    'yearly': frs[1].strip('yearly = ')
  }

  print("Budgets:", budgets)

  curr_csv = ""
  curr_pdf = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[0:3] == 'csv':
        curr_csv = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
      else:
        curr_pdf = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))

  todayyy = datetime.datetime.today()

  # checker data
  csv_file = open(curr_csv, mode='w', newline='')
  csv_writer = csv.writer(csv_file, delimiter=',')

  csv_writer.writerow(['col1','col2','col3'])
  csv_writer.writerows([['a','b','c'], ['d','e','f'], ['g','h','i']])
  csv_file.close()

  # transactions
  print("Current transactions: ")
  display_csv_content(curr_csv)



if __name__ == "__main__":
  main()
