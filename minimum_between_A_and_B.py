a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
for i in b:
	if i>=c and i<=d:
		e.append(i)
if len(e)!=0:
    print(min(e))
else:
    print(-1)