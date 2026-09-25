def f1(a, b):
    print("a=", a, ", b=", b)

f1(3, 5)          # positional argument
#f1(b=30, 5)      # syntax error (compile time error)
f1(30, b=4)
#f1(2, a=10)      # type error: multiple values of a (run time error)
f1(a=23, b=34)    # keyword argument