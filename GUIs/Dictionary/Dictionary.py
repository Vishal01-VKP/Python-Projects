while True:

    query = input("Do you want to add more words ? (Press no to exit): ").lower()

    if query != "no":
        word = input("Word : ")
        meaning = input("Meaning : ")

        term = [f"{word} : {meaning}"]
        
        file1 = open("Dictionary.txt", "a")
        file1.write(f"{str(term)}\n")
        file1.close()

        file2 = open("Dictionary.txt", "r")
        info = file2.read()
        print(info)
        file2.close()

    else:
        break