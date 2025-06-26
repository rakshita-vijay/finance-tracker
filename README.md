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
