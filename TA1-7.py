# 今天要設計一款自動把一個算式算出來的簡易計算機

# 說明:
# 輸入為一組只有一個運算符號(+、-、*、/)的算式，請輸出算式的答案
# 注意! 輸入不會有任何的空白

# 注意!
# 在做整數除法的時候，請直接無條件捨去至整數，不需要保留小數點
# ex: 5 / 5 = 1.0
# 請輸出1

a = input()
# a = '100+200'

caus = ['+', '-', '*', '/']
if caus[0] in a:
  num = a.split(caus[0])
  # print(num)
  result = int(num[0]) + int(num[1])
elif caus[1] in a:
  num = a.split(caus[1])
  result = int(num[0]) - int(num[1])
elif caus[2] in a:
  num = a.split(caus[2])
  result = int(num[0]) * int(num[1])
elif caus[3] in a:
  num = a.split(caus[3])
  result = int(num[0]) / int(num[1])
  result = int(result)
else:
  print('輸入錯誤')
print(result)