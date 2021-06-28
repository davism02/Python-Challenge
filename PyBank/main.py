# import os library
# import csv library
import os
import csv

# set the file location as a variable
csvpath = "C:/Users/MDavi23/Documents/Git hub/Python-Challenge/Python-Challenge/PyBank/Resources/budget_data.csv"

# create the list variable
budget = []

# create csv from file path and import into list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    budget.append(csv_header)
    for row in csvreader:
        budget.append(row)
        
# set variables for finding net total and Month Count        
# count the rows starting from second row
# sum all net totals
Mth_Count = 0
Net_Total = 0
for row in budget[1:]:
    Mth_Count += 1
    Net_Total += int(row[1])
    
# make a list of only the month totals
Month_Total= [int(j) for i, j in budget[1:]]

# zip the month total list to itself, one index ahead for one of the lists
# subtract Find the difference between the zipped items
MnthChng = [x - y for x, y in zip(Month_Total[1:], Month_Total)]

# find the average of the items in the month change list
MnthChngAvg = sum(MnthChng) / len(MnthChng)

# Create a list of the month names
MnthList = [i for i, j in budget[1:]]

# zip the month names and month change list together
# account for the first month not having a recorded change
MnthChngList = [i for i in zip(MnthList[1:], MnthChng)]

for row in MnthChngList:
    if row[1] == max(MnthChng):
        MxMnth = row[0]
        MxAmnt = row[1]
    if row[1] == min(MnthChng):
        MnMnth = row[0]
        MnAmnt = row[1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(budget) - 1}")
print(f"Total: ${Net_Total}")
print(f"Average  Change: ${round(MnthChngAvg, 2)}")
print(f"Greatest Increase in Profits: {MxMnth} (${max(MnthChng)})")
print(f"Greatest Decrease in Profits: {MnMnth} (${min(MnthChng)})")

with open("FinancialAnalysis.txt", "a") as txt:
    txt.write("Financial Analysis/n")
    txt.write("----------------------------/n")
    txt.write(f"Total Months: {len(budget) - 1}/n")
    txt.write(f"Total: ${Net_Total}/n")
    txt.write(f"Average  Change: ${round(MnthChngAvg, 2)}/n")
    txt.write(f"Greatest Increase in Profits: {MxMnth} (${max(MnthChng)})/n")
    txt.write(f"Greatest Decrease in Profits: {MnMnth} (${min(MnthChng)})/n")
    txt.close()