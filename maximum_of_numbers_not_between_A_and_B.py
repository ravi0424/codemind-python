def count(b,c,d):
	e=[]
	f=0
	for i in b:
		if i<c or i>d:
			e.append(i)
	if len(e)!=0:
			f=max(e)
			return f
	else:
		return False
a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=count(b,c,d)
if e:
	print(e)
else:
	print("-1")