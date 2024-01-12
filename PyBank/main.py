import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    months = 0
    for row in csvreader:
        total += float(row[1])
        months = months + 1
        #for next part, watch first 10 minutes of thursday's zoom session
print("Financial Analysis")
print("===================")
print(f"Total Months: {months}")
print(f"Total: {total}")

