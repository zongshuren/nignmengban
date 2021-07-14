

class MathMethod:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        return self.a - self.b

class MathMethod_1(MathMethod):
    def divide(self):  # 拓展
        return self.a/self.b

    def add(self):
        super(MathMethod_1, self).add()  # 超继承
        print(self.a + self.b + 10)

if __name__ == '__main__':
    MathMethod_1(1, 2).add()
