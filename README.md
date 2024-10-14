# Python Challenge: PyBank and PyPoll

Module 3 Challenge 

## Overview 
This project involved writing Python scripts to analyse two datasets: one for fdinancial data (PyBank) and another for election data (PyPoll). The goal was to develop scripts thata can read the provided dadtasets, perfom the required analysis, and output the results both in the terminal and as text files. This project demostrdates the use of Python for handing large datasets effieciently, calculating key metrics and exporting results. 

## Project Structure 
├── PyBank/
│   ├── Resources/
│   │   └── budget_data.csv  # Dataset for PyBank analysis
│   ├── analysis/
│   │   └── budget_analysis.txt  # Output text file for PyBank results
│   └── PyBank_starter.py  # PyBank script
├── PyPoll/
│   ├── Resources/
│   │   └── election_data.csv  # Dataset for PyPoll analysis
│   ├── analysis/
│   │   └── election_analysis.txt  # Output text file for PyPoll results
│   └── PyPoll_starter.py  # PyPoll script
└── README.md  # Project description and instructions

## PyBank Analysis 

### Objective 
The Pybank script reads financial data from a CSV file and perfoms the following analysis:
- **Total number of months** in the dataset. 
- **Net total profit/loss** over the entire period. 
- **Average change** in profit/loss between months. 
- **Greatest increase** in profits (date and amount).
- **Greatest decrease** in profits (date and amount).

### Results 
The results are printed in the terminal and saved to the 'budget_analysis_txt'. 
- Example output: Total Months: 86 Total: $38382578 Average Change: $-2315.12 Greatest Increase in Profits: Feb-2012 ($1926159) Greatest Decrease in Profits: Sep-2013 ($-2196167)

## PyPoll Analysis

### Objective 
The Pypoll script analyzes election data to:
- **Calculate the total number of votes**.
- **Determin the total votes and percentage of votes** for each candidate. 
- **Identify the candidate with the most votes** as the winner.

### Results 
The results are printedc in the terminal and saved 'election_analysis.txt' file.
- Example output: Total Votes: 369711 Charles Casper Stockham: 23.049% (85213) Diana DeGette: 73.812% (272892) Raymon Anthony Doane: 3.139% (11606) Winner: Diana DeGette

## Requirements 
Both scripts were written using Python and require the following: 
- **Python 3.12.4**
- **CSV module** (part of Python's standard library)

## How the Code Works 

### PyBank 
- Read 'budget_data.csv' and stores the data in lists. 
- Loops through the data to calculate total months, total profit/loss, and changes between months. 
- Outputs the results both to thed terminal and to 'budget_analysis.txt' file. 

### PyPoll 
- Reads 'election_data.csv' and stores the vote in a dictionary. 
- Loops through the data to tally votes for each candidate. 
- Determines the winner by identifying the candidated with the highest number of votes. 
- Outputs the results to the terminal and to 'election_analysis.txt'.

## Resources and Support 
For this project, I used multiple resources to ensure the successful completion of the assignment: 
- **ChatGPT (AI Assistant)**: For guidance on code logic, debugging, structuring the scripts and formatting my Readme file. 
- **Tutoring Sessions**: I completed a tutoring session to further refine my understanding of coding, project requirements and Github.
- All external resources used are listed here for transparency. 

## Code Cleanliness and Comments 
- Both scripts have been throughly cleaned and commented. 

## Submissions

This repository includes all required files for grading: 
1. 'PyBank' scripts with the 'budget_data.csv' file and output. 
2. 'PyPoll' script with the 'election_data.csv' file and output. 
3. This 'Readme.md' file explaining the project structure, objectives, results and resources used. 

## Acknowledgements

I have completed the project with the assistance of the resources mentioned above and have followed all guidelines for collaboration and external assistance.
