a=input()
b=list(a.split("."))
c=""
for i in range(len(b)-1):
    c+=b[i]
    c+="[.]"
c+=b[-1]
print(c)