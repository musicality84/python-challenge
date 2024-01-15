import os
import csv
csvpath = os.path.join('Resources','election_data.csv') #import csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #open csv file
    csv_header = next(csvreader) #skip header
    #establish variables
    total = 0
    candidates = []
    candidates_unique = []
    candidate_count = []
    first_row = next(csvreader)
    first_row_candidate = str(first_row[2])
    for row in csvreader:
        total = total + 1
        if str(row[2])!=first_row_candidate:
            candidates.append(first_row_candidate)
            first_row_candidate = str(row[2])
            candidate_count.append(str(row[2]))
            for name in candidates:
                if name not in candidates_unique:
                    candidates_unique.append(name)
        else:
            candidate_count.append(str(row[2]))
    candidate_1_votes = candidate_count.count(candidates_unique[0])+1 #adds plus one since we skipped the first row
    candidate_2_votes = candidate_count.count(candidates_unique[1])
    candidate_3_votes = candidate_count.count(candidates_unique[2])
    candidate_1_percent = candidate_1_votes/(candidate_1_votes+candidate_2_votes+candidate_3_votes)*100
    candidate_1_percent = round(candidate_1_percent,3)
    candidate_2_percent = candidate_2_votes / (candidate_1_votes + candidate_2_votes + candidate_3_votes) * 100
    candidate_2_percent = round(candidate_2_percent, 3)
    candidate_3_percent = candidate_3_votes / (candidate_1_votes + candidate_2_votes + candidate_3_votes) * 100
    candidate_3_percent = round(candidate_3_percent, 3)
print("Election Results")
print("-----------------")
print(f"Total Votes: {total+1}")#adds the skipped row 1 back to the count
print("-----------------")
print(f"{candidates_unique[0]}: {candidate_1_percent}% ({candidate_1_votes})")
print(f"{candidates_unique[1]}: {candidate_2_percent}% ({candidate_2_votes})")
print(f"{candidates_unique[2]}: {candidate_3_percent}% ({candidate_3_votes})")
print("-----------------")
print(f"Winner: {candidates_unique[1]}")