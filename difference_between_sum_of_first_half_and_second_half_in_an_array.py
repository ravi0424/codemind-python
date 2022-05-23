a=int(input())
b=list(map(int,input().split()))
c=a/2
d=int(c)
e,f=0,0
for i in b:
    if i<=d:
        e+=i
    else:
        f+=i
if e>f:
    print(e-f)
else:
    print(f-e)