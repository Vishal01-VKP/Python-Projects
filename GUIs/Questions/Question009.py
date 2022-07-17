# Question : How to convert a number of any system into a decimal number ?

# Program : Converting a number of any system into a decimal number . 

letters = ['F','E','D','C','B','A']

message1 = " Enter the number to be converted : "
message2 = " Enter the type of number system used ( in numbers ) \n 2 : Binary , 8 : Octal , 16 : Hexadecimal : "


def any_to_dec(number , conversion_type) :
    sum = 0
    result = []

    for i in number:
        result.append(i)

    for i in range(len(result)):
        if result[i] in letters:
            result[i] = 15-letters.index(result[i])

        i = int(i)

        result.reverse()

    for i in range(len(result)):
        i = int(result[i]) * (conversion ** i)
        sum += i
        
    print(f" ( {number} , {conversion} ) -> ( {sum} , 10 ) .")


while True:
    user_input = input(f"{message1}")
    conversion = int(input(f"{message2}"))

    any_to_dec(user_input, conversion)