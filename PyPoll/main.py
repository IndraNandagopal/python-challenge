# import csv and os modules
import csv
import os

# create a path to the input csv file and output file
# use os.path.join() to create a path as well

inputFile = os.path.join("Resources","election_data.csv")
outputFile = os.path.join("analysis", "pyPoll_analysis.txt")
print(inputFile)
# initialising variables
totalVotes = 0
candidates = [] # the list that holds the list of candidates
candidateVotes = {} # dictionary that holds the votes each candidate received
winningCount = 0 # holds the winning count
winningCandidate = "" # variable to hold the winning candidate

#total_profit_loss = 0
#netChange = 0
#monthlyChanges =[] # Initialising the list of Monthly changes
#months = [] #Initialise the list of months

with open(inputFile, 'r') as file:

    # use csvReader function to open the file
    csvReader = csv.reader(file, delimiter=",")

    # to print out the contents of the stream
    print(csvReader)
    header = next(csvReader)
    #print(f"Header: {header}") # each row creates a list
    # read the remaining rows in the CSV file
   
    # setting previous profit loss to 0
    #previous_ProfitLoss = 0
    
    for row in csvReader:
        
        # to print the names, access index 0
        totalVotes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidateVotes[row[2]] = 1
        else:
            #candidate is in the list, add vote to the candidates count
            candidateVotes[row[2]] += 1

        voteOutput = ""

    for candidate in candidateVotes:
        # get the votes count and the % of votes
        votes = candidateVotes.get(candidate)
        #print(votes)
        votePercent = (float(votes) / float(totalVotes)) * 100
        voteOutput += f"{candidate}: {votePercent:.3f}% ({votes})\n"
        
        #compare the votes to the winning count
        if votes > winningCount:
            #update votes to be the winning Count
            winningCount = votes
            #update the winning candidate
            winningCandidate = candidate

    winningCandidateOutput = f"Winner: {winningCandidate}\n"
    #Output to terminal 
    output = (  
    f"\nElection Results\n"
    f"-------------------------\n" 
    f"Total Votes: {totalVotes}\n"
    f"-------------------------\n"
    f"{voteOutput}\n"
    f"-------------------------\n"
    f"{winningCandidateOutput}"
    f"-------------------------\n"
    )
    print(output)

    # open the file path using write mode
with open(outputFile, 'w') as file:
    file.write(output)
    