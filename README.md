### This Repository is for 03-Python Homework

#### Fully automated report generation:
- Posted below, at bottom, is a Python script.
- Execute one time and it will pass thru stored monthly profit records generating a well-formatted, summarized report within the PyBank "analysis" folder called "OutputPyBank.txt"
- This script will scan rows for a: count of months, total profit/loss, average, greatest increase/decrease profit/loss change from previous month.


#### Text File input within repository: 
python-challenge\PyBank\Resources\03-Python_HW_Instructions_PyBank_Resources_budget_data

#### Text File output within repository: 
python-challenge\PyBank\analysis\OutputPyBank.txt

"""
03-Python-HW
python-challenge/PyBank 

s script will scan rows for a: count of months, total profit/loss, average, greatest increase/decrease profit/loss from profit/loss from previous month.

"""
# Initialize Counts
netTotal = 0
sumChange = 0
rowCount = 0
prevProfit = 0
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
        # Sum total
        netTotal = netTotal + int(row[1])
        # Ignore first record's change in profit (no previous month)
        if rowCount != 0:
            sumChange = sumChange + (int(row[1]) - prevProfit)
            print(sumChange)
        # Count number of months
        rowCount = rowCount + 1
        # Check to see if this month is Max/Min hange in profit  
        if int(row[1]) - prevProfit > maxProfit:
            maxProfit = int(row[1]) - prevProfit
            maxDate = row[0]
        if int(row[1]) - prevProfit < minProfit:
            minProfit = int(row[1]) - prevProfit
            minDate = row[0] 
        prevProfit = int(row[1])
    # Write report to OutputPyBank.txt, text file
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','w')
    outFile.write("\nFinancial Analysis \n")
    outFile.write("-"*50 + "\n")
    outFile.write("Total Months: " + str(rowCount) + " \n")   
    outFile.write("Total: $" + str(netTotal) + " \n") 
    outFile.write("Average Change: $" + str(round(sumChange/(rowCount-1),2)) + " \n")
    outFile.write("Greatest Increase in Profits: " + maxDate + " ($" + str(maxProfit) +") \n")
    outFile.write("Greatest Decrease in Profits: " + minDate + " ($" + str(minProfit) +") \n")
    outFile.close()
    outFile = open(r'C:\Users\coffm\CarlNU\python-challenge\PyBank\analysis\OutputPyBank.txt','r')
    # Print report from output file, OutputPyBank.txt
    print(outFile.read())
    
