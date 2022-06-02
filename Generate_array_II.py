a=int(input())
b=list(map(int,input().split()))
c,d=[],[]
for i in range(0,len(b)):
	if i%2:
		c.append(b[i])
	else:
		d.append(b[i])
z=[]
for j in range(len(d)):
	for k in range(c[j]):
		z.append(d[j])
print(*z)