def largestInColumn(mat, rows, cols):
    for i in range(cols):
        maxm = mat[0][i]
        for j in range(rows):
            if mat[j][i] > maxm:
                maxm = mat[j][i]
        print(maxm)
 
a,b=map(int,input().split())
c=[]
for i in range(a):
    d=list(map(int,input().split()))
    c.append(d)
largestInColumn(c,a,b)