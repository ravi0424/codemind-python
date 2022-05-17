a=list(map(str,input().split()))
bv=[]
c=0
for i in a:
    c=len(i)
    bv.append(c)
print(max(bv))
