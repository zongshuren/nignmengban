# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/31 15:31
"""
import unittest
import HTMLTestRunner
from class_06 import dz_case

suit = unittest.TestSuite()
loder = unittest.TestLoader()

suit.addTest(loder.loadTestsFromModule(dz_case))

with open('dz.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='多招测试用例', description='zsr')
    runner.run(suit)