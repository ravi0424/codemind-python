a=int(input())
b=list(map(int,input().split()))
c=[]
D=0
for i in range(0,len(b)):
    if b[i] in c:
        continue
    else:
        c.append(b[i])
print(sum(c))