def sum(a):
	s=0
	for i in range(1,a):
		if a%i==0:
			s+=i
	return s
a=int(input())
b=int(input())
if sum(a)==b and sum(b)==a:
	print("Amicable")
else:
	print("Not Amicable")