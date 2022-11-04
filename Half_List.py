a=int(input())
b=list(map(int,input().split()))
c=b[:a//2]
d=b[(a//2):]
d.reverse()
e=d+c
print(*e)