def count(a):
    b=0
    for i in range(1,len(a)-1):
        if a[i]%2 and a[i+1]%2==0 and a[i-1]%2==0:
            b+=1
    return b
a=int(input())
b=list(map(int,input().split()))
print(count(b))