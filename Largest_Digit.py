a=int(input())
b=0
c=[]
while a:
    b=a%10
    a=a//10
    c.append(b)
print(max(c))
    