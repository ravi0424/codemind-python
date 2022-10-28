a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)-2):
    if b[i]%2==0 and b[i+2]%2 or b[i]%2 and b[i+2]%2==0:
        c+=1
if b[-2]%2==0 and b[0]%2 or b[0]%2 and b[-2]%2==0:
    c+=1
if b[-1]%2==0 and b[1]%2 or b[-1]%2 and b[1]%2==0:
    c+=1
print(c)