a=int(input())
b=list(map(int,input().split()))
c=0
d=[]
n=0
for i in b:
    if i==1:
        c+=1
    else:
        d.append(c)
        c=0
d.append(c)
print(max(d))
        