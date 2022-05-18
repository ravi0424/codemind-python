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
d,e,f=0,0,0
if len(c)!=0:
	for i in c:
		d+=i
		e+=1
	f=d/e
	h="{:.2f}".format(f)
	print(h)
else:
    print(-1)