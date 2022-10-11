a=int(input())
b=list(map(int,input().split()))
c=min(b)
i=c
while i>0:
	l=0
	for j in b:
		if j%i==0:
			l+=1
		else:
			break
	if l!=len(b):
		i-=1
	else:
		break
print(i)