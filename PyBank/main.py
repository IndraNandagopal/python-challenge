# import os module that allows for us to use file pathing
import csv
import os

#import the csv module that will allow for us to handle .csv files
import csv

# create a path to the csv file
# use os.path.join() to create a path as well
#filePath = os.path.join("..","Resources","budget_data.csv")
inputFile = os.path.join("Resources","budget_data.csv")
outputFile = os.path.join("analysis", "pyBank_analysis.csv")
print(inputFile)

# initialising the counter
no_of_months = 0
total_profit_loss = 0

#open the file using the file path above

with open(inputFile, 'r') as file:

    # use csvReader function to open the file
    csvReader = csv.reader(file, delimiter=",")

    # to print out the contents of the stream
    print(csvReader)
    header = next(csvReader)
    #print(f"Header: {header}") # each row creates a list
    # read the remaining rows in the CSV file
    print("Financial Analysis")
    print("---------------------------")
    for row in csvReader:
        #print(row)
        # to print the names, access index 0
        no_of_months += 1

        total_profit_loss = total_profit_loss + int(row[1])
    print("Total Months: {no_of_months},"Total: ",{total_profit_loss})