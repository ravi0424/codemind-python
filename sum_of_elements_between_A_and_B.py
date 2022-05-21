a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=0
for i in b:
    if i>=c and i<=d:
        e+=i
print(e)