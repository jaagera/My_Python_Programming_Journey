f = lambda n : 1 if n==0 else n*f(n-1)
print(f(100))
#120
num = int(input("Enter a number:"))
#7
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num==0:
        print("The factorial of 0 is 1")
else:
        for i in range(1, num +1):
            factorial = factorial*1
        print(f"The factorial of {num} is, factorial")
        #5040