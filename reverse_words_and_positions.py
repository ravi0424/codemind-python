a=list(map(str,input().split()))
b=str(a)
c=a[::-1]
d=[]
e=0
for i in range(0,len(c)):
    e=c[i][::-1]
    d.append(e)
print(*d)
