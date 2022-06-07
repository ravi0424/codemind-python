def splt(a):
	b,c=0,0
	while a:
		b=a%10
		a=a//10
		c+=b*b
	return c
a=int(input())
b=splt(a)
while b>=10:
	b=splt(b)
if b==1:
	print("True")
else:
	print("False")