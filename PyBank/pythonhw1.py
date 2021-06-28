import os
import csv
csvpath = "C:/Users/MDavi23/Documents/Git hub/Python-Challenge/Python-Challenge/PyBank/Resources/budgetdata.csv"

#create list variables
budget =[]

# create csv from file path and import into list
with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    budget.append(csv_header)
    for row in csvreader:
        budget.append(row)
#set variables for finind net total and Month count
#count rows starting from the second row
#sum all net totals

Mth_Count = 0
Net_Total =0
for row in budget[1:]:
    Mth_Count +=1
    Net_Total += int(row[1:])
# make list of month totals
Mth_Total = [int(j) for i,j in budget[1:]]
print(Mth_Total)