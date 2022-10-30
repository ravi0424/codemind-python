def ispalin(a):
    b=str(a)
    i,j=0,len(b)-1
    while i<j:
        if int(b[i])!=int(b[j]):
            return 0;
        i+=1
        j-=1
    return 1;
a=int(input())
while 1:
    b=str(a)
    c=b[::-1]
    a+=int(c)
    if(ispalin(a)):
        break
print(a)