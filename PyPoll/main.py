# -*- coding: utf-8 -*-
"""
03-Python-HW
python-challenge/PyPoll 
"""
rowCount = 0
import csv
with open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
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
   
    
candidateList = []   
import csv
with open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        rowCount = rowCount + 1   
        if row[2] not in candidateList:
            candidateList.append(row[2])
    for candidate in set(candidateList):
        print(candidate)
        print(rowCount)
        print(candidateList.count(candidate))        
        
        
        next(csvreader)
        
        for row in csvreader:
            if rowCount == 0:
                rowCount = rowCount + 1  
            if row[2] = candidate[0]
            
            
        votes = candidateList.count(candidate)
        
        
        row in csvreader:  
        
        print(str(votes))
        print(str(round(votes/rowCount*100,3)))
        
 
        if maxVoteCount > voteCount:
            winner = candidate
        print(int(row) + ": " +  str(round(voteCount/rowCount,3)) + "% (" + str(votecount))")")
        voteCount = 0
    Print(winner)
    outfile.write(candidate)
    
        
        