import random

# 三個門後方有一到門是"車"，兩道門是"羊"，選擇的門打開後是"車"，就可以贏得一台車

win = 0
lose = 0

for i in range(10000):

    #隨機產出三個門
    doors = ['羊', '羊']
    num = random.randint(0, 2)
    doors.insert(num, '車')
    print('門後是:', doors)

    #參賽者隨機的選擇
    personal_num = random.randint(0, 2)
    personal_door = doors.pop(personal_num)
    print('參賽者選到的是:', personal_door)

    #主持人開出一道是羊的門
    doors.remove('羊')
    print('剩下的門:', doors)


    #參賽者選擇換另一道門贏到車的機率
    if doors[0] == '車':
        print('恭喜你,贏到一台車')
        win += 1

    else:
        print('抱歉,是一隻羊')
        lose += 1


count = win + lose
print('贏的機率是 ', win / count * 100, '%')
print('輸的機率是 ', lose / count * 100, '%')
