import os, sys, datetime
from crewai import Agent, Task, Crew, LLM

from file_methods.csv_file_methods import extract_csv_content
from file_methods.md_file_methods import find_md_file_location
from file_methods.txt_file_methods import create_and_format_pretty_table

from crewai_toolkits_gem_2point0_flash.transform_csv_to_md_table import transformed_table

def gen_report():
  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
  if not GOOGLE_API_KEY:
    raise ValueError("\nGOOGLE_API_KEY environment variable not set. \nPlease set it as a secret in your GitHub repository. \nIf in command line/terminal, run the command: export GOOGLE_API_KEY='YOUR_API_KEY' ")

  llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
  )

  analyser = Agent(
    role = "Transaction Data Analyst",

    goal = '''Gather transaction data from {pretty_table}, which is the pretty table version of the csv file.
    Perform comprehensive analysis of transaction data including:
    - Calculate daily/weekly/monthly transaction totals
    - Identify top 5 largest transactions
    - Detect unusual patterns (e.g., duplicate transactions, abnormal frequencies)
    - Categorize spending patterns
    - Flag potential anomalies''',

    backstory = "Former forensic accountant at Deloitte specializing in transaction pattern detection",

    verbose = True,
    llm = llm
  )

  rep_generator = Agent(
    role = "Financial Report Specialist",
    goal = """Generate comprehensive reports including:
    - Executive summary
    - Analysis period
    - Visual spending breakdowns
    - Anomaly highlights
    - Actionable recommendations
    - Appendices with full data
    Format: Comprehensive Markdown document with section headers.""",
    backstory = "Lead report designer for Fortune 500 financial departments",
    verbose = True,
    llm = llm
  )

  analysis = Task(
    name = "Transaction Analysis",
    agent = analyser,
    description = """Analyze {pretty_table} transaction data and:
    1. Calculate daily transaction volume and value trends
    2. Identify top 3 largest transactions with descriptions
    3. Detect duplicate transactions (same amount/date/description)
    4. Flag transactions exceeding $10,000
    5. Categorize spending into: Groceries, Utilities, Entertainment, etc.
    6. Highlight any date-based anomalies""",
    expected_output = "JSON report with keys: daily_totals, top_transactions, duplicates, large_transactions, spending_categories, anomalies"
  )

  to_do_rep_generation = Task(
    name = "Report Compilation",
    agent = rep_generator,
    description = """Create professional report using analysis from {analysis.output}:
    - Section 0: Executive summary of key findings
    - Section 1: Spending trends (time-based charts)
    - Section 2: Anomaly alerts with risk ratings
    - Section 3: Top 10 transactions table
    - Section 4: Category breakdown pie chart
    - Appendix: Full transaction table from {pretty_table}
    Format: Comprehensive Markdown document with section headers.""",
    expected_output = "Full report in Markdown format with 5 sections and appendix"
  )

  crewww = Crew(
    agents = [analyser, rep_generator],
    tasks = [analysis, to_do_rep_generation],
    process = 'sequential',
    verbose = True,
    chat_llm = llm
  )

  # pretti_table = create_and_format_pretty_table()
  # pretti_table_stringed = pretti_table.get_string()

  data_lines = extract_csv_content()
  t_t_res = transformed_table(data_lines)

  res = crewww.kickoff(inputs = {"pretty_table": t_t_res})

  # find md file location and write to it
  curr_md_path = find_md_file_location()

  tst = datetime.datetime.today()

  with open(curr_md_path, "w") as md_f:
    md_f.write(f"### Report Generated On: {str(tst)}")

  with open(curr_md_path, "a") as md_f:
    md_f.write(" \n\n--- \n")
    md_f.write(((res.raw).strip('```markdown')).strip('```'))

  curr_md_path = find_md_file_location()

  md_f_name = f"md_report_{tst.day}_{tst.month}_{tst.year}_{tst.hour}_{tst.minute}_{tst.second}.md"

  curr_dir = os.getcwd()
  saved_files_path = os.path.join(curr_dir, "saved_files")
  new_md_path = os.path.join(saved_files_path, md_f_name)

  os.rename(curr_md_path, new_md_path)

  print(".md file (with updated timestamp) saved to the 'saved_files' folder! :)")

  return new_md_path

if __name__ == "__main__":
  gen_report()
