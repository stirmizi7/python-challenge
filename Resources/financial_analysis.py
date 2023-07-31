import csv
total_months = 0
net_profit_loss = 0
prev_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

file_path = "budget_data.csv"
# Step 3: Read the data from the CSV file and perform the financial analysis
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
     # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Calculate the total number of months
        total_months += 1

        # Convert the profit/loss value to an integer
        profit_loss = int(row[1])

        # Calculate the net total amount of profit/losses
        net_profit_loss += profit_loss
# Calculate the change in profit/losses and store it in the list
        if total_months > 1:
            profit_loss_change = profit_loss - prev_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # Update the greatest increase and decrease if applicable
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

        # Update the previous profit/loss value
        prev_profit_loss = profit_loss
        # Step 4: Calculate the average change in profit/losses
average_change = sum(profit_loss_changes) / len(profit_loss_changes) if len(profit_loss_changes) > 0 else 0

# Step 5: Print the financial analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

import csv

# ... (Previous code to read and analyze the data)

# Step 5: Print the financial analysis results to the terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Step 6: Export the financial analysis results to a text file
output_file = "financial_analysis_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Net Total: ${net_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

