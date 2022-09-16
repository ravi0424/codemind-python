a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=input()
    for i in range(c):
        v=d[0:c-i]
        v=v[::-1]
        z=d[c-i:]
        d=v+z
    print(d)