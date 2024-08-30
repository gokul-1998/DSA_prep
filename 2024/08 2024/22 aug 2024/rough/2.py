# 0 1 1 2 3 5 8

def fib_recursion(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)

print(fib_recursion(6))