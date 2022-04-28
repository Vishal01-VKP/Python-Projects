from rich.table import Table
from rich.console import Console

def file_edit():
    while True:
        question = input("Do you want to exit the program ? (Press yes to exit): ")
        if question.lower() == "yes":
            break

        isread = input("Do you want to read the file after modification (Write Yes to read) ? : ").lower()
        file_name = input("Enter the name of the file you want to edit : ")
        line_no = int(input("Which line do you want to edit ? : "))
        data = input("Enter the data you want to modify in that particular line : ")

        with open(file_name,"r") as f:
            list=[]
            for word in f.readlines():
                list.append(word)
            
            list.remove(list[line_no-1])
            list.insert(line_no-1, f"{data}\n")

        with open(file_name,"w") as f:
            for line in list:
                f.writelines(line)

        if isread == "yes":
            with open(file_name, "r") as file:
                var4 = file.read()
                console1 = Console()
                table1 = Table()
                table1.add_column(file_name)
                table1.add_row(var4)
                console1.print(table1)

        else:
            print("Done ! You can now check your file to observe the changes .")
            