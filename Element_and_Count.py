a=int(input())
b=list(map(int,input().split()))
d=[ ]
g=[]
e=0
for i in b:
	if i not in d:
		d.append(i)
for j in d:
	g.append(j)
	e=b.count(j)
	g.append(e)
print(*g)
