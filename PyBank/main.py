import os
import csv
#path
csvpath = os.path.join("..", "Resources", "PyBank_Resources_budget_data.csv")

#define the function and have ot accept data


#open Csv File 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 #skip head     
    csv_header = next(csvreader, None)
    
  # Lists
    dates = []
    profit_losses = []
    monthly_change = []
    monthly_change = []
  # Loop for lists
    for row in csvreader:

        dates.append(row[0])
        profit_losses.append(row[1])
  # Total Months
    total_months = 0
    for months in dates:
        total_months += 1
  # Net total 
    net_total = 0
    for row in profit_losses:
        net_total += int(row)
  # Month change = i+1-i
    # for i in range((len(profit_losses)-1)):
    #   print(int(profit_losses[i+1])-int(profit_losses[i]))
    
    for i in range((len(profit_losses)-1)):
      chnge =+ (int(profit_losses[i+1])-int(profit_losses[i]))
      monthly_change.append(chnge)
    chg = round(sum(monthly_change)/len(monthly_change))
    
    # GRT INC
    profit_increase = max(monthly_change)
    print(profit_increase)
    j = monthly_change.index(profit_increase)
    month_increase = dates[j+1]
    
    # GRT DEC
    profit_decrease = min(monthly_change)
    print(profit_decrease)
    l = monthly_change.index(profit_decrease)
    month_decrease = dates[l+1]
     
    print(f"Financial Analysis")
    print(f"------------------------")
    print(F"Total Months: {total_months}")
    print(F"Total: ${net_total}")
    print(F"Average Change: ${chg}")
    print(F"Greatest Increase in Profits: {month_increase} ${profit_increase}")
    print(f"Greatest Decrease in Profits: {month_decrease} ${profit_decrease}")
