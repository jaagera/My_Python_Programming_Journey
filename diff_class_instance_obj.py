class test:
    x = 20
    def __init__(self, a, b):
        self.a=a #instance member argument
        self.b=b #instance member argument
    def show(self):
            print(self.a,self.b)
print(test.x) #class object
t1 = test(4,5) #instance object
t1.show()
#displaying instance variables directly
print(t1.a)
print(t1.b)