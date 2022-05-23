a=int(input())
b=list(map(int,input().split()))
c=a/2
f=int(c)
d,e=0,0
for i in b:
    if i<=f:
        d+=i
    else:
        e+=i
print(d)
print(e)