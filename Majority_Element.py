a=int(input())
b=list(map(int,input().split()))
c=0
d=0
e=set(b)
for i in e:
    if b.count(i)>c:
        c=b.count(i)
        d=i
print(d)