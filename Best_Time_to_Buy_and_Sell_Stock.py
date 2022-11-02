a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    for j in range(i+1,a):
        if b[i]<b[j]:
            c.append(abs(b[i]-b[j]))
if(len(c)==0):
    print(0)
else:
    c=sorted(c)
    print(c[-1])