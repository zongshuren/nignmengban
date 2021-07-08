class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        return self.first_name, self.last_name

    def greet_user(self):
        for i in self.describe_user():
            print('{0}晚上好'.format(i))


class User2():

    def greet_user(self):  # 子类里边与父类名字重复的时候，就叫重写

        print('hello')

    def new_user(self):   # 父类里没有的叫做拓展
        # 子类里边调用父类的函数，可以直接调用
        # self.describe_user()
        print('父类里没有的函数')

class User3(User, User2):

    def jump(self):

        print(self.last_name+'可以单膝跳跃')


t1 = User3('1, 2', '15')
t1.jump()