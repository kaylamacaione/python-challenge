import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])

    #define variaables
    Date = []
    Revenue = []
    MonthlyChanges = []
    Months = 0
    TotalProfit = 0
    StartingProfit = 0

# Calculate total number of months included in the dataset  
# Calculate net total amount of "Profit/Losses" over the entire period
# Find average of changes
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(int(row[1]))
        Months = Months + 1

        FinalProfit = int(row[1])
        MonthlyProfit = FinalProfit - StartingProfit
        MonthlyChanges.append(MonthlyProfit)

        TotalProfit = TotalProfit + MonthlyProfit
        StartingProfit = FinalProfit

    TotalRev = 0

    Count = Months - 1
    AverageChange = round((TotalProfit) / (Count))


# Determine greatest increase in profits (date and amount) over entire period
    GreatestIncrease = max(MonthlyChanges)
    GreatestIncreaseMonth = Date[MonthlyChanges.index(GreatestIncrease)]

# Determine greatest decrease in profits (date and amount) over entire period
    GreatestDecrease = min(MonthlyChanges)
    GreatestDecreaseMonth = Date[MonthlyChanges.index(GreatestDecrease)]

print("Financial Analysis:")
print("----------------------")
print(f"Total Months:" + str(Months))
print(f'Total: ${TotalProfit}')
print(f'Average Change: ${AverageChange}')
print(f'Greatest Increase in Profits: {GreatestIncreaseMonth} ${GreatestIncrease}')
print(f'Greatest Decrease in Profits: {GreatestDecreaseMonth} ${GreatestDecrease}')
print("----------------------")


#output files
output_file = os.path.join('Analysis','Financial_Analysis_Summary.txt')

file = open('Analysis/Financial_Analysist.txt','w')

file.write("Financial Analysis         \n")
file.write("\n----------------------\n")
file.write("Total Months: " + str(Months) +  "\n")
file.write("Total: $ " + str(TotalProfit) +  "\n")
file.write("Average Change: $ " + str(AverageChange) +  "\n")
file.write("Greatest Increase in Profits: " + str(GreatestIncreaseMonth) + " $ " + str(GreatestIncrease) +  "\n" )
file.write("Greatest Decrease in Profits:  " + str(GreatestDecreaseMonth) + " $ " + str(GreatestDecrease) +  "\n")
file.write("\n----------------------\n")