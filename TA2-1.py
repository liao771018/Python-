str_1 = input()

str_list = str_1.split()
a, b = str_list

i = 0
while i < int(a):
  i += 1
  j = 0
  while j < int(b):
    j += 1
    result = i * j
    print(f'{i}x{j}={result}')
        
  