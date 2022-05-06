def perfect(a):
	b=0
	for i in range(1,a+1) :
			b=i*i
			if b==a:
				return True
	return False
a=int(input())
if perfect(a):
	print("True")
else:
	print("False")