# -*- coding: utf-8 -*-
"""
03-Python-HW
python-challenge/PyPoll 
"""
import csv
rowCount = 0
with open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\Resources\03-Python_HW_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if rowCount == 0:
            rowCount = rowCount + 1   
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','w')
    outFile.write("\nElection Results \n")
    outFile.write("---------------------------- \n")
    outFile.write("Total Votes: " + str(rowCount) + " \n")  
    outFile.write("---------------------------- \n")
    outFile.write("Candidate 1 \n")  
    outFile.write("Candidate 2 \n")  
    outFile.write("Candidate 3 \n")  
    outFile.write("Candidate 4 \n") 
    outFile.write("---------------------------- \n")
    outFile.write("Winner: " + "winner " + "\n")
    outFile.write("---------------------------- \n")    
    outFile.close()
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyPoll\analysis\OutputPyPoll.txt','r')
    print(outFile.read())
   