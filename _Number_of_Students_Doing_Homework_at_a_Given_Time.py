a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e=int(input())
co=0
for i in range(a):
    if b[i]<=e and d[i]>=e:
        co+=1
print(co)
        