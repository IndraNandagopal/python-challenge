# python-challenge

## Background
This assignment is to analyze the financial(PyBank) and election(PyPoll) data using Python. 

### Initial Tasks performed

- Created a new repository for this project called `python-challenge`. 

- Cloned the new repository to my computer.

- Inside my local Git repository, created a folder for each Python assignment and named them as `PyBank` and `PyPoll`.

- In each folder that I just created, added the following content:

    - `main.py`: this will be the main script to run for each analysis.

    - `Resources` folder that contains the CSV files. 

    - `analysis` folder that contains the text file that has the results from my analysis.

- Pushed these changes to GitHub.

### Files Used

- [PyBank_Data](PyBank/Resources/budget_data.csv)

- [PyPoll_Data](PyPoll/Resources/election_data.csv)

### Python Challenge 1 - PyBank

In this Challenge, the task is to create a Python script to analyze the financial records. The financial dataset called budget_data.csv composed of two columns: "Date" and "Profit/Losses".

The Python script analyzed the records to calculate each of the following values:

    The total number of months included in the dataset

    The net total amount of "Profit/Losses" over the entire period

    The changes in "Profit/Losses" over the entire period, and then the average of those changes

    The greatest increase in profits (date and amount) over the entire period

    The greatest decrease in profits (date and amount) over the entire period

### PyBank Output:

Financial Analysis

---------------------------

Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)

* The final script, printed the analysis to the terminal and exported a text file with the results.

### Python Challenge 2 - PyPoll
In this Challenge, the task is to create a Python script to analyze the poll data from a dataset called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The Python script analyzed the votes and calculated each of the following values:

    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote

### PyPoll Output:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

* The final script, printed the analysis to the terminal and exported a text file with the results.
