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
        total += float(row[1])
        months = months + 1
        profit_change = int(row[1]) - previous_row
        if profit_change > profit_increase:
            profit_increase = profit_change
            profit_month_increase = str(row[0])
        elif profit_change < profit_decrease:
            profit_decrease = profit_change
            profit_month_decrease = str(row[0])
        profit_change_record.append(profit_change)
        previous_row = int(row[1])
    length = len(profit_change_record)
    average_change = sum(profit_change_record)/length
    average_change = round(average_change,2)
print("Financial Analysis")
print("===================")
print(f"Total Months: {months}")
print(f"Total: {total}")
print(f"Average Change:{average_change}")
print(f"Greatest increase in profits: {profit_month_increase} {profit_increase}")
print(f"Greatest decrease in profits: {profit_month_decrease} {profit_decrease}")