# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/7 20:00
"""
import random


class Rock_Scissors_paper():

    role_dict = {1: '曹操', 2: '刘备', 3: '诸葛亮'}
    paper_dict = {1: '剪刀', 2: '石头', 3: '布'}

    # def get_role_name(self):
    #     role_num = input('选择角色1:曹操,2:刘备,3:诸葛亮')
    #     if int(role_num) not in self.role_dict:
    #         print('角色不存在，请重新选择')
    #         self.game_begin()
    #     else:
    #         # print(self.role_dict[int(role_num)])
    #         return self.role_dict[int(role_num)]


    def get_role_name(self):

        try:

            role_num = input('选择角色1:曹操,2:刘备,3:诸葛亮')

            if int(role_num) not in self.role_dict:

                print('角色不存在，请重新选择')
                return self.get_role_name()

            else:
                return self.role_dict[int(role_num)]

        except Exception:

            print('选择错误请重新选择')

            return self.get_role_name()

    def get_role_fist(self):

        try:

            quan_num = input('请出拳1:剪刀,2:石头,3:布')
            if int(quan_num) > 3:

                print('出拳错误，请输入1-3')
                return self.get_role_fist()

            else:
                return int(quan_num)

        except Exception:

            print('输入有误请重新输入')
            return self.get_role_fist()

    def get_computer_fist(self):

        computer_num = random.randint(1, 3)

        return computer_num

    def game_begin(self):

        role_name = self.get_role_name()
        print('角色为{0}'.format(role_name))
        role_win = 0
        comp_win = 0
        ping = 0
        while True:
            role_quan = self.get_role_fist()
            comp_name = self.get_computer_fist()
            if role_quan-comp_name == 1 or role_quan-comp_name == 2:
                role_win += 1
                print('{0}赢了'.format(role_name))
            elif role_quan-comp_name == -1 or role_quan-comp_name == -2:
                comp_win += 1
                print('电脑赢了')
            elif role_quan-comp_name == 0:
                print('平局')
                ping += 1
            jixu = input('按n退出游戏,输入其他继续')
            if jixu == 'n':
                break
        print('游戏结束{0}赢了:{1}次,电脑赢了{2}次,平局{3}次'.format(role_name, role_win, comp_win, ping))


if __name__ == '__main__':

    Rock_Scissors_paper().game_begin()
