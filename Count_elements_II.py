a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=set(c)
f=set(d)
j=0
for i in e:
	if i not in d:
		j+=1
for k in f:
	if k not in c:
		j+=1
print(j)