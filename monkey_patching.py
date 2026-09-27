class test:
    def __init__(self, x):
        self.a = x

    def get_data(self):
        print("send code to fetch data from database")

    def f1(self):
        self.get_data()

t1 = test(4)
print("Before Monkey patching\n")
t1.f1()

def get_new_data(self):
    print("Some code to fetch data from test data")

test.get_data = get_new_data
print("\nAfter Monkey Patching\n")
t1.f1()