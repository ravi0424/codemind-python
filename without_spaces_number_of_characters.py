def remove(string):
    return "".join(string.split())
string = str(input())
b=remove(string)
print(len(b))