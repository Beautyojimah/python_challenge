# imports
import os
import csv
#from pathlib import Path

# csv reader function
def load_csv(filename):
    # Open file in read mode
    file = open(filename,"r")
    # Reading file
    lines = csv.reader(file)
    next(lines)
    data = list(lines)
    return data
file_path = ("Resources/budget_data.csv")
data = load_csv(file_path)

def convert_data(data):
    date_column=[]
    profit_column=[]
    for i in range(len(data)):
        date_column.append(data[i][0])
        profit_column.append(int(data[i][1]))
    return date_column,profit_column
# reading loaded data
date_column,profit_column = convert_data(data)

change_sum = 0
greatest_positive_change = 0
greatest_negative_change = 0
index_of_positive_increase = None
index_of_negative_increase = None
for i in range(len(data) - 1):
    diff = profit_column[i + 1] - profit_column[i]
    change_sum += diff
    # total_sum=
    if diff > greatest_positive_change:
        greatest_positive_change = diff
        index_of_positive_increase = i + 1
    if diff < greatest_negative_change:
        greatest_negative_change = diff
        index_of_negative_increase = i + 1

date_of_greatest_profit = date_column[index_of_positive_increase]
date_of_negative_profit = date_column[index_of_negative_increase]
date_length = len(date_column)
average_change = round(change_sum / (date_length - 1), 2)
print(f'Total month is {len(date_column)}')
print(f'Total  is $ {sum(profit_column)}')
print(f'Average change is $ {average_change}')
print(f'Greatest positive change is $ {greatest_positive_change} which occured on {date_of_greatest_profit}')
print(f'Greatest negative change is $ {greatest_negative_change} which occured on {date_of_negative_profit}')