# -*- coding:UTF-8 -*-
a = '1：file 文件open之后默认是 r 只读模式 如果要写入内容会报错 io.UnsupportedOperation: not writable\n' \
    '2：r+可读可写 先写的话 从头开始覆盖写 读光标之后的内容 读写跟着光标走\n' \
    '3：如果要写入中午 要注意编码格式\n' \
    '4: w 只写 会先清空 硬要去读会报错 io.UnsupportedOperation: not readable\n' \
    '5: w+ 可读可写 不管是w 还是w+ 如果文件存在 直接清空在重新写入，如果文件不存在 则新建一个文件然后写入\n' \
    '6: a追加 a+ 如果文件存在 就直接追加写 写在后面 如果不存在 则新建一个文件进行写入\n' \
    '7: readline(size) 方法用于从文件读取整行 size 从文件中读取的字节数，返回从字符串中读取的字符\n' \
    '8: readlines() 方法用于读取所有行，并返回列表格式 可以用for in 结构进行处理\n' \
    '9: writelines(['',''])方法用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。换行需要制定换行符 \n。' \
    ''
file = open('suixinxi.txt', 'w+')
# file.write(a)
print('文件名为：', file.name)
file.write(a)
file.close()
# for ln in file.readlines():
#     ln = ln.strip()
#     print('读取的数据为：',ln)
# b = file.readline(10)
# print(b)
