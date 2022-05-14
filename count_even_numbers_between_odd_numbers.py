a=int(input())
b=list(map(int,input().split()))
c=len(b)
d=0
for i in range(1,len(b)-1):
	if b[i]%2==0 and b[i+1]%2 and b[i-1]%2:
		d+=1
print(d)