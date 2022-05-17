a=int(input())
b=list(map(str,input().split()))
c=[]
d=[]
for i in b:
    c1=len(i)
    c+=[c1]
m=max(c)
for i in b:
    if len(i)==max(c):
        d.append(i)
print(*d)
