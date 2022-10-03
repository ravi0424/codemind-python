a=input().split()
b=[]
for i in a:
    b.append(ord(max(i))-ord(min(i)))
print(*b)