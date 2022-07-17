import matplotlib
import matplotlib.pyplot as plt

user_input = 2

lengths = []

while user_input<320:
    # user_input = int(input("Enter the number to observe it's collatz pattern : "))
    variable = user_input
    list = []

    while variable != 1:
        if variable % 2 == 1:
            variable = (variable * 3) + 1
        elif variable % 2 == 0:
            variable /= 2

        list.append(int(variable))
    lengths.append(len(list))

    print(f"{user_input} -> {list}\n")

    user_input += 1

print(f"{lengths} \n")

x_axis = [i for i in range(2,user_input)]

plt.plot(x_axis,lengths)
plt.show()