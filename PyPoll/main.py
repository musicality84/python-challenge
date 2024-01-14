import os
import csv
csvpath = os.path.join('Resources','election_data.csv') #import csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #open csv file
    csv_header = next(csvreader) #skip header
    #establish variables
    total = 0
    for row in csvreader:
        total = total + 1
print("Election Results")
print("-----------------")
print(f"Total: {total}")
print("-----------------")
