a=int(input())
b=list(map(int,input().split()))
c=set(b)
for i in c:
    if b.count(i)>=2:
        print(i)
        break