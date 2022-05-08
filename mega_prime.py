def prime(a):
	c=0
	for i in range(1,a+1):
		if a%i==0:
			c+=1
	if c==2:
		return True
	return False
a=int(input())
c=str(a)
d=0
b=0
if prime(a):
	while a:
		b=a%10
		a=a//10
		if prime(b):
			d+=1
		if d==len(c):
			print("Mega Prime")
			break
	else:
		print("Not Mega Prime")
else:
	print("Not Mega Prime")