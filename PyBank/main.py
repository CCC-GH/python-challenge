# -*- coding: utf-8 -*-
"""
03-Python-HW
python-challenge/PyBank 

This script will scan rows for a count of months, total profit, average, greatest increase/decrease in pofits (not difference from previous) 

"""
# Initialize Counts
netTotal = 0
rowCount = 0
maxProfit = 0
minProfit = 0
# Open CSV PyBank file
import csv
with open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\Resources\03-Python_HW_Instructions_PyBank_Resources_budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip Header Record
    next(csvreader)
    # Scan rows in PyBank file
    for row in csvreader:
    # Set Max and Min with first 
        if rowCount == 0:
            maxProfit = int(row[1])
            minProfit = int(row[1])
        # Count number of months
        rowCount = rowCount + 1
        # Sum total
        netTotal = netTotal + int(row[1])
        # Check to see if this month is Max/Min Profit
        if int(row[1]) > maxProfit:
            maxProfit = int(row[1])
            maxDate = row[0]
        if int(row[1]) < minProfit:
            minProfit = int(row[1])
            minDate = row[0] 
    # Write report to OutputPyBank.txt, text file
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','w')
    outFile.write("\nFinancial Analysis \n")
    outFile.write("-"*50 + "\n")
    outFile.write("Total Months: " + str(rowCount) + " \n")   
    outFile.write("Total: $" + str(netTotal) + " \n") 
    outFile.write("Average Change: $" + str(round(netTotal/rowCount,2)) + " \n")
    outFile.write("Greatest Increase in Profits: " + maxDate + " ($" + str(maxProfit) +") \n")
    outFile.write("Greatest Decrease in Profits: " + minDate + " ($" + str(minProfit) +") \n")
    outFile.close()
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','r')
    # Print report from output file, OutputPyBank.txt
    print(outFile.read())
 
    
    
