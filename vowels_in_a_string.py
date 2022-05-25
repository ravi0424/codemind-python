c=input()
b=str(c)
f=input()
f=str(f)
for i in range(0,len(b)):
	if b[i]==f:
		print("True")
		print(i)
		break
if f not in b:
    print("False")