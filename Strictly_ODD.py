def strictlyodd(a):
	c=len(b)
	d=0
	e=0
	for i in range(0,c):
		if b[i]%2 and i%2:
			d+=1
		if b[i]%2:
			e+=1
	if d==e:
		return True
	return False
a=int(input())
b=list(map(int,input().split()))
if strictlyodd(b):
	print("True")
else:
	print("False")