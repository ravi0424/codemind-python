def palindrome(a):
    f=a
    e=str(a)
    b,d,rev=0,0,0
    c=10**(len(e)-1)
    while a:
        b=a%10
        a=a//10
        d=b*c
        c=c//10
        rev+=d
    if rev==f:
        return True
    return False
a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in b:
    d=i
    if palindrome(d):
        c+=1
print(c)