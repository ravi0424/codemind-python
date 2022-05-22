a=int(input())
b=list(map(int,input().split()))
d,s=0,[]
for i in range(0,len(b)):
    if b[i]%2:
        d=i
        break
for j in range(0,d):
    s.append(b[j])
print(sum(s))