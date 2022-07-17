while True:
    numbers = int(input("How many binary numbers you want to add ? : "))
    bin_list = []
    result = 0

    for i in range(numbers):
        input_i = input("Enter the binary number : ")
        bin_list.append(f"0b{input_i}")
        
    for i in bin_list:
        i = int(i, base=0)
        result += i

    print(bin(result).split('b')[1])