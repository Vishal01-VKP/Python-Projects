# Question  : How to make all possible pairs of a list ?

# Program : Creating a function which will create all possible pairs of a list ( order of element matters )

grand_list = input("Enter the elements of the list ( separated by a comma ) : ").split(",")

elements_no = len(grand_list)

final_list = []

for i in range(elements_no):
    for j in range(elements_no):
        final_list.append([grand_list[i], grand_list[j]])

for i in final_list:
    if i[0] == i[1]:
        final_list.remove(i)

# for i in range(len(final_list)):
#     try:
#         if final_list[i][0] == final_list[i+1][0] or final_list[i][0] == final_list[i+1][1] or final_list[i][1] == final_list[i+1][0] or final_list[i][1] == final_list[i+1][1] :
            
#             final_list[i+1] , final_list[i+2] = final_list[i+2] , final_list[i+1]

#     except Exception:
#         pass

print(final_list)