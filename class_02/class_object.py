class TestResult(object):
    height = 175
    weight = 130
    money = '500万'
    def __init__(self, name, score):
        self.name = name
        self.score = score


    # 类函数

    def cooking(self):
        print(self.name)
        print('做饭')


    def earn(self):
        print('月薪3w')


bf = TestResult('zhangsan', 'lisi')
bf.name= 1