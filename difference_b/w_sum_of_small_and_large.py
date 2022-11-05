a=input()
b=list(a.split(" "))
mi,ma=0,0
for i in b:
    m=min(i)
    mi+=ord(m)
    k=max(i)
    ma+=ord(k)
print(ma-mi)
