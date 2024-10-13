# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank\\Resources\\budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank\\analysis\\budget_analysis.txt") 
 # Output file path
if not os.path.exists("analysis"):
    os.makedirs("analysis")

# Define variables to track the financial data
total_months = 0
total_net = 0
changes = []
dates = []
previous_profit_loss = None
greatest_increase = ["",0]
greatest_decrease = ["",0]
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load, mode="r") as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list

    # Process each row of data
    for row in reader:
        print(f"Processing row: {row}")

        date = row [0]
        profit_loss = int(row[1])
        
        # Track the total
        total_months += 1
        print(f"Total Months updated to: {total_months}")
        total_net += profit_loss

        # Track the net change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase= [date, change]

        # Calculate the greatest decrease in losses (month and amount)

            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_profit_loss = profit_loss

# Calculate the average net change across the months
if len(changes) > 0:
    average_change = sum(changes)/ len(changes)
else: 
    average_change = 0

# Generate the output summary

output = (
f"Financial Analysis\n"
f"---------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits:{greatest_increase[0]}(${greatest_increase[1]})\n"
f"Greatest Decrease in Profits:{greatest_decrease[0]}(${greatest_decrease[1]})\n"
)

# Print the output

print(output)



# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
