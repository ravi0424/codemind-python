def pro(a):
	b=0
	for i in range(-1,a):
		b=i*i+i
		if a==b:
			return True
	return False
a=int(input())
if pro(a):
	print("YES")
else:
	print("NO")
	