# Question : How to name the upcoming elements in the periodic table in a smooth and hassle-free manner ?

# Program : Creating a function which will name any element ( 100 < A < 999 ) just by it's atomic number ( IUPAC approved ) .

while True:
    user_input = input("Enter the atomic number of the element ( 100 < A < 999 ) : ")

    change_list = [("0","nil"),("1","un"),("2","bi"),("3","tri"),("4","quad"),("5","pent"),("6","hex"),("7","sept"),("8","oct"),("9","enn")]

    if len(user_input) == 3 and str(user_input)[0] != "0":

        for x,y in change_list:
            user_input = user_input.replace(x,y)

        user_input = f"{user_input}ium"

        print(f"The name of the element would be '{user_input}' .\n")

    else:
        print(f"Error , can't operate on '{user_input}' .\n")