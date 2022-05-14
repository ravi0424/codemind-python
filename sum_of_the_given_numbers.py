
m=int(input())
a=[]
for n in range(0, m):	
	a.append(list(map(int,input().split())))
for g in a:
	print (g[0]+g[1])
