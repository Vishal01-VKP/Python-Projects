import random

numbers = [] ; numlist = [] ; botlist = [] ; removed = []
var01 = True ; var02 = True ; var03 = True ; var04 = True ; var05 = True ; var06 = True ; var07 = True ; var08 = True ; var09 = True ; var10 = True ; var11 = True ; var12 = True ; var13 = True ; var14 = True ; var15 = True ; var16 = True ; var17 = True ; var18 = True ; var19 = True ; var20 = True ; var21 = True ; var22 = True ; var23 = True ; var24 = True
bot_points = 0 ; my_points = 0

for i in range(1,26):
    numlist.append(str(i).zfill(2)) ; botlist.append(str(i).zfill(2)) ; numbers.append(i)

random.shuffle(numlist) ; random.shuffle(botlist)

list1 = [] ; list2 = [] ; list3 = [] ; list4 = [] ; list5 = []
list6 = [] ; list7 = [] ; list8 = [] ; list9 = [] ; list0 = []

for i in range(5):
    list1.append(numlist[i]) , list6.append(botlist[i])
    list2.append(numlist[i+5]) ,list7.append(botlist[i+5]) 
    list3.append(numlist[i+10]) ,list8.append(botlist[i+10]) 
    list4.append(numlist[i+15]) ,list9.append(botlist[i+15]) 
    list5.append(numlist[i+20]) ,list0.append(botlist[i+20])

megalist1 = [list1 , list2 , list3 , list4 , list5]
megalist2 = [list6 , list7 , list8 , list9 , list0]

def points():
    global bot_points,my_points, megalist1, megalist2 , var01, var02, var03, var04, var05, var06, var07, var08, var09, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, var20, var21, var22, var23, var24

    pointlist1 = set(megalist1[0])
    pointlist2 = set(megalist1[1])
    pointlist3 = set(megalist1[2])
    pointlist4 = set(megalist1[3])
    pointlist5 = set(megalist1[4])

    pointlista = {megalist1[0][0],megalist1[1][0],megalist1[2][0],megalist1[3][0],megalist1[4][0]}
    pointlistb = {megalist1[0][1],megalist1[1][1],megalist1[2][1],megalist1[3][1],megalist1[4][1]}
    pointlistc = {megalist1[0][2],megalist1[1][2],megalist1[2][2],megalist1[3][2],megalist1[4][2]}
    pointlistd = {megalist1[0][3],megalist1[1][3],megalist1[2][3],megalist1[3][3],megalist1[4][3]}
    pointliste = {megalist1[0][4],megalist1[1][4],megalist1[2][4],megalist1[3][4],megalist1[4][4]}

    pointlista1 = {megalist1[0][0],megalist1[1][1],megalist1[2][2],megalist1[3][3],megalist1[4][4]}
    pointliste5 = {megalist1[4][0],megalist1[3][1],megalist1[2][2],megalist1[1][3],megalist1[0][4]}

    pointlist6 = set(megalist2[0])
    pointlist7 = set(megalist2[1])
    pointlist8 = set(megalist2[2])
    pointlist9 = set(megalist2[3])
    pointlist0 = set(megalist2[4])

    pointlistf = {megalist2[0][0],megalist2[1][0],megalist2[2][0],megalist2[3][0],megalist2[4][0]}
    pointlistg = {megalist2[0][1],megalist2[1][1],megalist2[2][1],megalist2[3][1],megalist2[4][1]}
    pointlisth = {megalist2[0][2],megalist2[1][2],megalist2[2][2],megalist2[3][2],megalist2[4][2]}
    pointlisti = {megalist2[0][3],megalist2[1][3],megalist2[2][3],megalist2[3][3],megalist2[4][3]}
    pointlistj = {megalist2[0][4],megalist2[1][4],megalist2[2][4],megalist2[3][4],megalist2[4][4]}

    pointlistf6 = {megalist2[0][0],megalist2[1][1],megalist2[2][2],megalist2[3][3],megalist2[4][4]}
    pointlistj0 = {megalist2[4][0],megalist2[3][1],megalist2[2][2],megalist2[1][3],megalist2[0][4]}

    if len(pointlist1) == 1 and var01 == True : my_points += 1 ; var01 = False
    if len(pointlist2) == 1 and var02 == True : my_points += 1 ; var02 = False
    if len(pointlist3) == 1 and var03 == True : my_points += 1 ; var03 = False
    if len(pointlist4) == 1 and var04 == True : my_points += 1 ; var04 = False
    if len(pointlist5) == 1 and var05 == True : my_points += 1 ; var05 = False
    if len(pointlista) == 1 and var06 == True : my_points += 1 ; var06 = False
    if len(pointlistb) == 1 and var07 == True : my_points += 1 ; var07 = False
    if len(pointlistc) == 1 and var08 == True : my_points += 1 ; var08 = False
    if len(pointlistd) == 1 and var09 == True : my_points += 1 ; var09 = False
    if len(pointliste) == 1 and var10 == True : my_points += 1 ; var10 = False
    if len(pointlista1) == 1 and var11 == True : my_points += 1 ; var11 = False
    if len(pointliste5) == 1 and var12 == True : my_points += 1 ; var12 = False

    if len(pointlist6) == 1 and var13 == True : bot_points += 1 ; var13 = False
    if len(pointlist7) == 1 and var14 == True : bot_points += 1 ; var14 = False
    if len(pointlist8) == 1 and var15 == True : bot_points += 1 ; var15 = False
    if len(pointlist9) == 1 and var16 == True : bot_points += 1 ; var16 = False
    if len(pointlist0) == 1 and var17 == True : bot_points += 1 ; var17 = False
    if len(pointlistf) == 1 and var18 == True : bot_points += 1 ; var18 = False
    if len(pointlistg) == 1 and var19 == True : bot_points += 1 ; var19 = False
    if len(pointlisth) == 1 and var20 == True : bot_points += 1 ; var20 = False
    if len(pointlisti) == 1 and var21 == True : bot_points += 1 ; var21 = False
    if len(pointlistj) == 1 and var22 == True : bot_points += 1 ; var22 = False
    if len(pointlistf6) == 1 and var23 == True : bot_points += 1 ; var23 = False
    if len(pointlistj0) == 1 and var24 == True : bot_points += 1 ; var24 = False
    

while True:
    choice1 = random.choice(numbers)
    bot_choice = str(choice1).zfill(2)

    if bot_choice in botlist :
        position = botlist.index(bot_choice)
        megalist2[(position//5)][(position%5)] = "XX"

    if bot_choice in numlist:
        position = numlist.index(bot_choice)
        megalist1[(position//5)][(position%5)] = "XX"

    numbers.remove(choice1)
    removed.append(choice1)

    print(removed)

    for i in megalist2:
        print(i)

    points()

    if bot_points >= 5:
        print("BINGO !\nComputer Won")
        break
    if my_points >= 5:
        print("BINGO ! \nYou Won")
        break
    
    choice2 = int(input("Enter your number : "))
    my_input = str(choice2).zfill(2)

    if my_input in numlist:
        position = numlist.index(my_input)
        megalist1[(position//5)][(position%5)] = "XX"

    if my_input in botlist :
        position = botlist.index(my_input)
        megalist2[(position//5)][(position%5)] = "XX"

    numbers.remove(choice2)
    removed.append(choice2)

    print(removed)

    for i in megalist2:
        print(i)

    points()

    if bot_points >= 5:
        print("BINGO !\nComputer Won")
        break
    if my_points >= 5:
        print("BINGO ! \nYou Won")
        break
