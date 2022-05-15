def count(a):
    b,c=0,0
    for i in a:
        b+=i
    c=b//len(a)
    return c
a=int(input())
b=list(map(int,input().split()))
c=count(b)
d=0
for i in b:
    if i>=c:
        d+=1
print(d)