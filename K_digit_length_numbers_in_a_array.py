a,b=map(int,input().split())
c=list(map(str,input().split()))
d=0
for i in c:
	i=int(i)
	if i<0:
		i=i//-1
	i=str(i)
	if b==len(i):
		d+=1
print(d)