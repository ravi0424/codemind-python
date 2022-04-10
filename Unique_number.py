a=int(input())
b=[]
c=str(a)
c=len(c)
while a:
	d=a%10
	a=a//10
	b.append(d)
e=set(b)
f=len(e)
if c==f:
	print("Unique Number")
else:
	print("Not Unique Number")