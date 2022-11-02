a=int(input())
e=int(input())
b=[]
for i in range(a):
    c=list(map(int,input().split()))
    b.append(c)
d=0
for i in b:
    d+=sum(i)
print(d)