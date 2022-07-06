# import csv and os modules
import csv
import os

# create a path to the input election file and output file
# use os.path.join() to create the path

inputFile = os.path.join("Resources","election_data.csv")
outputFile = os.path.join("analysis", "pyPoll_analysis.txt")

# initialising variables
totalVotes = 0
candidates = [] # the list that holds the list of candidates
candidateVotes = {} # dictionary that holds the votes each candidate received
winningCount = 0 # holds the winning count
winningCandidate = "" # variable to hold the winning candidate

with open(inputFile, 'r') as file:

    # use csvReader function to open the file
    csvReader = csv.reader(file, delimiter=",")

    # Read the header row
    header = next(csvReader)

    # read the remaining rows in the CSV file
       
    for row in csvReader:
        
        # increment the count of total votes
        totalVotes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidateVotes[row[2]] = 1
        else:
            #candidate is in the list, add vote to the candidates count
            candidateVotes[row[2]] += 1

        voteOutput = "" # Initialising Vote output

    for candidate in candidateVotes:
        # get the votes count and the % of votes
        votes = candidateVotes.get(candidate)
        votePercent = (float(votes) / float(totalVotes)) * 100
        voteOutput += f"{candidate}: {votePercent:.3f}% ({votes})\n"
        
        #compare the votes to the winning count
        if votes > winningCount:
            #update votes to be the winning Count
            winningCount = votes
            #update the winning candidate
            winningCandidate = candidate

    winningCandidateOutput = f"Winner: {winningCandidate}"
    #Output to terminal 
    output = (  
    f"\nElection Results\n"
    f"----------------------------\n" 
    f"Total Votes: {totalVotes}\n"
    f"----------------------------\n"
    f"{voteOutput}"
    f"----------------------------\n"
    f"{winningCandidateOutput}\n"
    f"----------------------------\n"
    )
    print(output)

    # open the output file in write mode
with open(outputFile, 'w') as file:
    file.write(output)
    