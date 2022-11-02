a=int(input())
for i in range(a):
    b=int(input())
    e=str(b)
    t=0
    c=[]
    f=0
    while(b):
        t=b%10
        c.append(t)
        b=b//10
    for i in range(min(c),max(c)):
        if str(i) not in e:
            f+=1
    if f==0:
        print("YES")
    else:
        print("NO")
            