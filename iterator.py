mylist = [23,65,22,76,34,98,43]
it = iter(mylist)
while True:
    try:
        print(next(it))
    except StopIteration:
        break