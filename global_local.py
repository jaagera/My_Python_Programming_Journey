
x = 5   # global variable
def f1():
    global x
    x = 15   # global variable updated
    y = 10   # local variable
    print("x=%d y=%d" % (x, y))

f1()
print(x)