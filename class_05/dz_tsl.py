# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/26 20:26
"""
import requests
from requests import request

class Get_Dz_Token():

    def __init__(self):
        self.url = 'http://dztsl.lexue.com/api/auth/login'
        self.date = {'username': '18410073181', 'password': 'null', 'tenant_id': 150, 'openid': ''}

    def get_token(self):

        res = requests.post(url=self.url, data=self.date)
        print(res.text)
        # cookies = res.cookies
        # token = res.json()['token']
        try:
            token = res.json()['token']
            # print(token)
            return token
        except KeyError as e:
            print('token获取失败，未找到token')


        print('hello')






if __name__ == '__main__':
    Get_Dz_Token().get_token()
    # print(Get_Dz_Token().get_token())