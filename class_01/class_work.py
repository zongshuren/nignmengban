# encoding:utf-8
#
# goumaijiner = input("请输入购买金额：")
#
# if goumaijiner.isdigit():
#     a = int(goumaijiner)
#     if 0<= a < 50:
#         print("您的购买金额是{0}无法享受优惠".format(a))
#     elif 50 <= a <=100:
#         print('您的购买金额是{0}可以享受优惠10%，优惠后价格为{1}'.format(a, a*(1-0.1)))
#     elif a > 100:
#         print('您的购买金额是{0}可以享受优惠20%，优惠后价格为{1}'.format(a, a*(1-0.2)))
# else:
#     print('请输入整数')
import random
a = random.randint(1, 10)
print(a)
b = int(input('请输入1-10之间的整数：'))

if a > b:
    print('bigger')
elif b > a:
    print('less')
elif b == a:
    print('equal')
