# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/7 20:00
"""
import random


class Rock_Scissors_paper():

    role_dict = {1: '曹操', 2: '刘备', 3: '诸葛亮'}
    paper_dict = {1: '剪刀', 2: '石头', 3: '布'}

    def get_role_name(self):

        role_num = input('选择角色1:曹操,2:刘备,3:诸葛亮')

        return self.role_dict[int(role_num)]

    def get_role_fist(self):

        quan_num = input('请出拳1:剪刀,2:石头,3:布')

        return int(quan_num)

    def get_computer_fist(self):

        computer_num = random.randint(1, 3)

        return computer_num

    def game_begin(self):
        role_name = self.get_role_name()
        role_quan = self.get_role_fist()
        comp_name = self.get_computer_fist()
        print('角色为{0}'.format(role_name))
        role_win = 0
        comp_win = 0
        ping = 0
        while True:
            if role_quan-comp_name == 1 or role_quan-comp_name == 2:
                role_win += 1
                print('{0}赢了'.format(role_name))
            elif role_quan-comp_name == -1 or role_quan-comp_name == -2:
                comp_win += 1
                print('电脑赢了')
            elif role_quan-comp_name == 0:
                ping += 1

            jixu = input('按n退出游戏')

            if jixu == 'n':

                break

if __name__ == '__main__':

    print(Rock_Scissors_paper().game_begin())