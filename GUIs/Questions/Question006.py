# Question : How to find out if a number is an armstrong number or not ?

# Program : Determining if a number is an armstrong number or not .

while True:
    var = int(input("Enter the number to be checked : "))
    copy_var = var

    sum_list = []

    result = 0

    while copy_var != 0 :
        sum_list.append(copy_var % 10)
        copy_var //= 10

    for i in sum_list:
        i **= len(var)
        result += i

    if result == var:
        print(f"{var} is an armstrong number .")

    else:
        print(f"{var} is not an armstrong number .")

    print()