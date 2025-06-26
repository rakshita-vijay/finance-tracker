def transformed_table(data_lines):
  import os, sys
  from crewai import Agent, Task, Crew, LLM

  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
  if not GOOGLE_API_KEY:
    raise ValueError("\nGOOGLE_API_KEY environment variable not set. \nPlease set it as a secret in your GitHub repository. \nIf in command line/terminal, run the command: export GOOGLE_API_KEY='YOUR_API_KEY' ")

  llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
  )

  table_generator = Agent(
    role = "2D Array to Table Converter",
    goal = "Given a 2D Array (list of lists) - {csv_data} - you must convert into a table of 'markdown' format, with spaces and pipes (|).",
    backstory = "Automatic spacer and demarcator using spaces and |",
    llm = llm,
    verbose = False
  )

  table_maker = Task(
    name = "Table Converter",
    agent = table_generator,
    description = "Given a 2D Array (list of lists) - {csv_data} - you must convert into a table of 'markdown' format, with spaces and pipes (|). The width of each column will be the width of the longest value in that specific column. Return the visually pleasing, appropriately spaced table of values, not the python script used to convert it.",
    expected_output = "Visually pleasing, appropriately spaced table of values."
  )

  crewww = Crew(
    agents = [table_generator],
    tasks = [table_maker],
    verbose = False,
    chat_llm = llm
  )

  resp = crewww.kickoff(inputs={"csv_data": data_lines})
  return resp.raw.strip('```')
