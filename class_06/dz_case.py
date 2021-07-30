# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/30 19:43
"""
import unittest
import requests
import time
COOKIES = None
class DzCase(unittest.TestCase):

    def setUp(self):
        url = 'http://dztsl.lexue.com/api/auth/login'
        date = {'username': '18410073181', 'password': '1234567', 'tenant_id': 150, 'openid': ''}
        res = requests.post(url=url, data=date)
        self.token = res.json()['token']
        self.headers = {
            'Host': 'dztsl.lexue.com',
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json',
            'Authorization': f'{self.token}',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://dztsl.lexue.com',
            'Referer': 'http://dztsl.lexue.com/mavinSales/'
        }
        self.nowTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())


    def test_dz_getUserActListByDateWithRoleAndUser(self):

        global COOKIES
        getUserActListByDateWithRoleAndUser_url = 'http://dztsl.lexue.com/api/ai/getUserActListByDateWithRoleAndUser?date=2021-7-30&role=consultant&username=18410073181&actType=S_LOV_SALES'
        res = requests.get(url=getUserActListByDateWithRoleAndUser_url, headers=self.headers)

        try:
            self.assertEqual('Get user act list successfully.', res.json()['error_message'])
        except AssertionError as e:
            print('用例test_dz_getUserActListByDateWithRoleAndUser报错：{0}'.format(e))
            raise e
        print(res.json())

    def test_dz_addCommonActivity(self):

        addCommonActivity_url = 'http://dztsl.lexue.com/api/activities/addCommonActivity'
        data = {"title": "自动化日常测试", "content": "自动化任务测试", "time": f"{self.nowTime}", "end_time": f"{self.nowTime}", "employee": "[{\"label\":\"宗树仁\",\"value\":2127}]", "rolePlay": "consultant", "type_id": 4745, "status": 0}
        res = requests.post(url=addCommonActivity_url, json=data, headers=self.headers)
        # print(res.json())
        try:
            self.assertEqual('Add activity successfully.', res.json()['error_message'])
        except AssertionError as e:
            print('用例test_dz_addCommonActivity报错：{0}'.format(e))
            raise e
        print(res.json())

    def test_time(self):
        print(time.strftime("%Y-%m-%d %H:%M", time.localtime()))


    def tearDown(self):
        print('这条结束啦')

