# Function - 1 [Status : Working Fine]

# def file_edit(file_name, line_no, data, isread):
#     with open(file_name,"r") as f:
#         list=[]
#         for word in f.readlines():
#             list.append(word)
        
#         list.remove(list[line_no-1])
#         list.insert(line_no-1, f"{data}\n")

#     with open(file_name,"w") as f:
#         for line in list:
#             f.writelines(line)

#     if isread == "yes":
#         with open(file_name, "r") as file:
#             var4 = file.read()
#             print(var4)

#     else:
#         pass

# while True:
#     option = input("Do you want to read the file after modification (Write Yes to read) ? : ").lower()
#     file = input("Enter the name of the file you want to edit : ")
#     number = int(input("Which line do you want to edit ? : "))
#     info = input("Enter the data you want to modify in that particular line : ")

#     file_edit(file,number,info,option)

from rich.console import Console
import PT
from rich.table import Table

collection1 = Console()

data = PT.the_element_list

table1 = Table(title="Elements")

column_heads = ["Name","Atomic Number","Type","Group","Period","Block","Atomic Mass","State","Density","Electronegativity"]
for i in column_heads:
    table1.add_column(i)

for i in data:
    table1.add_row(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8]),str(i[9]))

collection1.print(table1)




