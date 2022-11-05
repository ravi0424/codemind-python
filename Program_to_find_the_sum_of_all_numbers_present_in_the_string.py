a=input()
s=0
d="123456789"
for i in a:
    if i in d:
        s+=int(i)
print(s)