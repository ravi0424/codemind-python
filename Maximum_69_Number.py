num=int(input())
num=[x for x in str(num)]
for i in range(len(num)):
    if num[i]=="6":
        num[i]="9"
        break
print("".join(num))