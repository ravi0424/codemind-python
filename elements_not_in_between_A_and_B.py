def count(b,c,d):
	e=[]
	for i in b:
		if i<c or i>d:
			e.append(i)
	if len(e)!=0:
			return e
	else:
		return False
a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=count(b,c,d)
if e:
	for i in e:
		print(i,end=" ")
else:
	print("-1")