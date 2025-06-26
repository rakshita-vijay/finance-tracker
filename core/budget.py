import re, math

def displayBudget(budget_list):
  mb = re.search(r'monthly = (\d+)', budget_list[0].strip()).group(1)
  yb = re.search(r'yearly = (\d+)', budget_list[1].strip()).group(1)
  print("Monthly budget = {}".format(mb))
  print("Yearly budget = {}".format(yb))

def changeBudget():
  print()

  m_or_y_budget = input("Do you want to enter a monthly or yearly budget? Enter 'm' for monthly and 'y' for yearly: ")
  while (m_or_y_budget.lower()[0] != 'm' and m_or_y_budget.lower()[0] != 'y' ):
    m_or_y_budget = input("Enter a valid budget type - 'm' for monthly and 'y' for yearly: ")

  budget_type = "monthly" if m_or_y_budget.lower()[0] == 'm' else "yearly"

  print()

  repeat = 'yes'
  while repeat == 'yes':
    try:
      budget = int(input(f"Enter your {budget_type} budget: "))
      repeat = 'no'
    except ValueError as ve:
      repeat = 'yes'
      print("\nInvalid input. Please enter a valid number.")

  if budget_type == "monthly":
    monthly_budget = budget
    yearly_budget = math.floor(budget * 12)
    # print("\n{bt} budget = {b}".format(bt = budget_type.title(), b = monthly_budget))
    # print("Yearly budget = {}".format(yearly_budget))
  else:
    monthly_budget = math.floor(budget / 12)
    yearly_budget = budget
    # print("\nMonthly budget = {}".format(monthly_budget))
    # print("{bt} budget = {b}".format(bt = budget_type.title(), b = yearly_budget))

  bl = f"monthly = {monthly_budget}, yearly = {yearly_budget}".split(', ')
  displayBudget(bl)

  f = open("/Users/rakshita/dev/rakshita/finance-tracker/core/default_budget.txt", 'w')
  f.write(f"monthly = {monthly_budget}, yearly = {yearly_budget}")
  f.close()
