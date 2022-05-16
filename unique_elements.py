def find(a):
	c=[]
	for i in b:
		if i in c:
			continue
		else:
			c.append(i)
	return c
a=int(input())
b=list(map(int,input().split()))
c=find(b)
for i in c:
	print(i,end=" ")