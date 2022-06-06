# a = 0
# b = 100
# while b >= 0:
#     a = a+b
#     b = b-1
#
# print(a)d

# a = 10
# b = 0
# while a >= 0:
#     sex = input('请输入你的性别：')
#
#     if sex == 'v':
#         a = a - 1
#         age = int(input('请输入你的年龄：'))
#         if 10 <= age <= 12:
#             print('恭喜你加入我们')
#             b += 1
#         else:
#             print('对不起你不符合我们的要求')
#
#     else:
#         print('对不起你不符合我们的要求')
#         a -= 1
#     if a == 0:
#         break  # 跳出循环
#     else:
#         continue  # 结束本轮循环继续下一轮
#
# print('符合的人数有{}人'.format(b))

userandpassword = {'admin': '123456', 'power': '654321'}

# a = 3
# while True:
#     name = input('请输入用户名')
#     while name in userandpassword:
#         password = input('请输入密码')
#         if password != userandpassword[name]:
#             print('密码不正确')
#             a -= 1
#             if a == 0:
#                 print('输入次数超过三次')
#                 break
#             else:
#                 print('输入次数剩余{}次重新输入密码'.format(a))
#                 continue
#         elif password == userandpassword[name]:
#             print('密码正确')
#             break
#         else:
#             print('账号不存在')
#     bn = input('用户OR密码不正确是否从新输入？请输入Y/N：')
#     if bn == 'Y':
#         print('重新进入登录流程')
#         continue
#     elif bn == 'N':
#         print('退出登录流程')
#         break
#     else:
#         print('输入不合法退出登录流程')
#         break
#
# print('新建用户N/n')
# print('登录E/e')
# print('退出程序Q/q')
# ci = 3
# while True:
#     et = input('请输入指令代码：')
#     if et == 'N' or et == 'n':
#         name = input('请输入用户名：')
#         while name in userandpassword:
#             name = input('用户已经存在，请重新输入：')
#         userandpassword[name] = input('请输入密码：')
#         print('注册成功试试登录吧')
#     elif et == 'E' or et == 'e':
#         name = input('请输入用户名：')
#         while name not in userandpassword:
#             name = input('用户名不存在请重新输入')
#         psdr = input('请输入密码：')
#         while psdr != userandpassword[name]:
#             psdr = input('密码不正确，请重新输入：')
#             print('登录成功')
#             ci -= 1
#             print('您还有{}次机会'.format(ci))
#             if ci == 0:
#                 print('重试次数过多，退出登录')
#                 break
#             else:
#                 continue
#     elif et == 'Q' or et == 'q':
#         break
#     else:
#         print('无效指令')
#         continue
# print(userandpassword)

# a = [[1, 2, 3], [5, 5, 6], [7, 8, 9]]
# init_i = 0
# init_j = 0
# flag = True
# for i in range(3):
#     print(i)
#     for j in range(3):
#         # print(i, j)
#         if a[i][j] == 5:
#             # print(a[i][j])
#             flag = False
#             init_i = i
#             init_j = j
#             break
#     else:
#         continue
#     break
    # if not flag:
    #     break
# print(init_i, init_j)

count = 0
while 1:
    print('爱你哟')
    count += 1
    if count == 10:
        break

    a = [
        1,
        2,
        3
    ]
    print(a)