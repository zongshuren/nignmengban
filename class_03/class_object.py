import sys
sys.setrecursionlimit(1000000)
class QA:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hight = 180
        pass

    def qa_faction(self):
        print('晚上好啊{0},{1},{2}'.format(self.name, self.age, self.hight))
        self.test_01()

    def test_01(self):
        # 函数内可以互相调用
        self.qa_faction()
    # @classmethod    # 类方法
    # def swiming(cls):
    #     print('i can you yong')
    #
    # @staticmethod    # 静态方法
    # def swiming2():
    #     print('i cag')


qa = QA('maomao', 19) #实例 隐式传递
qa.test_01()
print(qa.i)

# QA.qa_faction(qa) #实例 显示传递 不建议使用
# QA.swiming()
# qa.swiming()
