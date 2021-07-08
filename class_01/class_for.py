# 循环for while
# s = 'hello'
# a = {'name': 'shuren', 'age': '18', 'sex': '男'}
# b = [11, 22, 1, True, [1, 2, 3]]
# c = '10'
# for item in c:
#     for d in item:
#         print(d)

# L = [5, 6, 9, 3, 7]
# a = 0
# for a in L:
#     print(a)
# # print(L)
# a = {'name': 'shuren',
#      'age': '18',
#      'sex': '男'}
# for iten in a:
#     L.append(a[iten])
#     print(a[iten])

# for iten in range(len(L)):
#     print(L[iten])
#     L.append(L[iten])
# print(L)

#
# a = 0
# for i in range(1, 101):
#     print(i)
#     a += i
# print(a)
#
# for i in range(10):
#
#     for c in range(1, i+1):
#         print(i,'*',c,'=',i*c, end='  ')
#     print(' ')
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print(' ')

#
# name = ['huahua', 'niangao', 'tingting', 'kaka']
#
# for i in name:
#     print(i)
#     username = input('请输入你的名字：')
#     if username == i:
#         print('用户名正确！')
#     else:
#         print('用户名不存在')

# for i in range(1,6):
#     for j in range(1,6-i):
#         print('  ', end='')
#     for b in range(1,i+1):
#         print(' *  ', end='')
#     print('')
# 利用for 循环
# 冒泡排序 相邻两个元素依次比较， 一般最多比较n-1次
# a = [1, 7, 4, 3, 6, 5, 2]
#
#
# for i in range(1, (len(a))):
#     for j in range(0, len(a)-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#     print(a)
def city_hanshu(name,city,six='n'):
    # print(six)
    if six == 'n':
        if city =='changsha':
            return name, six, city,True
        else:
            print('城市不符合', False)
    else:
        print('性别不符合',False)
if __name__ == '__main__':
    b = city_hanshu('张三', 'changsh')
    print(b)


# def fanmaiji():
#     print('这是一个贩卖机')
#     money = input('请投币')
#     money = int(money)
#     if money == 1 or money == 5 or money == 10:
#         commodity = input('请输入商品编码，1.橙汁，2.椰汁,3.矿泉水，4.早餐奶：')
#         commodity = int(commodity)
#         if commodity == 1:
#             print('选择的商品为橙汁')
#             print('找零{0}'.format(money-3.5))
#     else:
#         print('输入的金额不为1，5，10元')
# if __name__ == '__main__':
#     fanmaiji()
