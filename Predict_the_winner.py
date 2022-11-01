a=int(input())
b=list(map(int,input().split()))
x,y=0,0
i,j=0,1
while j!=a and i!=a:
    x+=b[i]
    y+=b[j]
    i+=2
    j+=2
c=abs(x-y)
if (c%4==0):
    print("X")
else:
    print("Y")