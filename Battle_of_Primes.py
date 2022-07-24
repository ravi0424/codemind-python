def prime(a):
	b=0
	for i in range(1,a):
		if a%i==0:
			b+=1
	if b==1:
		return True
	return False
a=int(input())
b=int(input())
c=0
while c<=a+b:
	c+=1
	if prime(c+a+b):
		break
print(c)