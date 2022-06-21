import random


def lottery_ch():
    # 隨機取出六個號碼
    ticket = set()

    while len(ticket) < 6:
        num = random.randint(1, 50)
        ticket.add(num)

    return ticket


# 中獎號碼
bingo = lottery_ch()
print('中獎號碼是 ', bingo)

# 特別號
while True:
    special_num = random.randint(1, 50)
    if special_num not in bingo:
        break

print('特別號是 ', special_num, '\n\n')


# 計算機率的次數
times = 100000

# 中獎次數
lucky = {'頭': 0, '二': 0, '三': 0, '四': 0, '五': 0, '六': 0, '七': 0, '普': 0}
times_big, times_2, times_3, times_4, times_5, times_6, times_7, times_local = lucky

for i in range(times):

    # 投注者的號碼
    lottery = lottery_ch()
    print('投注號碼是 ', lottery)

    # 兌獎
    total = 0
    for n in lottery:
        if n in bingo:
            total += 1
    print('對中 ', total, ' 個號碼', end=' ')

    # 列出特別號是否中獎
    special_total = 0
    if special_num in lottery:
        special_total = 1
        print('及 特別號', special_num, end=' ')

    # 列出中幾獎
    if total == 6:

        print('恭喜中 頭獎')
        lucky[times_big] += 1

    elif total == 5:

        if special_total == 1:
            print('恭喜中 二獎')
            lucky[times_2] += 1

        else:
            print('恭喜中 三獎')
            lucky[times_3] += 1

    elif total == 4:

        if special_total == 1:
            print('恭喜中 四獎')
            lucky[times_4] += 1

        else:
            print('恭喜中 五獎')
            lucky[times_5] += 1

    elif total == 3:

        if special_total == 1:
            print('恭喜中 六獎')
            lucky[times_6] += 1

        else:
            print('恭喜中 普獎')
            lucky[times_local] += 1

    elif total == 2:

        if special_total == 1:
            print('恭喜中 七獎')
            lucky[times_7] += 1

        else:
            print('未中獎 再接再厲')

    else:
        print('未中獎 再接再厲')


# 列出全部機率
print('\n總共', times, '張')

for name, value in lucky.items():
    print(name, '獎', value, '張', '  機率是', value * 100 / times, '%')
