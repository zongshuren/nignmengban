import os
import re

file = open(r'D:\pycharm-professional-2017.2.3\nignmengban\class_07\rukudata.txt', 'r', encoding='utf-8')
aa = file.readlines()
b = []
c = []
for i in aa:
    b.append(i.replace('\n', ''))
for j in b:
    c.append(j.replace(' ', ''))
print(c)

alist = []
for i in c:
    alist.append(i.split(':'))
print(alist)

b1 = {}
for i in alist:
    b = dict(zip(i[0::2], i[1::2]))
    b1.update(b)
    # print(b)
print(b1)

file.close()
