def prime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc+=1
    return fc
a=int(input())
fc=prime(a)
if fc==1 or fc==2:
    print("prime")
else:
    print("not a prime")