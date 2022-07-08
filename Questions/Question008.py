# Question : How to convert decimal number into any other number system type ?

# Program : Creating a program for : Decimal -> Any other number system

letters = ['F','E','D','C','B','A']

message1 = " Enter the number to be converted : "
message2 = " Enter the type of conversion ( in numbers ) \n 2 : Binary , 8 : Octal , 16 : Hexadecimal : "


def dec_to_any(number , conversion_type) :

    while True:
        if number < conversion :
            if number > 9 :
                result.append(letters[15 - number])
            else:
                result.append(number)
            break

        remainder = number % conversion

        if remainder > 9 :
            result.append(letters[15 - remainder])
        else:
            result.append(remainder)

        number //= conversion

    for i in result : i = str(i)

    result.reverse()
    answer = ''.join(map(str , result))

    print(f" ( {number} , 10 ) -> ( {answer} , {conversion} ) .")


while True:
    user_input = int(input(f"{message1}"))
    conversion = int(input(f"{message2}"))
    result = []

    dec_to_any(user_input, conversion)