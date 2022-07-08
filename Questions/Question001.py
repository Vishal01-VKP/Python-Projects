# Question : What is 0**0 ?

# Program : Finding out a**a , where a tends to zero ( till 15 decimal places )
 
a = 0.1

for i in range(100000000):
    print(f"{str(i+1).zfill(9)} -> {round(a**a, 100)}")
    a /= 10

# Conclusion : a**a tends towards 1
