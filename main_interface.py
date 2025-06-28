import os, sys, math, re, csv, pypdf, datetime, shutil

from core.budget_methods import get_budgets_list, changeBudget, displayBudget
# from types_of_methods.csv_saver import save_as_csv
# from types_of_methods.pdf_saver import save_as_pdf

from download_to_device import download_file, delete_pychache

from file_methods.csv_file_methods import display_csv_content, find_csv_file_location, get_trans_line_details, add_to_csv

from file_methods.txt_file_methods import find_txt_file_location, update_txt_file, create_and_format_pretty_table

from file_methods.pdf_file_methods import find_pdf_file_location
from file_methods.md_file_methods import find_md_file_location

from crewai_toolkits_gem_2point0_flash.generate_report_from_csv import gen_report

# from prettytable import from_csv, PrettyTable

l_only_line_demarcator = "\n{}".format("~" * 120)
r_only_line_demarcator = "{}\n".format("~" * 120)
l_and_r_line_demarcator = "\n{}\n".format("~" * 120)

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
  print("6. Wipe Transactions")
  print("7. Exit \n")

  repeat = 'yes'
  purpose_of_visit = 0
  while repeat == 'yes' or purpose_of_visit < 1 or purpose_of_visit > 7:
    try:
      purpose_of_visit = int(input(f"Enter a valid choice (1-7): "))
      repeat = 'no'
    except ValueError as ve:
      repeat = 'yes'
      print("\nInvalid input. Please enter a valid integer choice.")

  print(l_and_r_line_demarcator)

  global_pretti_tabel = create_and_format_pretty_table()
  update_txt_file(global_pretti_tabel)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Add Transaction
  if purpose_of_visit == 1:

    num_of_trans = 1
    thro_err = True
    while thro_err == True:
      try:
        num_of_trans = int(input("Enter the number of transactions you wish to add: "))
        thro_err = False

      except Exception as ex:
        # thro_err = True
        print("Invalid numbers of transactions. Retry.")

    print()
    trans_deets = []
    for trans_num in range(num_of_trans):
      print(f"ADDING TRANSACTION #{trans_num+1}: ")
      print("-" * len(f"ADDING TRANSACTION #{trans_num+1}"))

      trans_deets.append(get_trans_line_details())

      print()
      print("-" * len(f"| TRANSACTION #{trans_num+1} HAS BEEN RECORDED! |"))
      print(f"| TRANSACTION #{trans_num+1} HAS BEEN RECORDED! |")
      print("-" * len(f"| TRANSACTION #{trans_num+1} HAS BEEN RECORDED! |"))
      print()

    # ensures it is a list of lists

    if num_of_trans == 0:
      pass
    else:
      add_to_csv(trans_deets)
      rn_ts = datetime.datetime.today()

      # renaming the .csv file
      new_name = f"csv_{rn_ts.day}_{rn_ts.month}_{rn_ts.year}_{rn_ts.hour}_{rn_ts.minute}_{rn_ts.second}.csv"

      curr_fp = find_csv_file_location()
      # /Users/rakshita/dev/rakshita/finance-tracker/saved_files/csv_26_06_2025_3_48_10.csv
      dir_path = os.path.join(curr_fp.split('saved_files/')[0], 'saved_files/')
      new_fp = os.path.join(dir_path, new_name)

      os.rename(curr_fp, new_fp)

      # renaming the .pdf file
      new_name = f"pdf_{rn_ts.day}_{rn_ts.month}_{rn_ts.year}_{rn_ts.hour}_{rn_ts.minute}_{rn_ts.second}.pdf"

      curr_fp = find_pdf_file_location()
      dir_path = os.path.join(curr_fp.split('saved_files/')[0], 'saved_files/')
      new_fp = os.path.join(dir_path, new_name)

      os.rename(curr_fp, new_fp)

      print("-" * len("| Transactions successfully added into the csv file! :) |"))
      print("| Transactions successfully added into the csv file! :) |")
      print("-" * len("| Transactions successfully added into the csv file! :) |"))

    pretti_tabel = create_and_format_pretty_table()
    update_txt_file(pretti_tabel)

    print(l_only_line_demarcator)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # View Spending
  elif purpose_of_visit == 2:

    bud_list = get_budgets_list()
    displayBudget(bud_list)
    print()

    curr_csv = find_csv_file_location()

    print("Transactions to date: ")
    display_csv_content(curr_csv)

    # with open(curr_csv, "r") as fp:
    #   table = from_csv(fp)
    #   table.align = "l"  # left align all columns
    #   print(table)

    # pt = create_and_format_pretty_table()
    # print(pt)
    # update_txt_file(pt)

    print(r_only_line_demarcator)
    purpose_of_visit = 4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Generate Report
  elif purpose_of_visit == 3:
    # rep_ch = input("Would you like to generate a report / analysis of your transactions? Enter 'y' for yes and 'n' for no: ")
    # while rep_ch.lower()[0] != 'y' and rep_ch.lower()[0] != 'n':
    #   rep_ch = input("Invalid choice. Please enter 'y' for yes and 'n' for no: ")

    # if rep_ch.lower()[0] == 'y':
    new_md_path = gen_report()

    print(l_and_r_line_demarcator)

    d_md_or_not = input("Would you also like to download the .md file to the Downloads folder on your device? Enter 'y' for yes and 'n' for no: ")

    if d_md_or_not.lower()[0] == 'y':
      download_file(new_md_path)
      print(l_only_line_demarcator)
    else:
      print()
      print("Your .md file is available in the 'saved_files' directory.")
      print(l_only_line_demarcator)

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
    print("Would you like to download one of the files listed below?")
    print("1. the csv file of your transactions")
    print("2. the txt file of your transactions")
    print("3. the pdf file of your transactions")
    print("4. the md file of your report")
    print("5. any other file in this directory")

    while dl_or_not.lower()[0] not in ['y', 'n', '1', '2', '3', '4', '5']:
      dl_or_not = input("\nEnter 'y'/'1'/'2'/'3'/'4'/'5' for yes/specific and 'n' for no: ")

    if dl_or_not.lower()[0] == 'y':
      dl_or_not = '0'
      while dl_or_not.lower()[0] not in ['1', '2', '3', '4', '5']:
        dl_or_not = input("\nEnter a number from 1 to 5: ")

    if dl_or_not.lower()[0] == '1':
      print(l_and_r_line_demarcator)
      download_file()

    elif dl_or_not.lower()[0] == '2':
      txt_file_path = find_txt_file_location()
      print(l_only_line_demarcator)
      download_file(txt_file_path)

    elif dl_or_not.lower()[0] == '3':
      pdf_file_path = find_pdf_file_location()
      print(l_only_line_demarcator)
      download_file(pdf_file_path)

    elif dl_or_not.lower()[0] == '4':
      pass
      md_file_path = find_md_file_location()
      print(l_only_line_demarcator)
      download_file(md_file_path)

    elif dl_or_not.lower()[0] == '5':
      dl_fp = input("\nEnter file path or name in this directory: ")
      print(l_only_line_demarcator)
      download_file(dl_fp)

    print(l_only_line_demarcator)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Wipe transactions
  elif purpose_of_visit == 6:
    ch_wipe = input("Are you sure you want to wipe all your transaction history? Enter 'y' for yes and 'n' for no: ")

    if ch_wipe.lower()[0] == 'y':
      wipe_loc = find_csv_file_location()
      with open(wipe_loc, "w", encoding='utf-8') as wipe_loc_wrtr:
        csv_wiper = csv.writer(wipe_loc_wrtr)
        csv_wiper.writerow(['S.NO','DATE','DESCRIPTION','AMOUNT','PAYMENT METHOD','STATUS','NOTES'])

    pretti_tabel = create_and_format_pretty_table()
    update_txt_file(pretti_tabel)

    print(l_only_line_demarcator)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # Exit
  elif purpose_of_visit == 7:
    delete_pychache()
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
    delete_pychache()
    pretti_tabel = create_and_format_pretty_table()
    update_txt_file(pretti_tabel)
    print("Exiting...")
    sys.exit(1)

if __name__ == "__main__":
  main()
