def find(a,e):
	b=[]
	c,d=0,0
	for i in a:
		d=a.count(i)
		if d==e:
			if i in b:
				continue
			else:
				b.append(i)
	return b
a=int(input())
b=list(map(int,input().split()))
e=int(input())
c=find(b,e)
if len(c)!=0:
	print(*c)
else:
	print(-1)