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
d,e=0,0
c=[]
for i in b:
    if prime(i):
        c.append(i)
d=sum(c)/len(c)
e="{:.2f}".format(d)
print(e)