print('Please input the date and the string:')
#多行输入存为line，转换为列表
sentinel = ''
line = '\n'.join(iter(input, sentinel))
sss = list(line)
#在三个列表中分别存放月、日、输入的字符串，并将月、日转为整型
s1 = []
s2 = []
s3 = []
n = 0
while sss[n] != ' ':
    s1.append(sss[n])
    sss.pop(n)
sss.pop(0)
while sss[n] != '\n':
    s2.append(sss[n])
    sss.pop(n)
sss.pop(0)
if len(s1) > 1:
    m = int(s1[0])*10+int(s1[1])
else:
    m = int(s1[0])
if len(s2) > 1:
    d = int(s2[0])*10+int(s2[1])
else:
    d = int(s2[0])
#用二维列表ss存放编码
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
b = ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
c = ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
ss = [a, b, c]
#设计左移规则
t = []
while m > 1:
    t = ss[0]
    ss.pop(0)
    ss.append(t)
    m = m-1
t1 = []
t2 = []
t3 = []
while d > 1:
    t1 = a[0]
    a.pop(0)
    a.append(t1)
    t2 = b[0]
    b.pop(0)
    b.append(t2)
    t3 = c[0]
    c.pop(0)
    c.append(t3)
    d = d-1
#对输入的字符串进行查找匹配并输出对应数字
for x in sss:
    if x in a:
        print(str(ss.index(a)+1) + str(a.index(x)+1), end=' ')
    elif x in b:
        print(str(ss.index(b)+1) + str(b.index(x)+1), end=' ')
    else:
        print(str(ss.index(c)+1) + str(c.index(x)+1), end=' ')
