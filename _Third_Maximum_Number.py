a=int(input())
b=list(map(int,input().split()))
c=set(b)
d=sorted(c)
if len(d)==1:
    print(d[0])
elif len(d)==2:
    print(d[1])
else:
    print(d[-3])