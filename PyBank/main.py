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

max_increase_index = 0
max_decrease_index = 0

for i in range(1, len(monthly_change)):
	if monthly_change[i] > monthly_change[max_increase_index]:
		max_increase_index = i

	if monthly_change[i] < monthly_change[max_decrease_index]:
		max_decrease_index = i

max_increase_amount = monthly_change[max_increase_index]
max_decrease_amount = monthly_change[max_decrease_index]

max_increase_month = dates[max_increase_index + 1]
max_decrease_month = dates[max_decrease_index + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months {total_months}")
print(f"Total: ${total}")
print(f"Average Change ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount})")
print(f"Greatest Increase in Profits: {max_decrease_month} (${max_decrease_amount})")