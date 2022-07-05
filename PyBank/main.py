# import csv and os modules
import csv
import os

# create a path to the input csv file and output file
# use os.path.join() to create the path as well

inputFile = os.path.join("Resources","budget_data.csv")
outputFile = os.path.join("analysis", "pyBank_analysis.txt")

# initialising the variables
no_of_months = 0
total_profit_loss = 0
netChange = 0
monthlyChanges =[] # Initialising the list of Monthly changes
months = [] #Initialise the list of months

with open(inputFile, 'r') as file:

    # use csvReader function to open the file
    csvReader = csv.reader(file, delimiter=",")

    #Read the header row
    header = next(csvReader)
    
    # read the remaining rows in the CSV file
       
    for row in csvReader:
        
        # increment the count of total months
        no_of_months += 1

        # accumulating profit/loss in index 1
        total_profit_loss = total_profit_loss + int(row[1])

        if no_of_months == 1: # make the previous month profit loss as current month profit loss
            previous_ProfitLoss = int(row[1])

        # Calculate the net change
        netChange = int(row[1]) - previous_ProfitLoss

        # add net change to the Monthly changes list
        monthlyChanges.append(netChange)

        # add first month that a change happened
        months.append(row[0])

        # setting previous profit loss with the current row's profit loss
        previous_ProfitLoss = int(row[1])

    averageMonthlyChanges = sum(monthlyChanges) / (len(monthlyChanges) - 1)
    greatestIncrease = [months[0], monthlyChanges[0]] # to hold the month and the value of the greatest increase
    greatestDecrease = [months[0], monthlyChanges[0]] # to hold the month and the value of the greatest decrease

    #use loop to calculate the index of the greatest and the least monthly changes
    for m in range(len(monthlyChanges)):
        #calculate the greatest increase and decrease
        if monthlyChanges[m] > greatestIncrease[1]:
            greatestIncrease[1] = monthlyChanges[m]
            greatestIncrease[0] = months[m]
        if monthlyChanges[m] < greatestDecrease[1]:
            greatestDecrease[1] = monthlyChanges[m]
            greatestDecrease[0] = months[m]

    #Output to terminal   
    print(f"\nFinancial Analysis\n")
    print(f"---------------------------\n") 
    print(f"Total Months: {no_of_months}\n")
    print(f"Total: ${total_profit_loss}\n")
    print(f"Average Change: ${averageMonthlyChanges:.2f}\n")
    print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")

    # open the file path using write mode
with open(outputFile, 'w') as file:
    
    # use writeRow function to write data to the file
    file.write(f"Financial Analysis\n\n")
    file.write(f"---------------------------\n\n")
    file.write(f"Total Months: {no_of_months}\n\n")
    file.write(f"Total: ${total_profit_loss}\n\n")
    file.write(f"Average Change: ${averageMonthlyChanges:.2f}\n\n")
    file.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n\n")
    file.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n\n")