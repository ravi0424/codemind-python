a=list(map(str,input().split()))
c=[]
d=0
for i in range(0,len(a)):
    if i%2==0:
        d=a[i][::-1]
        c.append(d)
    else:
        c.append(a[i])
print(*c)