def reverse(a):
	if a<0:
		b=abs(a)
	else:
		b=a
	c=str(b)
	d=10**(len(c)-1)
	rev,e,f=0,0,0
	while b:
		e=b%10
		b=b//10
		f=e*d
		d=d//10
		rev+=f
	return rev
a=int(input())
b=reverse(a)
c=-b
if a<0:
	print(c)
else:
	print(b)