print('Please input the limit money and the price of items(all number should <= 10000):')
#支持多行输入并将输入存在line中
sentinel = ''
line = list('\n'.join(iter(input, sentinel)).split())
#两行字符串拆分为限额limit和单价price（列表），并转为整型
choose = list(map(int, line))
limit = choose[0]
choose.pop(0)
#判断输入的数字是否小于10000，正整数判断不太会写，求指教（输入判断待完善）
for price in choose:
    if price > 10000 or limit > 10000:
        print('Wrong input!')
        break
#判断单价中的最小值是否超出限额
if min(choose) > limit:
    print('Over the limit!')
#在总价不超出限额且单价列表不为空的情况下计算总价
else:
    total = 0
    while (total + min(choose, default=0)) <= limit and len(choose) > 0:
            total = total + min(choose)
            choose.pop(choose.index(min(choose)))
    print(total)
