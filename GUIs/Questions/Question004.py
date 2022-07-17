# Question : How to print a table with user inputs , with limited input commands ?

# Program : Creating a customized table creator , with less number of input commands and lesser lines of code

import tabulate

data = []

input1 = input("Enter the name of the you want to save it in : ")
input2 = input("Enter a suitable heading for the table : ")
input3 = int(input("Number of rows you want on your table : "))

for i in range(input3):
    row_data = input("Enter data for current row ( separate each value with a comma ) : ").split(",")

    data.append(row_data)

with open(input1, "a") as file:
    file.write(f"{input2} \n{tabulate.tabulate(data, tablefmt='grid')} \n\n{'='*50} \n\n")