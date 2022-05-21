a=int(input())
b=list(map(int,input().split()))
c=[]
d,e=map(int,input().split())
for i in b:
	if i>=d and i<=e:
		c.append(i)
if len(c)!=0:
    print(*c)
else:
    print(-1)