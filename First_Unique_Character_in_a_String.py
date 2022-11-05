a=input()
b=0
for i in a:
    if a.count(i)==1:
        print(a.index(i))
        break
else:
    print(-1)