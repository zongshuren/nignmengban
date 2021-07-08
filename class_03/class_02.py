list1 = [12, 78, 88]

zidian = {'语文': 88, '数学': 99, '英语': 99, '物理': 'hehe'}
list2 = []
# print(max(zidiann.values()))
for i in zidian.values():
    list1.append(i)
# a = max(list1ist1)
# print(a)
for i in list1:
    b = str(i)
    if b.isdigit():
        list2.append(int(b))
c = max(list2)

chengji = 0
kemu = []
for key in zidian:
    # print(key)
    if zidian[key] == c:
        chengji += 1
        n = zidian[key]
        kemu.append(key)
        kemu.append(n)
print('成绩最高的有{0}科'.format(chengji))
print(kemu)