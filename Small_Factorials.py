def fact(a):
	c=1
	for i in range (1,a+1):
		c*=i
	return c
t=int(input())
for i in range(t):
	a=int(input())
	print(fact(a))