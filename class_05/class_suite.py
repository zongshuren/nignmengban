# -*- coding: utf-8 -*-
"""
@Author:ShuRen
@Time:2021/7/22 10:51
"""
import unittest
import sys
import HTMLTestRunner
from class_05.class_unittest import TestMathMethod, TestMulti
from class_05 import class_unittest
suite = unittest.TestSuite()  # 存储用例
# 方法1
# suite.addTest(TestMathMethod('test_add_two_positive'))  # 具体到某一个用例
# suite.addTest(TestMathMethod('test_add_two_zero'))

# 方法2
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))  # 查找出类下的所有测试用例
# suite.addTest(loader.loadTestsFromTestCase(TestMulti))  # 查找出类下的所有测试用例

suite.addTest(loader.loadTestsFromModule(class_unittest))  # 查找出模块下的所有用例

# file = open('test.txt', 'w+', encoding='utf-8')
# runner = unittest.TextTestRunner(stream=file, verbosity=1)
# runner.run(suite)

# 执行使用上下文管理器
# with open('test.txt', 'w+', encoding='utf-8') as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=1)
#     runner.run(suite)
# print(file.closed)

with open('test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='宗树仁测试报告', description='测试报告')
    runner.run(suite)
print(file.closed)