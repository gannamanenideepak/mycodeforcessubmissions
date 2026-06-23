mat=[]
for i in range(5):
    a,b,c,d,e=map(int,input().split())
    mat.append([a,b,c,d,e])
row=-1
col=-1
for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            row=i
            col=j
            break
res=0
print(abs(2-row)+abs(2-col))
            
        