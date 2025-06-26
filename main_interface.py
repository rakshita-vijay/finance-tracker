import os, sys, math, re, csv, pypdf, datetime

from core.budget import changeBudget, displayBudget
# from types_of_methods.csv_saver import save_as_csv
# from types_of_methods.pdf_saver import save_as_pdf

from file_methods.csv_file_methods import display_csv_content

def get_budgets_list():
  with open("core/default_budget.txt", 'r') as f:
    f.seek(0)
    fr = f.read()
  frs = fr.split(', ')
  return frs

def find_csv_file_location():
  curr_csv = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[0:3] == 'csv':
        curr_csv = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_csv

def choice_to_change_or_keep_current_budget():
  bud_list = get_budgets_list()

  # mb = re.search(r'monthly = (\d+)', bud_list[0].strip()).group(1)
  # yb = re.search(r'yearly = (\d+)', bud_list[1].strip()).group(1)

  ch = 'd'
  while ch.lower()[0] != 'y' and ch.lower()[0] != 'n':
    print("Current budgets:")
    displayBudget(bud_list)
    ch = input(f"\nDo you want to change them? Enter 'y' for yes and 'n' for no: ")

  choice = ch.lower()[0]

  if choice == 'y':
    changeBudget()
    print("\n{}".format("~" * 120))
  else:
    print("\n{}".format("~" * 120))

def main():
  print("\nWhat are you here to do?")
  print("1. Add Transaction")
  print("2. View Spending")
  print("3. Generate Report")
  print("4. Exit \n")

  repeat = 'yes'
  purpose_of_visit = 0
  while repeat == 'yes' or purpose_of_visit < 1 or purpose_of_visit > 4:
    try:
      purpose_of_visit = int(input(f"Enter a valid choice (1-4): "))
      repeat = 'no'
    except ValueError as ve:
      repeat = 'yes'
      print("\nInvalid input. Please enter a valid integer choice.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  if purpose_of_visit == 1:
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  elif purpose_of_visit == 2:
    print("\n{}\n".format("~" * 120))

    bud_list = get_budgets_list()
    displayBudget(bud_list)
    print()

    curr_csv = find_csv_file_location()

    print("Transactions to date: ")
    display_csv_content(curr_csv)
    print("\n{}\n".format("~" * 120))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  elif purpose_of_visit == 3:
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  elif purpose_of_visit == 4:
    print("Exiting...")
    sys.exit(1)

  choice_to_change_or_keep_current_budget()

  continue_or_not = 'd'
  while continue_or_not.lower()[0] != 'y' and continue_or_not.lower()[0] != 'n':
    continue_or_not = input("\nWould you like to make more changes? Enter 'y' for yes and 'n' for no: ")

  c_or_e = continue_or_not.lower()[0]

  if c_or_e == 'y':
    print("\n{}".format("~" * 120))
    main()
  else:
    print("Exiting...")
    sys.exit(1)
















'''
  bud_list = get_budgets_list()

  budgets = {
    'monthly': bud_list[0].strip('monthly = '),
    'yearly': bud_list[1].strip('yearly = ')
  }

  # csv_fp = open(curr_csv, 'w', encoding='utf-8')
  # csv_writer = csv.writer(csv_fp)
  # csv_writer.writerow(['S.NO', 'DATE', 'DESCRIPTION', 'AMOUNT', 'NOTES'])
  # # csv_writer.writerows([['S.NO', 'DATE', 'DESCRIPTION', 'AMOUNT', 'NOTES']])
  # csv_fp.close()

  # transactions


  todayyy = datetime.datetime.today()


'''





if __name__ == "__main__":
  main()
