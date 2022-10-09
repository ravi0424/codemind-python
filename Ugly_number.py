def ugly(a):
    if a==1:
        return 1
    if a<=0:
        return 0
    if a%2==0:
        return ugly(a//2)
    if a%3==0:
        return ugly(a//3)
    if a%5==0:
        return ugly(a//5)
    return 0
a=int(input())
if ugly(a):
    print("Ugly Number")
else:
    print("Not Ugly Number")