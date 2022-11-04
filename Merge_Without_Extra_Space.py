a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    e=list(map(int,input().split()))
    f=d+e
    f.sort()
    print(*f)