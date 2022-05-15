a=int(input())
b=list(map(int,input().split()))
c=0
d=len(b)
for i in b:
    if i<=1:
        c+=1
if c==d:
   print("True")
else:
    print("False")