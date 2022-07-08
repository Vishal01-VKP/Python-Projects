import os

location = os.getcwd()
data = os.listdir(location)
number = 0

print(data)

for i in data:
    if ".py" in i:
        os.rename(i,f"Question{str(number-1).zfill(3)}.py")
    number += 1

print(data)

