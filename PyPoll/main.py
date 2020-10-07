"""
03-Python-HW
python-challenge/PyPoll 

This Python script will scan rows for candidates total votes, candidates' votes and their %-of-total, and the candidate winner of the election.

Write results to report file, OutputPyPoll.txt, and when finished, print report file to terminal.

"""
# Initialize Counts
candidateList = [] 
totalVotes = 0
voteCount = 0
winnerCount = 0
# Open CSV PyPoll 
import csv
with open(r'\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip Header Record
    next(csvreader)
     # Scan rows in PyPoll csv file for distinct list of candidates and total votes
    for row in csvreader:      
        totalVotes = totalVotes + 1   
        if row[2] not in candidateList:
            candidateList.append(row[2])
    # Open report file output file, outputPyPoll.txt, to write header and total votes (this file will be printed at end)
    outFile = open(r'\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','w')
    outFile.write("\nElection Results \n")
    outFile.write("-"*23 + "\n")
    outFile.write("Total Votes: " + str(totalVotes) + " \n") 
    outFile.write("-"*23 + "\n")
    # Scan PyPoll csv file for each candidate counting votes and check for Winner
    for candidate in candidateList:
        csvfile.seek(0)
        for row in csvreader:
            if candidate == row[2]:
                voteCount = voteCount + 1
        if voteCount > winnerCount:
            winner = candidate
            winnerCount = voteCount
        # Write each candidate, their number of votes, and percentage of total votes
        outFile.write(candidate + ": " + str(round(voteCount/totalVotes*100,4)) + "% (" + str(voteCount) + ")\n")
        voteCount = 0   
    # Write winner candidate with greatest number of votes
    outFile.write("-"*23 + "\n")
    outFile.write("Winner: " + winner + "\n")
    outFile.write("-"*23 + "\n")   
    outFile.close()
    # Print report from output file, OutputPyBank.txt
    outFile = open(r'\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','r')
    print(outFile.read())
