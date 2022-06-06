# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/31 15:31
"""
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from class_07.ph_case import DzCase


suit = unittest.TestSuite()
loder = unittest.TestLoader()

# 一次性加载出测试类里的所有测试用例
suit.addTest(loder.loadTestsFromTestCase(DzCase))
  
with open('dz_case.html', 'wb') as file:

    runner = HTMLTestRunner(stream=file, verbosity=2, title='多招测试用例', description='zsr')
    runner.run(suit)
