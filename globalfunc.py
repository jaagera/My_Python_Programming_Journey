#globals function returns dictionary
#you can use the globals() function to access or modify global variables 
#within a function or code block
x = 5   # global variable
def func():
    x = 10   # local variable
    d = globals()   # d is a dictionary
    print("local x=%d global x=%d" % (x, d['x']))

func()