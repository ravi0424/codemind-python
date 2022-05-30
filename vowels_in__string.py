a=input()
ow="aeiouAEIOU"
c=[]
for i in a:
	if i in ow:
		if i not in c:
			c.append(i)
if len(c)!=0:
	print(*c)
else:
	print("-1")