n=int(input())
res=0
for i in range(n):
    s=input()
    if(s=="X++" or s=="++X"):
        res+=1
    elif(s=="X--" or s=="--X"):
        res-=1
print(res)