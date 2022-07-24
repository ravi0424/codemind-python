def prime(a):
	b=0
	for i in range(1,a):
		if a%i==0:
			b+=1
	if b==1:
		return True
	return False
def np(a):
	b,c,d=a,0,0
	while b>c:
		b+=1
		if prime(b):
			c=b
	b=a
	while d<b:
		b-=1
		if prime(b):
			d=b
			break
	if c-a<a-d:
		return c-a
	else:
		return a-d
a=int(input())
if prime(a):
	print(0)
else:
	print(np(a))