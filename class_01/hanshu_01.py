
# The file image.png has been uploaded.


# from fnmatch import translate
#
#
def num(a, num):
    a = a
    for i in range(num):
        a += i
    return a

n = print('nihao')
print(n)

#
# intab = 'abcdefghigklmnopqrstuvwxyz'
# outtab = '1234567890,./;=-`~!#$%^&*('
# trantable = str.maketrans(intab, outtab)
# atable = str.maketrans(outtab,intab)
#
# str = 'this is may book ault'
# b = str.translate(trantable)
# a = str.translate(atable)
# print(b)
# print(a)

# def changdu(chang):
#     a = len(chang)
#     if a >= 2:
#         b = chang[0:2]
#         return b
#     else:
#         print('长度大于2')
#
# print(changdu('哈哈哈哈'))
#
# def tusi(*args):
#     # print(type(args))
#     # alltu=''
#     # for i in args:
#     #     alltu += i
#     #     alltu += '、'
#     str(args)
#     return args
# print(type(tusi()))
# b = tusi('翻墙', '土豆', '鸡蛋')
# print(b)

# a = 10
#
# def gel(b):
#     global a
#     a = ''
#     int(a)
#     a += b
#     print(a)
# gel(11)

# num = input('请输入4位数字：')
# i = ''
# for item in num:
#     i += str((int(item) + 5) % 10)
#
# print(i[::-1])
# d = 2
# st = 'Runoob'
# print(st[:len(st)-d])


# def rotate(input, d):
#     Lfirst = input[0: d]
#     print(Lfirst)
#     Lsecond = input[d:]
#     print(Lsecond)
#     Rfirst = input[0: len(input) - d]
#     print(Rfirst)
#     Rsecond = input[len(input) - d:]
#     print(Rsecond)
#
#     print("头部切片翻转 : ", (Lsecond + Lfirst))
#     print("尾部切片翻转 : ", (Rsecond + Rfirst))
#
#
# if __name__ == "__main__":
#     input = 'Runoob'
#     d = 2  # 截取两个字符
#     rotate(input, d)

