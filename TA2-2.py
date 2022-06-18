# 輸入為一串數字，每個數字間以一個空白隔開，數字長度不固定，請把這些數字每個各加1後輸出

a = input()
list = a.split()

i = 0
newlist = []
while i < len(list):
  new = int(list[i]) + 1
  print(new, end=' ')
  i += 1
  
