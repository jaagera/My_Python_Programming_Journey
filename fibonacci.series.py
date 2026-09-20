fib = [0,1]
#range starts from 0 by default
n=5
for i in range(n):
    fib.append(fib[-1] + fib[-2])
#convertin the list of integers to string 
print('-'.join(str(e) for e in fib))