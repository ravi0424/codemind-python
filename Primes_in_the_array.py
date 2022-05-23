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
c=0
for i in b:
    if prime(i):
        c+=1
print(c)