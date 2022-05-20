a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
    if i in c:
        continue
    else:
        c.append(i)
for j in c:
    if j%2:
        d+=1
print(d)