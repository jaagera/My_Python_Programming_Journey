class myclass:
    a = 5  # Static variable (Created immediately)

    def __init__(self):
        self.x = 10  # Instance variable
        y = 4  # Local variable (dies when __init__ ends)
        myclass.b = 34  # Static variable (Created when object is made)
        myclass.g = 11  # Static variable (Created when object is made)

    # 1. Regular Instance Method
    def f1(self):
        myclass.c = 65  # Static variable (Created when f1() is called)

    # 2. Static Method (Does not take self or cls)
    @staticmethod
    def f2():  # Removed 'self' because static methods don't track instances
        myclass.d = 66  # Static variable (Created when f2() is called)

    # 3. Class Method (Takes 'cls' representing the class)
    @classmethod
    def f3(cls):
        cls.e = 15  # Static variable (Created when f3() is called)
        myclass.f = 53  # Static variable (Same as above)
