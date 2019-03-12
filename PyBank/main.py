import csv

csvpath = 'Resources/budget_data.csv'

dates = []
profits_losses = []

with open(csvpath, newline='') as handler:
	budget_data = csv.reader(handler)
	header = next(budget_data)

	for row in budget_data:
		dates.append(row[0])
		profits_losses.append(int(row[1]))

total_months = len(dates)
total = sum(profits_losses)

monthly_change = []

for i in range(len(profits_losses) - 1):
	monthly_change.append(profits_losses[i + 1] - profits_losses[i])

average_change = round(sum(monthly_change)/len(monthly_change), 2)

print(total_months)
print(total)
print(average_change)