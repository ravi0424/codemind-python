c=input()
b=str(c)
f="aeiouAEIOU"
d=0
for i in b:
	if i in f:
		d+=1
if d!=0:
	print(d)
else:
	print(0)