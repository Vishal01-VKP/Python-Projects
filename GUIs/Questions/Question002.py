# Question : How to convert a decimal number to an octal number ?

# Program : Converting a decimal number ( input ) to an octal number ( output ) ?

input = int(input("Enter the number to be converted to octal number : "))

answer = []

while input >= 8:
    remainder = input % 8
    input //= 8
    answer.append(remainder)

    if input < 8 :
        answer.append(input)
        result = ''.join(map(str, answer[::-1]))
        print(result)