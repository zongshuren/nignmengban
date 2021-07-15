import requests
from faker import Faker
faker = Faker('zh-CN')
class NewXueyuan:
    def __init__(self):
        self.faker = faker
        self.sex = [True, False]
        self.grade = ['初一', '初二', '初三', '高一', '高二', '高三']
        self.division = ['文科', '理科']
        self.birthday = faker.date_between(start_date="-11y", end_date="today")
        self.community = faker.address()
        self.lexue_id = faker.random_number(digits=8)

    def create(self):
        url = 'http://dztsl.lexue.com/api/customers'
        headers = {
                    'Host': 'dztsl.lexue.com',
                    'Proxy-Connection': 'keep-alive',
                    'Content-Length': '515',
                    'Accept': 'application/json, text/plain, */*',
                    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOjE1MCwic3RhIjoxNjI1ODI1MDc2OTAyLCJleHAiOjE2MjY0Mjk4NzY5MDIsInVzciI6IjE4NDEwMDczMTgxIn0.J2HmMdL4ZCQXxTOeOeihriw4Z-AyFYvk-waEXKHWmgM',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Origin': 'http://dztsl.lexue.com',
                    'Referer': 'http://dztsl.lexue.com/mavinSales/',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9'
                 }
        data = {"name": f"{self.faker.name()}",
                "nickname": "",
                "phone": f"{self.faker.phone_number()}",  # 手机号
                "sex": True,
                "birthday": f"{self.birthday}",
                "status": 0,
                "tag": "1级",
                "stage_id": 4805,
                "school": "这是学校名字",
                "grade": "初一",
                "division": "理科",
                "second_phone": f"{self.faker.phone_number()}",  # 第二手机号
                "score_before": "99",
                "rank_before": "10",
                "channel_tag": f"{self.faker.address()}",  # 来源
                "community": f"{self.community}",  # 地址
                "lexue_id": "95841678",  # 乐学号
                "is_valid": True,  # 有效性
                "customized_tag": "[\"高三数学\"]",  # 标签
                "salesList": "[{\"label\":\"宗树仁\",\"value\":2127}]",  # 销售
                "teachersList": "[{\"value\":2127,\"label\":\"宗树仁\"}]"}  # 教师
        # res = requests.post(url=url, headers=headers, data=data)
        print(data)
if __name__ == '__main__':
    NewXueyuan().create()