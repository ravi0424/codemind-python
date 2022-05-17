a=list(map(str,input().split()))
c=[]
b=0
for i in range(0,len(a)):
    b=a[i][::-1]
    c.append(b)
print(*c)
             