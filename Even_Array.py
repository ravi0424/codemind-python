def lit(a):
	b=len(a)
	c=0
	for i in a:
		if i%2==0:
			c+=1
	return c
a=int(input())
b=list(map(int,input().split()))
c=len(b)
d=lit(b)
if d==c:
	print("True")
else:
	print("False")