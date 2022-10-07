def ispal(a):
    b=str(a)
    i,j=0,len(b)-1
    while i<j:
        if int(b[i])!=int(b[j]):
            return False
        i+=1
        j-=1
    return True
a=int(input())
b,c=a,a
while 1:
    c+=1
    if ispal(c):
        break
while 1:
    b-=1
    if ispal(b):
        break
if c-a<a-b:
    print(c)
elif c-a>a-b:
    print(b)
else:
    print(b,c)