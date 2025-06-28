import os, sys
from crewai import Agent, Task, Crew, LLM

from file_methods.csv_file_methods import find_csv_file_location
from file_methods.txt_file_methods import create_and_format_pretty_table

def gen_report(csv_file_loc_full_path = find_csv_file_location()):
  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
  if not GOOGLE_API_KEY:
    raise ValueError("\nGOOGLE_API_KEY environment variable not set. \nPlease set it as a secret in your GitHub repository. \nIf in command line/terminal, run the command: export GOOGLE_API_KEY='YOUR_API_KEY' ")

  llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
  )

  analyser = Agent(
    role = '''Given the data {pretti_table_stringed}, which is the pretty table version of the csv file, analyse the contents''',
    goal = "",
    backstory = "",
    verbose = True,
    llm = llm
  )

  rep_generator = Agent(
    role = "",
    goal = "",
    backstory = "",
    verbose = True,
    llm = llm
  )

  analysis = Task(
    name = "",
    agent = rep_generator,
    description = "",
    expected_output = ""
  )

  to_do_rep_generation = Task(
    name = "",
    agent = rep_generator,
    description = "",
    expected_output = ""
  )

  crewww = Crew(
    agents = [analyser, rep_generator],
    tasks = [analysis, to_do_rep_generation],
    process = 'sequential',
    verbose = True,
    chat_llm = llm
  )

  pretti_table = create_and_format_pretty_table()
  pretti_table_stringed = pretti_table.get_string()

  res = crewww.kickoff(inputs = {"full_file_path": csv_file_loc_full_path, "pretty_table": pretti_table_stringed})

  # save directly to ./saved_files
  # then ask, if user also wants it downloaded





























# also ask if user wants to download it
# it will be generated as a markdown file

# from download_to_device import download_file
# download_file(generated_md_file_report)

if __name__ == "__main__":
  gen_report(find_csv_file_location())
