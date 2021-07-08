# age = 17
# if age>=18:
#     print('您已经成年了')
# else:
#     print('你还小')

s = input("请输入a年龄：")  # 空数据 false 非空数据true

# if s.isdigit():
#     s = int(s)
#     if s >= 18:
#         print("你成年了")
#     elif 18 > s >= 0:
#         print('加油长大')
#     else:
#         print("不准许为负数")
# else:
#     print('输入不合法')
s = int(s)
if s >= 18:
    print('你的年龄是{}已经满18岁可以上网吧了'.format(s))
else:
    print('小伙子才{}太年轻了过几年再来玩'.format(s))