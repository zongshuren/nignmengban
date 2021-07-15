import random

import requests
from faker import Faker
class NewXueyuan(object):

    def __init__(self):
        self.faker = Faker('zh-CN')
        self.sex = [True, False]
        self.grade = ['初一', '初二', '初三', '高一', '高二', '高三']
        self.division = ['文科', '理科']
        self.channel_tag = ['学校名单', '活动采单', '客户介绍', '机构合作', '渠道购买', '地推']
        self.tag = ['1级', '2级']
        self.school_name= ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
        # self.birthday = self.faker.date_between(start_date="-11y", end_date="today")
        # self.community = self.faker.address()
        # self.lexue_id = self.faker.random_number(digits=8)
        # self.score_before = self.faker.random_int(99, 660)
        # self.rank_before = self.faker.random_int(1, 99)

    def data_preparation(self):
        sex = random.choice(self.sex)
        grade = random.choice(self.grade)
        division = random.choice(self.division)
        channel_tag = random.choice(self.channel_tag)
        tag = random.choice(self.tag)
        school = random.choice(self.school_name)
        score_before = self.faker.random_int(99, 660)
        rank_before = self.faker.random_int(1, 99)
        birthday = self.faker.date_between(start_date="-11y", end_date="today")
        community = self.faker.address()
        lexue_id = self.faker.random_number(digits=8)
        name = self.faker.name()
        phone = self.faker.phone_number()
        phone2 = self.faker.phone_number()
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
        self.json = {"name": f"{name}",
                "nickname": "",
                "phone": f"{phone}",  # 手机号
                "sex": sex,
                "birthday": f"{birthday}",
                "status": 0,
                "tag": f"{tag}",  # 可能性
                "stage_id": 4805,
                "school": f"{school}大学",
                "grade": f"{grade}",
                "division": f"{division}",
                "second_phone": f"{phone2}",  # 第二手机号
                "score_before": f"{score_before}",
                "rank_before": f"{rank_before}",
                "channel_tag": f"{channel_tag}",  # 来源
                "community": f"{community}",  # 地址
                "lexue_id": f"{lexue_id}",  # 乐学号
                "is_valid": True,  # 有效性
                "customized_tag": "[\"高三数学\"]",  # 标签
                "salesList": "[{\"label\":\"宗树仁\",\"value\":2127}]",  # 销售
                "teachersList": "[{\"value\":2127,\"label\":\"宗树仁\"}]",  # 教师
                "schoolAdminList": "[{\"value\":2127,\"label\":\"宗树仁\"}]"}
        # print(self.json)
        return self.url, self.headers, self.json
        # res = requests.post(url=url, headers=headers, json=json)
        # print(res.json())
    def create(self,num):

        for i in range(num):
            url, headers, josn = self.data_preparation()
            # res = requests.post(url=url, headers=headers, json=josn)
            print(josn)
            # print(res.json())

if __name__ == '__main__':

    NewXueyuan().create(10)
