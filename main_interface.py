import os, sys, math, re, csv, pypdf, datetime

from core.budget import changeBudget, displayBudget
# from types_of_methods.csv_saver import save_as_csv
# from types_of_methods.pdf_saver import save_as_pdf

from download_to_device import download_file

from file_methods.csv_file_methods import display_csv_content, find_csv_file_location, get_trans_line_details

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
  print("1. Add Transaction(s)")
  print("2. View Spending")
  print("3. Generate Report")
  print("4. Change Budget")
  print("5. Download Report / CSV file / other files")
  print("6. Exit \n")

  repeat = 'yes'
  purpose_of_visit = 0
  while repeat == 'yes' or purpose_of_visit < 1 or purpose_of_visit > 6:
    try:
      purpose_of_visit = int(input(f"Enter a valid choice (1-6): "))
      repeat = 'no'
    except ValueError as ve:
      repeat = 'yes'
      print("\nInvalid input. Please enter a valid integer choice.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Add Transaction
  if purpose_of_visit == 1:

    thro_err = True
    while thro_err == True:
      try:
        num_of_trans = int(input("Enter the number of transactions you wish to add: "))
        thro_err = False

      except Exception as ex:
        # thro_err = True
        print("Invalid numbers of transactions. Retry.")

    trans_deets = []
    for trans_num in range(num_of_trans):
      print(f"Adding transaction #{trans_num+1}: ")
      trans_deets.append(get_trans_line_details())

    # ensures it is a list of lists

    if num_of_trans == 0:
      pass
    else:
      todayyy = datetime.datetime.today()
      add_to_csv(trans_deets, len(trans_deets))


    # not finished yet

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
    purpose_of_visit = 4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Generate Report
  elif purpose_of_visit == 3:
    pass
    # have a choice if they have accidentally pressed 3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Change budget
  if purpose_of_visit == 4:
    choice_to_change_or_keep_current_budget()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Download Report / CSV file / other files
  elif purpose_of_visit == 5:

    # add the choice to also download report
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

  # Exit
  elif purpose_of_visit == 6:
    print("Exiting...")
    sys.exit(1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
under budget or over budget
show budget left
'''
