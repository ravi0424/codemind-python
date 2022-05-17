a=list(map(str,input().split()))
d=0
c=[]
for i in a:
    d=len(i)
    c.append(d)
print(min(c))