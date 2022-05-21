def split(a):
	b=0
	c=0
	while a:
		b=a%10
		a=a//10
		c+=b
	return c
a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
	c+=split(i)
print(c)