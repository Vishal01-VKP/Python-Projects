def C(x,y):
    difference = x-y

    def factorial(num):
        for i in range(1,num):
            num = num * i
        return num
    
    var1 = factorial(x)
    var2 = factorial(y)
    var3 = factorial(difference)

    result = int(var1 / (var2 * var3))

    return result
