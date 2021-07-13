

class MathMethod:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

class MathMethod_1(MathMethod):
    def divide(self):
        return self.a/self.b

    def add(self):
        return self.a + self.b + 10
