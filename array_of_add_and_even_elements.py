a=int(input())
b=list(map(int,input().split()))
for i in b:
    if i%2:
        print(i,end=" ")
for j in b:
    if j%2==0:
        print(j,end=" ")