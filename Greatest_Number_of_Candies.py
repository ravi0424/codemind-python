a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=[]
for i in b:
    if(i+c)>=max(b):
        d.append("True")
    else:
        d.append("False")
print(*d)