# -*- coding: utf-8 -*-
"""
03-Python-HW
python-challenge/PyPoll 
"""
rowCount = 0
import csv
with open(r'\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        rowCount = rowCount + 1   
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','w')
    outFile.write("\nElection Results \n")
    outFile.write("-"*30 + "\n")
    outFile.write("Total Votes: " + str(rowCount) + " \n")  
    outFile.write("-"*30 + "\n")
    outFile.write("Candidate 1 \n")  
    outFile.write("Candidate 2 \n")  
    outFile.write("Candidate 3 \n")  
    outFile.write("Candidate 4 \n") 
    outFile.write("-"*30 + "\n")
    outFile.write("Winner: " + "winner " + "\n")
    outFile.write("-"*30 + "\n")   
    outFile.close()
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','r')
    print(outFile.read())
   
print([i+1 for i in range(100)])


import csv
candidateList = [] 
totalVotes = 0
voteCount = 0
winner = "carl"
with open(r'\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:      
        totalVotes = totalVotes + 1   
        if row[2] not in candidateList:
            candidateList.append(row[2])
    for candidate in candidateList:
        print(candidate)
        for row2 in csvreader:
            print(row2[2])
            print(candidate)
            if candidate == row2[2]:
                voteCount = voteCount + 1
                if voteCount > winnerCount:
                    winner = candidate
        print(candidate + " " + str(voteCount))
        voteCount = 0   
    print(winner)        
            
             
            
 
        if maxVoteCount > voteCount:
            winner = candidate
        print(int(row) + ": " +  str(round(voteCount/rowCount,3)) + "% (" + str(votecount))")")
        voteCount = 0
    Print(winner)
    outfile.write(candidate)
    
        
        