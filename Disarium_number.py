a=int(input())
f=a
b=str(a)
i=len(b)
c,d,e=0,0,0
while a:
	c=a%10
	a=a//10
	d=c**i
	i-=1
	e+=d
if e==f:
	print("True")
else:
	print("False")
	