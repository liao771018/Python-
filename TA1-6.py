# 閨年判斷
# 西元年份除以4不可整除，為平年。
# 西元年份除以4可整除，且除以100不可整除，為閏年。
# 西元年份除以100可整除，且除以400不可整除，為平年
# 西元年份除以400可整除，為閏年。

year = int(input())
# year = 2000
# year = 1900
# year = 1996
# year = 1999
# year = 2002

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print('True')
        else:
            print('False')
    else:
        print('True')
else:
    print('False')
