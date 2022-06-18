# 起始條件，第一個數字為0，第二個數字為1，後面的數字為前面兩個數字的相加
# 0 1 1 2 3 5 8 13 21 …

# 說明:
# 輸入唯一個數字i，請試試看印出指定數字的(以人類的索引直)第i個數字是多少
s = int(input())

fei = [0, 1]

i = 2
while i < 18:

    next = fei[i - 2] + fei[i - 1]
    fei.append(next)
    i += 1

print(fei[s - 1])
