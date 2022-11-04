a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
t=int(input())
c=0
for i in b:
    if(i<=t):
        c+=1
    else:
        c+=2
print(c)