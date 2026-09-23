def welcome(fx):
    def mfx(*t, **d):
        print("Before hello function")
        fx(*t, **d)   #*args to take arguments as tuple, **kwargs to take arguments
        print("Thanks for using the function")
    return mfx

#decorator function without arguments
@welcome
def hello():
    print("Hello !")

#decorator function with arguments
@welcome
def add(a, b):
    print(a+b)

hello()
add(1, 3)