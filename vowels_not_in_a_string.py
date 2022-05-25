c=input()
b=str(c)
z="aeiou"
g=[]
for i in z:
	if i not in b:
	    g.append(i)
if len(g)!=0:
    print(*g)
else:
    print(0)