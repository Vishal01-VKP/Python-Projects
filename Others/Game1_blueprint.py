import random

numbers = []
numlist = []
botlist = []
removed = []

bot_points = 0
my_points = 0

for i in range(1,26):
    numlist.append(str(i).zfill(2))
    botlist.append(str(i).zfill(2))
    numbers.append(i)

random.shuffle(numlist)
random.shuffle(botlist)

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
    global bot_points,my_points, megalist1, megalist2

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

    if len(pointlist1) == 1 : bot_points += 1
    if len(pointlist2) == 1 : bot_points += 1
    if len(pointlist3) == 1 : bot_points += 1
    if len(pointlist4) == 1 : bot_points += 1
    if len(pointlist5) == 1 : bot_points += 1
    if len(pointlista) == 1 : bot_points += 1
    if len(pointlistb) == 1 : bot_points += 1
    if len(pointlistc) == 1 : bot_points += 1
    if len(pointlistd) == 1 : bot_points += 1
    if len(pointliste) == 1 : bot_points += 1

    if len(pointlist6) == 1 : my_points += 1
    if len(pointlist7) == 1 : my_points += 1
    if len(pointlist8) == 1 : my_points += 1
    if len(pointlist9) == 1 : my_points += 1
    if len(pointlist0) == 1 : my_points += 1
    if len(pointlistf) == 1 : my_points += 1
    if len(pointlistg) == 1 : my_points += 1
    if len(pointlisth) == 1 : my_points += 1
    if len(pointlisti) == 1 : my_points += 1
    if len(pointlistj) == 1 : my_points += 1
    

while True:
    bot_choice = random.choice(numbers)

    if 0<bot_choice<=5 : req_num = megalist1[0][bot_choice-1] ; megalist1[0][bot_choice-1] = "XX"
    if 5<bot_choice<=10 : req_num = megalist1[1][bot_choice-6] ; megalist1[1][bot_choice-6] = "XX"
    if 10<bot_choice<=15 : req_num = megalist1[2][bot_choice-11] ; megalist1[2][bot_choice-11] = "XX"
    if 15<bot_choice<=20 : req_num = megalist1[3][bot_choice-16] ; megalist1[3][bot_choice-16] = "XX"
    if 20<bot_choice<=25 : req_num = megalist1[4][bot_choice-21] ; megalist1[4][bot_choice-21] = "XX"

    if req_num in megalist2[0] : megalist2[0][list6.index(req_num)] = "XX"
    if req_num in megalist2[1] : megalist2[1][list7.index(req_num)] = "XX"
    if req_num in megalist2[2] : megalist2[2][list8.index(req_num)] = "XX"
    if req_num in megalist2[3] : megalist2[3][list9.index(req_num)] = "XX"
    if req_num in megalist2[4] : megalist2[4][list0.index(req_num)] = "XX"

    numbers.remove(bot_choice)
    removed.append(bot_choice)

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

    my_input = int(input("Enter your position : "))

    if 0<my_input<=5 : req_num = megalist2[0][my_input-1] ; megalist2[0][my_input-1] =="XX"
    if 5<my_input<=10 : req_num = megalist2[1][my_input-6] ; megalist2[1][my_input-6] = "XX"
    if 10<my_input<=15 : req_num = megalist2[2][my_input-11] ; megalist2[2][my_input-11] = "XX"
    if 15<my_input<=20 : req_num = megalist2[3][my_input-16] ; megalist2[3][my_input-16] = "XX"
    if 20<my_input<=25 : req_num = megalist2[4][my_input-21] ; megalist2[4][my_input-21] = "XX"

    if req_num in megalist1[0] : megalist1[0][list1.index(req_num)] = "XX"
    if req_num in megalist1[1] : megalist1[1][list2.index(req_num)] = "XX"
    if req_num in megalist1[2] : megalist1[2][list3.index(req_num)] = "XX"
    if req_num in megalist1[3] : megalist1[3][list4.index(req_num)] = "XX"
    if req_num in megalist1[4] : megalist1[4][list5.index(req_num)] = "XX"

    numbers.remove(my_input)
    removed.append(my_input)

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
