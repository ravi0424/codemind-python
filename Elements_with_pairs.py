a=int(input())
b=list(map(int,input().split()))
c=[]
d=len(b)
for i in range(0,d):
    c.append(b[i])
if d%2!=0:
    c.append(0)
print(*c)