# Questions : How to check if a string is a palindrome or not ?

# Program : Checking if a string is a palindrome or not .

while True:
    user_input = input("Enter the string to be checked whether it is a palindrome or not : ")
    
    variable = list(user_input)
    variable.reverse()

    output = ''.join(map(str, variable))

    if user_input.lower() == output.lower():
        print(f"{user_input} is a palindrome .")

    else:
        print(f"{user_input} is not a palindrome .")