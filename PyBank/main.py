import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')#import csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')#open csv file
    csv_header = next(csvreader)#skip first row
    #establish variables
    total = 0
    months = 0
    first_row = next(csvreader)  # establish variable for look behind process, set as row after header
    profit_change = 0
    previous_row = int(first_row[1])
    profit_change_record = []
    profit_increase = 0
    profit_decrease = 0
    profit_month = "Month"
    for row in csvreader:
        total += float(row[1]) #sums total of profit gain/loss
        months = months + 1 #counts number of months
        profit_change = int(row[1]) - previous_row #compares current value to previous value
        if profit_change > profit_increase: #looks for greatest increase
            profit_increase = profit_change
            profit_month_increase = str(row[0])
        elif profit_change < profit_decrease: #looks for greatest decrease
            profit_decrease = profit_change
            profit_month_decrease = str(row[0])
        profit_change_record.append(profit_change) #places profit change in an array
        previous_row = int(row[1]) #sets previous row for next iteration
    length = len(profit_change_record)
    average_change = sum(profit_change_record)/length
    average_change = round(average_change,2) #calculates average and rounds to 2 decimal places
print("Financial Analysis")
print("===================")
print(f"Total Months: {months+1}") #adds a month since the for loop started on row 2
print(f"Total: {total+int(first_row[1])}") #adds the skipped first row back to the total
print(f"Average Change:{average_change}")
print(f"Greatest increase in profits: {profit_month_increase} {profit_increase}")
print(f"Greatest decrease in profits: {profit_month_decrease} {profit_decrease}")