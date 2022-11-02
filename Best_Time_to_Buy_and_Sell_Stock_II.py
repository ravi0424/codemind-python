a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(len(b)-1):
    if b[i]<b[i+1]:
        c.append(abs(b[i]-b[i+1]))
print(sum(c))