import csv

# Step 1: Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Step 2: Read and analyze the data from the CSV file
with open("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # Update the votes for each candidate
        if candidate_name in candidates:
             candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Step 3: Calculate the percentage of votes for each candidate
for candidate_name, votes in candidates.items():
    candidates[candidate_name] = round((votes / total_votes) * 100, 2)

# Step 4: Determine the winner based on the popular vote
winner = max(candidates, key=candidates.get)
# Step 5: Print the analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate_name, votes in candidates.items():
    print(f"{candidate_name}: {votes}% ({candidates[candidate_name]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Step 6: Export the analysis results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate_name, votes in candidates.items():
        txtfile.write(f"{candidate_name}: {votes}% ({candidates[candidate_name]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
    
