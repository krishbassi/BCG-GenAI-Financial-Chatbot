# BCG GenAI Financial Chatbot

Financial analysis and rule-based chatbot developed as part of the BCG GenAI Job Simulation on Forage.

## Project Overview

This project analyses 2023–2025 financial statement data for Microsoft, Tesla and Apple using Python and pandas.

I calculated year-on-year changes across key financial metrics, compared company performance and visualised financial trends using Matplotlib. I then used insights from the analysis to develop and test a rule-based financial chatbot.

## Financial Analysis

The analysis examines:

- Total revenue
- Net income
- Total assets
- Total liabilities
- Operating cash flow
- Year-on-year growth

The project uses pandas for data manipulation and analysis and Matplotlib to visualise financial trends across the three companies.

## Financial Chatbot

I developed a Python-based rule-based chatbot capable of responding to predefined financial questions based on the analysis.

The chatbot was tested using supported and unsupported queries to verify both its financial responses and fallback behaviour.

## Technologies Used

- Python
- pandas
- Matplotlib
- Jupyter Notebook

## Skills Demonstrated

- Python programming
- Data manipulation with pandas
- Financial statement analysis
- Data extraction and interpretation
- Data visualisation
- Functions and conditional logic
- Testing and debugging

## Limitations and Future Development

The current chatbot uses exact query matching and hard-coded responses rather than natural language processing or machine learning.

A future version could retrieve answers dynamically from the financial dataset and use NLP to interpret a wider range of user questions.

## Project Files

- `financial_analysis.ipynb` — financial data analysis, year-on-year calculations and visualisations
- `financial_chatbot.ipynb` — chatbot development, testing and documentation
- `financial_chatbot.py` — standalone Python chatbot
- `data/10K_financial_data_2023_2025.csv` — financial dataset used for the analysis

## Acknowledgement

Developed as part of the BCG GenAI Job Simulation on Forage. This repository presents my own code, analysis and documentation produced while completing the simulation.
