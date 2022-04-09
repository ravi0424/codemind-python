a=int(input())
s=0
p=1
while a:
    b=a%10
    a=a//10
    s+=b
    p=p*b
if (s==p):
    print("Spy Number")
else:
    print("Not Spy Number")
    