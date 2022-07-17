# Question : How to determine if a number is a Krishnamurthy number or not ?

# Program : Writing a program to check if a number is a Krishnamurthy number or not .

import math

while True:
    user_input = int(input("Enter the number you want to check : "))
    sum = 0
    copy = user_input
        
    for x in range(len(str(user_input))):
        i = copy % 10

        y = math.factorial(i)
        sum += y

        copy //= 10

    if sum == user_input:
        print(f"{sum} ; {user_input} -> True")

    else:
        print(f"{sum} ; {user_input} -> False")