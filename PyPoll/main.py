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

print(candidate_votes)