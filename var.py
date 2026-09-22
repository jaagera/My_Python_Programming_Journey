class Test:
    def __init__(self):
        self.a = 5
    def f1(self):
        self.b = 10
t1 = Test()
t2 = Test()
t1.f1()
t1.c = 15
print(t1.__dict__)
print(t2.__dict__)