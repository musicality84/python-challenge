import os
import csv
csvpath = os.path.join('Resources','election_data.csv') #import csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #open csv file
    csv_header = next(csvreader) #skip header
    #establish variables in winner library
    total = 0
    candidates = []
    candidates_unique = []
    candidate_count = []
    candidate_total = 0
    candidate_percent = 0
    candidate_total_storage = {}
    winner_tally = 0
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
print("Election Results")
print("-----------------")
print(f"Total Votes: {total+1}")#adds the skipped row 1 back to the count
print("-----------------")
for name in candidates_unique:
    candidate_total = candidate_count.count(name)
    candidate_percent = (candidate_total/total)*100
    candidate_percent = round(candidate_percent,3)
    print(f"{name}: {candidate_percent}% ({candidate_total})")
    candidate_total_storage[name] = candidate_total
    candidate_total = 0
    candidate_percent = 0
print("-----------------")
for key in candidate_total_storage:
    if candidate_total_storage[key] > winner_tally:
        winner_tally = candidate_total_storage[key]
        winner_name = key
print(f"Winner: {winner_name}")
with open("results.txt", "w") as txt_file:
    print("Election Results", file = txt_file)
    print("-----------------", file = txt_file)
    print(f"Total Votes: {total + 1}", file = txt_file)  # adds the skipped row 1 back to the count
    print("-----------------", file = txt_file)
    for name in candidates_unique: #counts number of votes for each candidate based on the number of times the name appears in the candidate_count list and calculates the percentage of total votes
        candidate_total = candidate_count.count(name)
        candidate_percent = (candidate_total / total) * 100
        candidate_percent = round(candidate_percent, 3)
        print(f"{name}: {candidate_percent}% ({candidate_total})", file = txt_file)
        candidate_total_storage[name] = candidate_total #appends dictionary with total votes per candidate in for use when calculating winner
        candidate_total = 0
        candidate_percent = 0
    print("-----------------", file = txt_file)
    for key in candidate_total_storage:
        if candidate_total_storage[key] > winner_tally:
            winner_tally = candidate_total_storage[key]
            winner_name = key
    print(f"Winner: {winner_name}", file=txt_file)