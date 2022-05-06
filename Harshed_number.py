def Harshed(a):
	b,c=0,0
	while a:
		b=a%10
		a=a//10
		c+=b
	return c
a=int(input())
d=Harshed(a)
if a%d==0:
	print("True")
else:
	print("False")
	