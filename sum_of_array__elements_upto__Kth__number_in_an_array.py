a=int(input())
b=list(map(int,input().split()))
c=int(input())
s=0
for i in b:
    if i<=c:
        s+=i
print(s)