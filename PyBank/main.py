#David Fried
#Data Science Bootcamp
#6/20/20

#Challenge 1: Analyzing Finance Records
#budget_data.csv
#The data set is composed of two columns: Date and Profit/Losses

# Python script analyzes the records to calculate each of the following:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The average of the changes in "Profit/Losses" over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in losses (date and amount) over the entire period

import csv
import os

resources = os.path.join('Resources','budget_data.csv')
analysis = os.path.join('analysis', 'analysis.txt')

#Converting rows in bank CSV file into Py lists
dates = []
profit_losses = []
with open(resources) as bank_data:
    reader = csv.reader(bank_data, delimiter=',')
    header = next(reader) #Save CSV header
    for row in reader:
        dates.append(row[0])
        profit_losses.append(row[1])

#Months included in the dataset
months = []
for date in dates:
    months.append(date[:3])

#The net total amount of "Profit/Losses" over the entire period
net = 0
amounts = []
for dollars in profit_losses:
    dollars = float(dollars)
    net += dollars
    amounts.append(dollars)

#The average of the changes in "Profit/Losses" over the entire period
average_change = 0
changes = []
for i in range(len(amounts)-1):
    change = amounts[i+1] - amounts[i]
    average_change += change
    changes.append(change)
average_change = average_change/(len(amounts)-1)

#The greatest increase in profits (date and amount) over the entire period
max_increase_value = max(changes)
max_increase_date = dates[changes.index(max(changes))+1]

#The greatest decrease in profits (date and amount) over the entire period
max_decrease_value = min(changes)
max_decrease_date = dates[changes.index(min(changes))+1]

#Finance Analysis - Terminal Output
print("\nFinancial Analysis\n------------------------------")
print("Total Months: " + str(len(months)))
print(f"Total: ${net:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {max_increase_date[:3]}-20{max_increase_date[-2:]} (${max_increase_value:,.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_date[:3]}-20{max_decrease_date[-2:]} (${max_decrease_value:,.2f})")

#Financial - Text Output ('analysis.txt')
with open(analysis, 'w') as analysis:
    analysis.write("Financial Analysis\n------------------------------")
    analysis.write("\nTotal Months: " + str(len(months)))
    analysis.write(f"\nTotal: ${net:,.2f}")
    analysis.write(f"\nAverage Change: ${average_change:,.2f}")
    analysis.write(f"\nGreatest Increase in Profits: {max_increase_date[:3]}-20{max_increase_date[-2:]} (${max_increase_value:,.2f})")
    analysis.write(f"\nGreatest Decrease in Profits: {max_decrease_date[:3]}-20{max_decrease_date[-2:]} (${max_decrease_value:,.2f})")