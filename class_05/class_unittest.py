# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/19 20:28
"""

# 功能测试
# 写用例 TestCase
# 执行用例1：TestSuite 储存用例 2:TestLoader 找用例 ，加载用例 ，存到1的TestSuite
# 对比实际结果 期望结果 判定用例是否通过 # 断言 Assert
# 出具测试报告 TextTestRunner
import unittest

from class_05.math_method import MathMethod

class TestMathMethod(unittest.TestCase):

    def test_add_two_positive(self):
        res = MathMethod(1, 1).add()
        print('1加1的结果是', res)
        # self.assertEqual(3, res, msg='1加1的用例断言错误')  # 两个值相等执行成功
        try:
            self.assertEqual(3, res, msg='1加1的用例断言错误')  # 两个值相等执行成功
            # self.assertNotEqual(1, res, msg='1加1的用例断言错误')  # 两个值不相等执行成功
            # self.assertTrue(res)  # 判断返回的布尔值是否为True
            # self.assertFalse(res) # 判断返回的布尔值是否为False
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e


    def test_add_two_zero(self):
        res = MathMethod(0, 1).add()
        print('0加1的结果是', res)
        try:
            self.assertEqual(1, res, msg='0加1用例错误')
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e

    def test_add_two_negative(self):
        res = MathMethod(-1, -2).add()
        print('-1加-2的结果是', res)
        try:
            self.assertEqual(-3, res, msg='-1 - -2用例错误')
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e



class TestMulti(unittest.TestCase):

    def test_multi_two_positive(self):
        res = MathMethod(1, 1).multi()
        print('1乘以1的结果是', res)
        try:
            self.assertEqual(1, res, msg='1*1用例错误')
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e

    def test_multi_two_zero(self):
        res = MathMethod(0, 1).multi()
        print('0乘以1的结果是', res)
        try:
            self.assertEqual(0, res, msg='0*0用例错误')
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e

    def test_multi_two_negative(self):
        res = MathMethod(-1, -2).multi()
        print('-1乘以-2的结果是', res)
        try:
            self.assertEqual(1, res, msg='-1 * -2用例错误')
        except AssertionError as e:
            print('出错了，错误是{0}'.format(e))
            raise e

if __name__ == '__main__':

    unittest.main()
