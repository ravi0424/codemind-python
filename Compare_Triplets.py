a=list(map(int,input().split()))
b=list(map(int,input().split()))
g,l=0,0
for i in range(len(a)):
    if a[i]>b[i]:
        g+=1
    elif a[i]<b[i]:
        l+=1
print(g,l)