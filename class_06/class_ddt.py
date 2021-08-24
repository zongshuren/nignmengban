from ddt import ddt, data, unpack
import unittest

test_data = [[1, 2], [3, 4, 5]]
test_data1 = [{'no': 1, 'name': '名字'}, {'no': 2, 'name': '名字2'}]

@ddt  # 装饰测试类
class TestMath(unittest.TestCase):
    #
    # @data(*test_data1)  # 装饰测试方法，拿到几个数据就执行几条用例
    # @unpack  # 参数过多不适用
    # def test_print_data(self, no, name):
    #     print('no:', no)
    #     print('name:', name)

    @data(*test_data1)  # 装饰测试方法，拿到几个数据就执行几条用例
    def test_print_data1(self, no):
        print('no:', no['no'])
        print('name:', no['name'])
