# 💰 Personal Finance Tracker & AI Report Generator

[![Python](https://img.g.shields.img.shieldse](https://img.shields.io/badge/Licensece tracker with AI-powered analysis and multi-format report generation. Built with Python, CrewAI, and Google's Gemini 2.0 Flash for intelligent financial insights.

## 🎯 Project Overview

This finance tracker combines traditional transaction logging with cutting-edge AI analysis to provide strategic financial insights. The system uses a **two-agent CrewAI architecture** powered by **Gemini 2.0 Flash** to analyze spending patterns, detect anomalies, and generate actionable financial recommendations.

### 🔥 Key Highlights
- **AI-Powered Analysis**: Strategic transaction intelligence using Gemini 2.0 Flash
- **Multi-Agent System**: Transaction Intelligence Analyst + Financial Strategy Consultant
- **Multi-Format Support**: CSV, TXT, PDF, and Markdown outputs with auto-synchronization
- **Budget Management**: Monthly/yearly budget tracking with AI-generated recovery strategies
- **Automated File Management**: Smart Downloads folder detection and cleanup operations
- **Clean Architecture**: Modular design with separation of concerns

## ✨ Features

### 📊 Core Financial Tracking
- **7-Field Transaction Management**: S.NO, DATE, DESCRIPTION, AMOUNT, PAYMENT METHOD, STATUS, NOTES
- **Budget Analysis**: Compare spending against monthly/yearly budgets with overspend alerts
- **Multi-Format Exports**: Automatic CSV, TXT, PDF, and MD file generation
- **Real-Time Synchronization**: Auto-update all formats when transactions change
- **Data Validation**: Robust input validation with error handling

### 🤖 AI-Powered Analytics
- **Behavioral Segmentation**: Identify spending patterns (impulse vs planned purchases)
- **Liquidity Risk Analysis**: Calculate days of financial runway
- **Fraud Detection**: Network analysis for anomaly detection
- **Budget Recovery Plans**: AI-generated strategies for overspend scenarios
- **Trend Forecasting**: Year-end financial position projections
- **Payment Method Analysis**: Distribution and effectiveness insights
- **Transaction Status Tracking**: Completion, pending, and failure analysis

### 🛠️ Advanced File Operations
- **Smart Downloads**: Cross-platform Downloads folder detection/creation
- **Bulk Repository Download**: Zip entire repo (excluding __pycache__, README)
- **Format Conversion Pipeline**: Seamless CSV ↔ TXT ↔ PDF ↔ MD conversion
- **Automatic Cleanup**: __pycache__ and temporary zip file deletion
- **Timestamp Management**: Automatic file renaming with precise timestamps
- **File Integrity**: Flush and fsync operations for data safety

### 💡 User Experience
- **Terminal Interface**: Clean, intuitive command-line interaction
- **PrettyTable Visualization**: ASCII tables with proper alignment and formatting
- **Progress Feedback**: Real-time status updates during operations
- **Error Handling**: Comprehensive input validation and exception management
- **Session Management**: Graceful exit with cleanup operations

## 🏗️ Project Structure

```
finance-tracker/
├── 📁 core/                                   # Core application logic
│   ├── 🐍 budget_methods.py                  # Budget management & comparison
│   └── 📄 default_budget.txt                 # Default budget configuration
├── 📁 crewai_toolkits_gem_2point0_flash/     # AI toolkit modules
│   ├── 🐍 generate_report_from_csv.py        # Main AI report generator
│   └── 🐍 transform_csv_to_md_table.py       # CSV to ASCII table converter
├── 📁 file_methods/                          # File processing modules
│   ├── 🐍 csv_file_methods.py               # CSV operations & validation
│   ├── 🐍 md_file_methods.py                # Markdown file handling
│   ├── 🐍 pdf_file_methods.py               # PDF generation (FPDF)
│   └── 🐍 txt_file_methods.py               # Text file & PrettyTable ops
├── 📁 saved_files/                           # Generated files storage
│   ├── 📊 csv_*.csv                         # Transaction data files
│   ├── 📝 txt_version_of_csv_*.txt          # ASCII table versions
│   ├── 📄 pdf_*.pdf                         # PDF reports
│   ├── 📋 md_report_*.md                    # AI analysis reports
│   └── 📋 trial_csv_data                    # Test data template
├── 🎯 main_interface.py                      # 🎯 MAIN ENTRY POINT
├── 📥 download_to_device.py                  # File download utilities
├── 📋 requirements.txt                       # Python dependencies
└── 📖 README.md                             # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+** (Required for CrewAI and modern features)
- **Google Cloud Account** (for Gemini API access)
- **Terminal/Command Line** access

### 1. Clone Repository
```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Google Gemini API
```bash
# Set your Google API key as environment variable
export GOOGLE_API_KEY='your_api_key_here'

# On Windows:
set GOOGLE_API_KEY=your_api_key_here

# On PowerShell:
$env:GOOGLE_API_KEY="your_api_key_here"
```

**Get your API key**: [Google AI Studio](https://ai.google.dev)

### 4. Initialize Default Budget
Edit `core/default_budget.txt`:
```
monthly = 6000, yearly = 72000
```

### 5. Set Up Test Data (Optional)
Copy the contents from `saved_files/trial_csv_data` into a new CSV file for testing:
```csv
S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES
01,28/06/2025,Groceries at SuperMart,45.75,Debit Card,Completed,Weekly shopping
02,28/06/2025,Bookstore purchase,32.99,Credit Card,Completed,Educational
...
```

### 6. Run the Application
```bash
python main_interface.py
```

## 📖 Usage Guide

### Main Menu Options
```
1. Add Transaction(s)     - Input new financial transactions
2. View Spending         - Display transactions and budget status
3. Generate Report       - Create AI-powered financial analysis
4. Change Budget         - Modify monthly/yearly allocations
5. Download Files        - Export files to Downloads folder
6. Wipe Transactions     - Clear all transaction history
7. Exit                  - Clean up and terminate
```

### Adding Transactions
```
Enter the date in MM/DD/YYYY format: 06/28/2025
Enter the description: Coffee at Starbucks
Enter the amount: 5.25
Enter payment method: Credit Card
Enter status: Completed
Enter notes: Morning coffee
```

### Transaction Fields
| Field | Description | Validation |
|-------|-------------|------------|
| **S.NO** | Sequential number (auto-generated) | Auto-increment |
| **DATE** | Transaction date | MM/DD/YYYY format |
| **DESCRIPTION** | Transaction description |  B[Intelligence Analyst]
    B --> C[Strategy Consultant]
    C --> D[Final Report]
    
    B1[Pattern Detection] --> B
    B2[Anomaly Analysis] --> B
    B3[Budget Analysis] --> B
    
    C --> C1[Recovery Plans]
    C --> C2[Recommendations]
    C --> C3[Risk Assessment]
```

**Agent Configuration:**
```python
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
)
```

## 📁 File Format Details

### CSV Structure
```csv
S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES
01,28/06/2025,Groceries at SuperMart,45.75,Credit Card,Completed,Weekly shopping
02,29/06/2025,Coffee at Starbucks,5.25,Cash,Completed,Morning coffee
```

### ASCII Table Output (PrettyTable)
```
+------+------------+----------------------+--------+----------------+-----------+------------------+
| S.NO |    DATE    |     DESCRIPTION      | AMOUNT | PAYMENT METHOD |  STATUS   |      NOTES       |
+------+------------+----------------------+--------+----------------+-----------+------------------+
|  01  | 28/06/2025 | Groceries at Super.. |  45.75 |  Credit Card   | Completed | Weekly shopping  |
|  02  | 29/06/2025 | Coffee at Starbucks  |   5.25 |      Cash      | Completed | Morning coffee   |
+------+------------+----------------------+--------+----------------+-----------+------------------+
```

### AI Report Structure (Markdown)
```markdown
# Financial Analysis Report

## Executive Summary
Key strategic insights and recommendations...

## Behavioral Segmentation Profiles
Customer spending patterns and habits...

## Liquidity Risk Dashboard
Financial health metrics and warnings...

## Fraud Network Mapping
Anomaly detection results and risk factors...

## Expense Optimization Plan
Cost reduction strategies and opportunities...

## Budget Recovery Roadmap
Overspend management with Plan A/B scenarios...

## Appendix
Full transaction table and supporting data...
```

## 🔧 Advanced Features

### Automatic File Management
- **Cross-Platform Downloads Detection**: Windows, macOS, Linux support
- **Timestamp Synchronization**: All files maintain consistent naming `format_DD_MM_YYYY_HH_MM_SS`
- **Format Conversion Pipeline**: 
  ```
  CSV → PrettyTable → TXT → PDF
                  ↓
                 AI Analysis → MD Report
  ```
- **Cleanup Operations**: 
  - Automatic `__pycache__` directory removal
  - Temporary zip file deletion
  - Session cleanup on exit

### Budget Analysis Engine
- **Real-Time Monitoring**: Instant budget threshold detection
- **Recovery Strategy Generation**: 
  - **Plan A**: Full deduction from next month's budget
  - **Plan B**: Proportional reduction across remaining months
- **Projection Models**: End-of-year financial forecasting
- **Category-Specific Analysis**: Spending breakdown by transaction type
- **Impact Assessment**: Overspend effects on annual savings goals

### File Download System
```bash
# Download specific files
python download_to_device.py filename.csv

# Download entire repository (flat structure)
python download_to_device.py all
```

**Features:**
- Automatic zip compression for non-CSV files
- Flat directory structure in Downloads folder
- Exclusion of system files (.git, __pycache__, README)
- Progress feedback and error handling

### Data Validation & Error Handling
- **Date Parsing**: Multiple format support (MM/DD/YYYY, MM-DD-YYYY, etc.)
- **Amount Validation**: Float parsing with negative value support
- **Status Validation**: Enum-based validation for transaction status
- **File Integrity**: `flush()` and `fsync()` operations for data safety
- **Retry Mechanisms**: Automatic retry for file operations

## 🐛 Troubleshooting

### Common Issues

**1. Google API Key Error**
```
ValueError: GOOGLE_API_KEY environment variable not set
```
**Solution**: Set your Google API key as environment variable
```bash
export GOOGLE_API_KEY='your_api_key_here'
```

**2. File Not Found Error**
```
FileNotFoundError: No such file or directory
```
**Solution**: Ensure you're running from the project root directory and `saved_files/` exists

**3. CrewAI JSON Parsing Error**
```
JSON parsing error: Expecting value: line 1 column 1 (char 0)
```
**Solution**: Check internet connection and API quota; restart application

**4. Permission Denied (Downloads)**
```
PermissionError: Access denied
```
**Solution**: Run with appropriate file system permissions or check Downloads folder accessibility

**5. PrettyTable Formatting Issues**
```
UnicodeEncodeError: 'ascii' codec can't encode
```
**Solution**: Ensure terminal supports UTF-8 encoding or use ASCII-only characters

### Performance Optimization Tips
- Keep CSV files under 1000 transactions for optimal AI processing
- Use SSD storage for faster file operations
- Close other applications during report generation
- Set terminal encoding to UTF-8 for proper table display

### Debug Mode
Enable verbose logging by modifying agent settings:
```python
verbose = True  # In generate_report_from_csv.py
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Install development dependencies: `pip install -r requirements.txt`
4. Run tests with sample data from `trial_csv_data`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open Pull Request

### Code Style Guidelines
- Follow PEP 8 guidelines for Python code
- Use descriptive variable names (`curr_csv_path` not `cp`)
- Add docstrings for complex functions
- Maintain modular architecture with clear separation
- Test with provided `trial_csv_data` before submitting

### Testing
Use the provided test data:
```bash
# Copy trial_csv_data contents to a new CSV file
cp saved_files/trial_csv_data saved_files/test_transactions.csv
python main_interface.py
```

## 📚 Technical Resources

### Documentation Links
- [CrewAI Documentation](https://docs.crewai.com/)
- [Google Gemini API Guide](https://ai.google.dev/docs)
- [PrettyTable Documentation](https://pypi.org/project/prettytable/)
- [FPDF User Manual](https://pyfpdf.readthedocs.io/)

### Research Papers & Articles
- [Multi-Agent Systems in Finance](https://arxiv.org/abs/2301.07515)
- [LLM Applications in Financial Analysis](https://arxiv.org/abs/2310.12659)

### Example Implementations
- [Personal Finance Tracker Examples](https://github.com/Firdous2307/personal-finance-tracker)
- [CrewAI Multi-Agent Examples](https://github.com/DAEM007/finance-tracker-project)

## 🏷️ Technical Tags

`Multi-Agent AI` `Financial Analysis` `Python` `CrewAI` `Gemini 2.0 Flash` `Budget Management` `Report Generation` `Terminal Application` `CSV Processing` `PDF Generation` `Markdown Reports` `ASCII Tables` `File Management` `Auto-Synchronization` `Downloads Management` `Format Conversion` `Cleanup Automation` `Strategic Analytics` `Behavioral Analysis` `Fraud Detection` `Liquidity Analysis` `PrettyTable` `FPDF` `Zipfile Operations` `Prompt Engineering` `AI Agents` `LLM Integration`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Quick Links

- **Google AI Studio**: [ai.google.dev](https://ai.google.dev)
- **CrewAI Framework**: [crewai.com](https://crewai.com)
- **Gemini 2.0 Flash**: [Google Blog](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)
- **Project Issues**: [GitHub Issues](https://github.com/your-username/finance-tracker/issues)

## 🎯 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
pip install -r requirements.txt

# Set API key
export GOOGLE_API_KEY='your_api_key_here'

# Run application
python main_interface.py

# Download all files
python download_to_device.py all
```

**Built with ❤️ using Python, AI, and lots of coffee ☕**

> *"Transforming personal finance through intelligent automation and strategic AI insights"*

**🌟 Star this repo if it helped you manage your finances better!**

[1] https://pplx-res.cloudinary.com/image/private/user_uploads/53367127/d132da1a-a1bd-4f9f-9542-61562ddd9a67/Screenshot-2025-06-28-at-11.36.52-PM.jpg
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/aaaea074-acb9-439a-8230-4ea819d6baa9/budget_methods.py
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/92aca27f-865f-4d1b-af7c-a6e6bf5730ed/csv_file_methods.py
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/41942093-88f0-4f86-9856-e5f9ec410df0/default_budget.txt
[5] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/42b46bbf-512a-4a38-8a73-079c9e83bddf/download_to_device.py
[6] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/2e3730b5-a6ef-4984-a6e5-6193aa9f9305/generate_report_from_csv.py
[7] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/194e9ebb-8de8-4c3a-b2f6-f48d32fbf168/main_interface.py
[8] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/bd3e0db3-9ee3-4517-b63c-a98e1cd617e0/md_file_methods.py
[9] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/2b8232d2-d285-447a-a406-8c3fc73cb56e/pdf_file_methods.py
[10] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/feb6ce05-5968-43ad-ac9a-1eff3fa07c30/requirements.txt
[11] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/5049ffdb-971b-4b81-94fd-16e62ba54f62/transform_csv_to_md_table.py
[12] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/94addd9f-26b9-4b14-8542-67ca5d3545e2/trial_csv_data
[13] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/53367127/19efd7de-ff32-4a97-91b3-467684b80110/txt_file_methods.py
[14] https://github.com/Firdous2307/personal-finance-tracker
[15] https://github.com/DAEM007/finance-tracker-project
[16] https://community.crewai.com/t/automated-project-notebook-gemini/2441
[17] https://github.com/Keonleebv/FinanceTracker
[18] https://github.com/lucaspoli/sonda-ai
[19] https://www.thebricks.com/resources/how-to-build-a-personal-finance-tracker-in-spreadsheets-using-ai
[20] https://www.ijsrtjournal.com/article/AI-Powered-Expense--Budget-Tracker-A-Web-Based-Financial-Planning-System
[21] https://www.youtube.com/watch?v=gvUsUpDlav4
[22] https://expenseai.app
[23] https://ijarcce.com/wp-content/uploads/2025/03/IJARCCE.2025.14364.pdf
