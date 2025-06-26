import os, sys, math, re, csv, pypdf, datetime

from core.budget import changeBudget, displayBudget
# from types_of_methods.csv_saver import save_as_csv
# from types_of_methods.pdf_saver import save_as_pdf

from download_to_device import download_file

from file_methods.csv_file_methods import display_csv_content, find_csv_file_location

l_only_line_demarcator = "\n{}".format("~" * 120)
r_only_line_demarcator = "{}\n".format("~" * 120)
l_and_r_line_demarcator = "\n{}\n".format("~" * 120)

def get_budgets_list():
  with open("core/default_budget.txt", 'r') as f:
    f.seek(0)
    fr = f.read()
  frs = fr.split(', ')
  return frs

def choice_to_change_or_keep_current_budget():
  bud_list = get_budgets_list()

  print("Current budgets:")
  displayBudget(bud_list)

  ch = 'd'
  while ch.lower()[0] != 'y' and ch.lower()[0] != 'n':
    ch = input(f"\nDo you want to change them? Enter 'y' for yes and 'n' for no: ")

  choice = ch.lower()[0]

  if choice == 'y':
    changeBudget()
    print(l_only_line_demarcator)
  else:
    print(l_only_line_demarcator)

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

  # Add Transaction
  if purpose_of_visit == 1:
    todayyy = datetime.datetime.today()
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # View Spending
  elif purpose_of_visit == 2:
    print(l_and_r_line_demarcator)

    bud_list = get_budgets_list()
    displayBudget(bud_list)
    print()

    curr_csv = find_csv_file_location()

    print("Transactions to date: ")
    display_csv_content(curr_csv)
    print(l_and_r_line_demarcator)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Generate Report
  elif purpose_of_visit == 3:
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Exit
  elif purpose_of_visit == 4:
    print("Exiting...")
    sys.exit(1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  choice_to_change_or_keep_current_budget()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  dl_or_not = 'd'
  print("\nWould you like to download one of the two listed below?")
  print("1. the csv file of your transactions")
  print("2. any other file in this directory")

  while dl_or_not.lower()[0] not in ['y', 'n', '1', '2']:
    dl_or_not = input("\nEnter '1'/'2'/'y' for specific/yes and 'n' for no: ")

  if dl_or_not.lower()[0] == 'y':
    num_ch = '0'
    while num_ch.lower()[0] not in ['1', '2']:
      num_ch = input("\nEnter '1' for csv and '2' for other: ")

    if num_ch.lower()[0] == '1':
      print(l_and_r_line_demarcator)
      download_file()
    else:
      dl_fp = input("\nEnter file path or name in this directory: ")
      print(l_only_line_demarcator)
      download_file(dl_fp)

  elif dl_or_not.lower()[0] == '1':
    print(l_and_r_line_demarcator)
    download_file()

  elif dl_or_not.lower()[0] == '2':
    dl_fp = input("\nEnter file path or name in this directory: ")
    print(l_only_line_demarcator)
    download_file(dl_fp)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  continue_or_not = 'd'
  while continue_or_not.lower()[0] != 'y' and continue_or_not.lower()[0] != 'n':
    continue_or_not = input("\nWould you like to make more changes? Enter 'y' for yes and 'n' for no: ")

  c_or_e = continue_or_not.lower()[0]

  if c_or_e == 'y':
    print(l_only_line_demarcator)
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

'''



if __name__ == "__main__":
  main()



'''
to also accept float values
under budget or over budget
show budget left
auto download of csv onto system
'''
