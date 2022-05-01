def fib(n):
    a=0
    b=1
    c=0
    while True:
        c=a+b
        a=b
        b=c
        if c==n:
            return True
        if c>n:
            return False
a=int(input())
if fib(a):
    print("True")
else:
    print("False")
        