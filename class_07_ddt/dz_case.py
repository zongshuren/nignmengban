# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/30 19:43
"""
import unittest
import requests
import time
from ddt import ddt, data
from class_06.get_token import GetToken
import do_excel

test_data = do_excel.DzExcel(r'C:\Users\Administrator\Desktop\测试.xlsx', 'Sheet1').get_data2()
nowTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())


@ddt
class DzCase(unittest.TestCase):

    def setUp(self):
        url = 'http://dztsl.lexue.com/api/auth/login'
        date = {'username': '18410073181', 'password': '1234567', 'tenant_id': 150, 'openid': ''}
        try:
            res = requests.post(url=url, data=date)
            if res.json()['token']:
                setattr(GetToken, 'Token', res.json()['token'])
            else:
                print('没有Token，请指示')
        except KeyError:
            print('token获取失败')
            # raise KeyError
        self.headers = {
            'Host': 'dztsl.lexue.com',
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json',
            'Authorization': getattr(GetToken, 'Token'),
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://dztsl.lexue.com',
            'Referer': 'http://dztsl.lexue.com/mavinSales/'
        }
        self.nowTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())

    @data(*test_data)
    def test_dz_addCommonActivity(self, test_data):
        try:
            res = requests.post(json=eval(test_data['data']), url=test_data['url'], headers=self.headers)
            self.assertEqual('Add activity successfully.', res.json()['error_message'])
        except Exception as e:
            print('用例test_dz_addCommonActivity报错：{0}'.format(e))
            raise e
        print(res.json())

    def tearDown(self):

        print('此条用例执行结束时间：', time.strftime("%Y-%m-%d %H:%M", time.localtime()))
