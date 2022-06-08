a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c in b:
	print(b.count(c))
else:
	print(0)