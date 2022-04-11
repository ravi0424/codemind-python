n=int(input())
b=1
c=0
for i in range(1,n):
		d=n%b
		if n%b==0:
			c=c+b
		b+=1
if c==n:
	print("True")
else:
	print("False")