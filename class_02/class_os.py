import os

# 新建一个目录/新建一个文件夹
# os.mkdir('Alisa')
# 跨级新建目录 用/表示不同的层级，必须确保上面的层级是存在的
# os.mkdir('Alisa/aixinru/abs.py')  # 相对路径

# os.mkdir(r'/Users/zongshuren/Desktop/test1')

# 删除 只能删除空文件夹 否则会报错
# os.rmdir('Alisa')
# os.remove(r'Alisa\aixinru')
# os.path.isfile('Alisa/aixinru')
# os.mknod('Alisa/aixinru/abs.txt')

# chdir()改变当前工作目录为指定目录
# os.chdir('/Users/zongshuren/PycharmProjects/nignmengban/class_02/Alisa/aixinru')
# ss = open('text01.txt', 'w')
# getcwd()获取当前路径 相对路径
# a= os.getcwd()
# print(a)
# 删除一个文件
# os.remove('/Users/zongshuren/PycharmProjects/nignmengban/class_02/Alisa/aixinru/text.txt')

# 获取当前文件的绝对路径 __file__指的当前文件本身
# file = os.path.realpath(__file__)
# print(file)
# import sys
#
# f, b = os.path.split(os.path.abspath(sys.argv[0]))
# er =os.path.abspath(sys.argv[0])
# et = os.path.abspath(sys.argv[0])
# # print(f, b)
# # print(sys.argv[0])
# print(et)
# wy = os.path.abspath(sys.argv[0])
# print(wy)

# path 连接路径 可以添加多个上级目录

# path_list = ['python11', 'python22', 'python33']
#
# for i in path_list:
#     path_2 = os.path.join(os.getcwd(), i)
#     os.mkdir(path_2)
#
# # 判断路径是否是路径
# print(os.path.isdir(os.getcwd()))
# # 判断是否是文件
# print(os.path.isfile(__file__))
# # 判断文件是存在
# print(os.path.exists(os.getcwd()+'/text01.txt'))
# 列出当前路径所有文件路径
# lis_path = os.listdir(os.getcwd())
# print(lis_path)
# for all_path in os.listdir(os.path.abspath(os.path.dirname(__file__))):
#     if os.path.isdir(all_path):
#         print(os.path.join(os.path.abspath(os.path.dirname(__file__)), all_path))
#         print('{0}还需要做进一步处理'.format(all_path))
#     else:
#         print(os.path.join(os.path.abspath(os.path.dirname(__file__)), all_path))


# os.walk()简单易用的文件、目录遍历器
# path = r'/Users/zongshuren/PycharmProjects/nignmengban/class_02/'
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)

# path = r'/Users/zongshuren/PycharmProjects/nignmengban/class_02/'
# for dirpath, dirnames, filenames in os.walk(path):
#     for filename in filenames:
#         print(os.path.join(dirpath, filename))
# if __name__ == '__main__':
#