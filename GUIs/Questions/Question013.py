import string

print("Check if two words are anagrams of each other . \n\nNote : This function won't work properly if two numbers have same sets of letters in different magnitudes but have the same length . \n\n")

while True:
    input1 = input("Enter 1st word : ")
    input2 = input("Enter 2nd word : ")

    var1 = len(input1)
    var2 = len(input2)

    set1 = set(input1)
    set2 = set(input2)

    if set1 == set2 and var1 == var2:
        print(f"{input1} and {input2} are anagrams .")

    else:
        print(f"{input1} and {input2} are not anagrams .")