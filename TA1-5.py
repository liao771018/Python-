# 戶籍代表字母
# A台北市　B台中市　C基隆市　D台南市　E高雄市　F台北縣
# G宜蘭縣　H桃園縣　I 嘉義市　J新竹縣　K苗栗縣　L台中縣
# M南投縣　N彰化縣　O新竹市　P雲林縣　Q嘉義縣　R台南縣
# S高雄縣　T屏東縣　U花蓮縣　V台東縣　W金門縣　X澎湖縣
# Y陽明山　Z連江縣
ID = input()
# ID = 'A123456781'# 
# 英文字母代表的數字
places = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J' ,'K' ,'L' ,'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', 'I', 'O']
# A=10 B=11 C=12 D=13 E=14 F=15 G=16 H=17 I=34 J=18 K=19 L=20
# M=21 N=22 O=35 P=23 Q=24 R=25 S=26 T=27 U=28 V=29 W=32 X=30
# Y=31 Z=33

# for i in range (len(places)):
#   print(places[i],i + 10)
# 性別代表數字
# 1：男性
# 2：女性
sex = [1, 2]

id_place = ID[0]
id_num = list(ID[1:10])
# print(type(id_place))
# print(id_num)
check_num = 0

if id_place in places:
  num = str(places.index(id_place) + 10)
  place_num = int(num[0]) + int(num[1]) * 9
  # print(place_num)
  # print(type(place_num))

  for i in range ( len(id_num) - 1):
    check_num = check_num + int(id_num[i]) * (8 - i)
  check_num = check_num + int(id_num[-1]) * 1
  # print(check_num)

  check_num = check_num + place_num
  if check_num % 10 == 0:
    print('合法')
  else:
    print('不合法')

  

else:
  print('不合法')