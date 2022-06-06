# -*- coding: utf-8 -*-
"""
@Author:ZongShuRen
@Time:2021/7/31 14:33
"""
class GetToken:

    Token = None  # 存储Token 初始值为None

if __name__ == '__main__':

    print(GetToken.Token)
    setattr(GetToken, 'Token', 'zongshurne')
    print(getattr(GetToken, 'Token'))
    print(hasattr(GetToken, 'Token'))
    delattr(GetToken, 'Token')
    print(hasattr(GetToken, 'Token'))
