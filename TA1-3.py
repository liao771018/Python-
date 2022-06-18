stock = input()

stocks = stock.split()

no_open = ['星期五', '星期六', '星期日']

if stocks[0] not in no_open:
  print(int(stocks[1]) * int(stocks[2]))
else:
  print('不開市')
