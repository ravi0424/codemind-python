def find(a):
	b=[]
	c,d=0,0
	for i in a:
		c=i
		d=a.count(i)
		if d==c:
			if i in b:
				continue
			else:
				b.append(i)
	return b
a=int(input())
b=list(map(int,input().split()))
c=find(b)
if len(c)!=0:
	d,e=max(c),min(c)
	print(e,d,end=" ")
else:
	print(-1)