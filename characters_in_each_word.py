a=list(map(str,input().split()))
b=[]
c=0
for i in a:
    c=len(i)
    b.append(c)
print(*b)