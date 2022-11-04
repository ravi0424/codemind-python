def factors(a):
    b=0
    for i in range(1,a+1):
        if a%i==0:
            b+=i
    return b
a=input()
b=list(a.split(","))
x=0
y=[]
for i in b:
    c=factors(int(i))
    if str(c) in b:
        x=1
        y.append(int(i))
y.sort()
if(x==0):
    print(-1)
else:
    print(*y)
        