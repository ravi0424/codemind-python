a=int(input())
b=list(map(int,input().split()))
s=""
for i in b:
    s+=str(i)
s=int(s)+1
s=str(s)
r=[int(x) for x in s]
print(*r)