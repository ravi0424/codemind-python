def prime(a):
    b=0
    for i in range(1,a):
        if a%i==0:
            b+=1
    if b==1:
        return True
    return False
a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=0
for i in b:
    if i<=c:
        if prime(i):
            d+=1
print(d)