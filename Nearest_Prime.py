def prime(a):
    b=0
    for i in range(1,a):
        if a%i==0:
            b+=1
    if b==1:
        return True
    return False
def np(a):
    b,c,d=a,0,0
    while b>c:
        b+=1
        if prime(b):
            c=b
    b=a
    while d<b:
        b-=1
        if prime(b):
            d=b
            break
    if c-a<a-d:
        return c
    else:
        return d
a=int(input())
b=[]
for i in range(a):
    c=int(input())
    if prime(c):
        b.append(c)
    else:
        b.append(np(c))
for j in b:
    print(j)