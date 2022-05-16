a=int(input())
b=list(map(int,input().split()))
c=len(b)
d=0
e=0
for i in range(0,c):
	if b[i]%2==0 and i%2==0:
		d+=1
	if b[i]%2==0:
		e+=1
if d==e:
	print("True")
else:
	print("False")