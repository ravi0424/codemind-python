a=int(input())
s1,s2=0,0
i1,i2=0,a-1
for i in range(a):
    c=list(map(int,input().split()))
    s1+=c[i1]
    s2+=c[i2]
    i1+=1
    i2-=1
st1="Principal Diagonal:"
st2="Secondary Diagonal:"
st1+=str(s1)
st2+=str(s2)
print(st1)
print(st2)