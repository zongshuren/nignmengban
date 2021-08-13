import time


class A_Time:

    def a_time(self, struct_time):  # 传入时间戳
        # 获得当前时间时间戳
        # struct_time = int(time.time())
        timeArray = time.localtime(struct_time)

        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)

    from multiprocessing import cpu_count
    from multiprocessing import Process



if __name__ == '__main__':

    A_Time().a_time(1628841273)

#
# from multiprocessing import cpu_count
# from multiprocessing import Process
# def func():  # 死循环函数,让cpu满载
#     while True:
#         pass
#
# if __name__ == '__main__':
#     p_lst = []  # 定义一个列表
#     core_count = cpu_count()  # CPU核心数
#     for i in range(core_count):
#         p = Process(target=func)  # 子进程调用函数
#         p.start()  # 启动子进程
#         p_lst.append(p)  # 将所有进程写入列表中
#     for p in p_lst : p.join()  # 检测p是否结束,如果没有结束就阻塞直到结束,否则不阻塞
#     from multiprocessing import cpu_count
#     from multiprocessing import Process
#
#     print('结束')
