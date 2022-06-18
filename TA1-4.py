lottery = input()

s = lottery.split(',')

gamer = s[0].split()

lucky = s[1].split()

bingo = 0

for i in gamer:
  if i in lucky:
    bingo += 1

if bingo == 3:
  print(100)
elif bingo == 4:
  print(1000)
elif bingo ==5 :
  print(10000)
else:
  print(0)