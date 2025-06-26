```bash
finance_tracker/
├── core/                  # Business logic (OOP)
│   ├── __init__.py
│   ├── transaction.py     # Transaction class
│   ├── budget.py          # Budget class
│   ├── analyzer.py        # Spending analysis
│   └── storage.py         # CSV persistence
├── interfaces/
│   ├── cli_app.py         # Terminal interface
│   └── streamlit_app.py   # Web interface
├── reports/
│   ├── pdf_generator.py   # PDF export
│   └── visualizations.py  # Matplotlib/Seaborn
├── data/                  # CSV storage directory
└── tests/                 # Unit tests
```

---

end:

downloads_folder = ''

f = open('file_locations.txt', 'w')
f.write("CSV file location: {}".format(csv_file_loc))
f.close()

f = open('file_locations.txt', 'a')
f.write("PDF file location: {}".format(pdf_file_loc))
f.close()

f = open("transactions.csv", encoding = "utf-8")
