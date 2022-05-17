a=list(map(str,input().split()))
b=a[::-1]
c=[]
d=0
for i in range(0,len(b)):
    d=b[i][::-1]
    c.append(d)
print(*c)