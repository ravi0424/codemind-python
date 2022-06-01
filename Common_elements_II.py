def find(b):
	a=[]
	for i in b:
		if i not in a:
			a.append(i)
	return a
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=find(c)
f=find(d)
k=[]
for i in e:
	if i not in f:
		k.append(i)
for j in f:
	if j not in e:
		k.append(j)
z=find(k)
print(*z)