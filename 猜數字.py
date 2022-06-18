# 小時候一定玩過一個遊戲，從1~100內猜一個數字，如果沒猜到，下一個猜的人會從你所猜的數字得到新的範圍，從新的範圍開始猜

import random

i = random.randint(1, 100)

min = 1
max = 100

while True:
  guess = int(input(f'請猜一個{min}-{max}的數字'))
  if guess == i:
    print('correct')
    break

  else:
    if guess < i:
      min = guess
    else:
      max = guess
      