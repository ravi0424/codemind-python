a=input()
b=str(a)
ow="aeiou"
Ow="AEIOU"
c=0
d=0
for i in ow:
	if i in b:
		c+=1
for  j in Ow:
		if j in b:
			d+=1
if c==5:
	print("True")
elif d==5:
	print("True")
else:
	print("False")