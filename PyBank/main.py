import csv
import os

csvpath = os.path.join("budget_data.csv")

dates = []
profits_losses = []

with open(csvpath, newline='') as handler:
	budget_data = csv.reader(handler)
	header = next(budget_data)

	for row in budget_data:
		dates.append(row[0])
		profits_losses.append(int(row[1]))

print(dates[0])
print(profits_losses[0])