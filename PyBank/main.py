# -*- coding: utf-8 -*-
"""
03-Python-HW
python-challenge/PyBank 
"""
import csv
netTotal = 0
rowCount = 0
maxProfit = 0
minProfit = 0
with open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\Resources\03-Python_HW_Instructions_PyBank_Resources_budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if rowCount == 0:
            maxProfit = int(row[1])
            minProfit = int(row[1])
        rowCount = rowCount + 1
        netTotal = netTotal + int(row[1])
        if int(row[1]) > maxProfit:
            maxProfit = int(row[1])
            maxDate = row[0]
        if int(row[1]) < minProfit:
            minProfit = int(row[1])
            minDate = row[0] 
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','w')
    outFile.write("\nFinancial Analysis \n")
    outFile.write("------------------------------------- \n")
    outFile.write("Total Months: " + str(rowCount) + " \n")   
    outFile.write("Total: $" + str(netTotal) + " \n") 
    outFile.write("Average Change: $" + str(round(netTotal/rowCount,2)) + " \n")
    outFile.write("Greatest Increase in Profits: " + maxDate + " ($" + str(maxProfit) +") \n")
    outFile.write("Greatest Decrease in Profits: " + minDate + " ($" + str(minProfit) +") \n")
    outFile.close()
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','r')
    print(outFile.read())
 
    
    
