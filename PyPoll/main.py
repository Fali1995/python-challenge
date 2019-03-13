import csv

csv_path = "Resources/election_data.csv"

candidate_votes = {}

with open(csv_path, newline = "") as handler:
	csv_reader = csv.reader(handler, delimiter = ',')

	header = next(csv_reader)

	for row in csv_reader:
		if row[2] in candidate_votes.keys():
			candidate_votes[row[2]] += 1
		else:
			candidate_votes[row[2]] = 1

total_votes = sum(candidate_votes.values())
highest_votes =  0

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidate_votes.keys():
	print(f"{candidate}: {round(100 * candidate_votes[candidate]/total_votes, 3)}% ({candidate_votes[candidate]})")

	if highest_votes < candidate_votes[candidate]:
		highest_votes = candidate_votes[candidate]
		winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = "Output/results.txt"

with open(output_path, 'w') as handler:
	handler.write("Election Results \n")
	handler.write("------------------------- \n")
	handler.write(f"Total Votes: {total_votes} \n")
	handler.write("------------------------- \n")

	for candidate in candidate_votes.keys():
		handler.write(f"{candidate}: {round(100 * candidate_votes[candidate]/total_votes, 3)}% ({candidate_votes[candidate]}) \n")

	handler.write("------------------------- \n")
	handler.write(f"Winner: {winner} \n")
	handler.write("------------------------- \n")

