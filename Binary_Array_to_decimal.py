a=int(input())
b=list(map(int,input().split()))
k=1
for i in range(1,len(b)):
	k=k+k	
d=len(b)
c=0
e=0
for i in range(0,d):
	c=b[i]*k
	e+=c
	k=k//2	
print(e)


	
	