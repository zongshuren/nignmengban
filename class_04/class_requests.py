import random

import requests
from faker import Faker
class NewXueyuan:
    def __init__(self):
        self.faker = Faker('zh-CN')
        self.sex = [True, False]
        self.grade = ['初一', '初二', '初三', '高一', '高二', '高三']
        self.division = ['文科', '理科']
        self.birthday = self.faker.date_between(start_date="-11y", end_date="today")
        self.community = self.faker.address()
        self.lexue_id = self.faker.random_number(digits=8)

    def data_preparation(self):
        sex = random.choice(self.sex)
        grade = random.choice(self.grade)
        division = random.choice(self.division)
        self.url = 'http://dztsl.lexue.com/api/customers'
        self.headers = {
                    'Host': 'dztsl.lexue.com',
                    'Proxy-Connection': 'keep-alive',
                    'Accept': 'application/json',
                    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOjE1MCwic3RhIjoxNjI1ODI1MDc2OTAyLCJleHAiOjE2MjY0Mjk4NzY5MDIsInVzciI6IjE4NDEwMDczMTgxIn0.J2HmMdL4ZCQXxTOeOeihriw4Z-AyFYvk-waEXKHWmgM',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Origin': 'http://dztsl.lexue.com',
                    'Referer': 'http://dztsl.lexue.com/mavinSales/'
                 }
        self.json = {"name": f"{self.faker.name()}",
                "nickname": "",
                "phone": f"{self.faker.phone_number()}",  # 手机号
                "sex": sex,
                "birthday": f"{self.birthday}",
                "status": 0,
                "tag": "1级",
                "stage_id": 4805,
                "school": "这是学校名字",
                "grade": f"{grade}",
                "division": f"{division}",
                "second_phone": f"{self.faker.phone_number()}",  # 第二手机号
                "score_before": "99",
                "rank_before": "10",
                "channel_tag": f"{self.faker.address()}",  # 来源
                "community": f"{self.community}",  # 地址
                "lexue_id": f"{self.lexue_id}",  # 乐学号
                "is_valid": True,  # 有效性
                "customized_tag": "[\"高三数学\"]",  # 标签
                "salesList": "[{\"label\":\"宗树仁\",\"value\":2127}]",  # 销售
                "teachersList": "[{\"value\":2127,\"label\":\"宗树仁\"}]",  # 教师
                "schoolAdminList": "[{\"value\":2127,\"label\":\"宗树仁\"}]"}
        print(self.json)
        return self.url, self.headers, self.json
        # res = requests.post(url=url, headers=headers, json=json)
        # print(res.json())
    def create(self):
        url, headers, josn = self.data_preparation()

        res = requests.post(url=url, headers=headers, json=josn)

        print(res.json())

if __name__ == '__main__':

    NewXueyuan().create()
