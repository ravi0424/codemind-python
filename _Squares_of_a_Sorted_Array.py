a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    c.append(i**2)
c=sorted(c)
print(*c)