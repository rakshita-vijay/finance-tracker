
import os, sys
from crewai import Agent, Task, Crew, LLM

def get_max_width_of_each_column(csv_dataaaa):
  fields = csv_dataaaa[0]
  max_width_of_each_column = {field: 3 for field in fields}

  for col_no in range(len(fields)):
    for row_no in range(len(csv_dataaaa)):
      cell_data = str(csv_dataaaa[row_no][col_no])

      if len(cell_data) > max_width_of_each_column[fields[col_no]]-2:
        max_width_of_each_column[fields[col_no]] = len(cell_data) + 2

  return max_width_of_each_column

def transformed_table(data_lines):
  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
  if not GOOGLE_API_KEY:
    raise ValueError("\nGOOGLE_API_KEY environment variable not set. \nPlease set it as a secret in your GitHub repository. \nIf in command line/terminal, run the command: export GOOGLE_API_KEY='YOUR_API_KEY' ")

  llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
  )

  table_generator = Agent(
    role = "2D Array to ASCII Table Converter",

    goal = '''Given a 2D array (list of lists) called {csv_data}, convert it into a classic ASCII table for terminal/plain text viewing.
    The table must use pipes (|) to separate columns and dashes (-) for horizontal lines.
    Left-align all text columns. Right-align all numeric columns.
    Each column should be as wide as the values mentioned against the column name in {maximum_width_of_each_column}.
    Do not use Markdown table syntax. Do not center-align any columns.''',

    backstory = "You are an expert at formatting data into readable, fixed-width ASCII tables for terminal or plain text viewing. You only use ASCII with pipes and spaces for padding and alignment.",

    llm = llm,
    verbose = False
  )

  table_maker = Task(
    name = "ASCII Table Converter",
    agent = table_generator,

    description = '''Given a 2D array (list of lists) called {csv_data}, convert it into a visually pleasing ASCII table using pipes (|) to separate columns and dashes (-) for horizontal lines.
    Each column should be as wide as the values mentioned against the column name in {maximum_width_of_each_column}.
    Left-align all text columns (S.NO, DATE, DESCRIPTION, NOTES). Right-align all numeric columns (AMOUNT, S.NO if numeric).
    Pad each cell with spaces so that all rows and columns align perfectly.
    Instead, produce a classic ASCII table like:
    | S.NO |    DATE    | DESCRIPTION            | AMOUNT | NOTES          |
    |------|------------|------------------------|--------|----------------|
    | 1    | 12-12-12   | d1                     |    1.0 | n1             |
    | 2    | 07/08/2009 | Parking fee            |   12.0 | Downtown       |
    | 3    | 12/31/2025 | Invalid date corrected |    0.0 | winchesterlove |
    ''',

    expected_output = "A properly aligned ASCII table as described above, with left-aligned text and right-aligned numbers."
  )

  crewww = Crew(
    agents = [table_generator],
    tasks = [table_maker],
    verbose = False,
    chat_llm = llm
  )

  max_width_of_each_column = get_max_width_of_each_column(data_lines)

  resp = crewww.kickoff(inputs={"csv_data": data_lines, "maximum_width_of_each_column": max_width_of_each_column})
  return resp.raw.strip('```')
