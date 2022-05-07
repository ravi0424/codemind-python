def ab(a):
	b=0
	for i in range(1,a):
		if a%i==0:
			b+=i
	return b
a=int(input())
b=ab(a)
if b>a:
	print("True")
else:
	print("False")
	