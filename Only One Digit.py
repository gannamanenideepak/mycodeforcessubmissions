t=int(input())
for i in range(t):
    x=str(int(input()))
    lis=list(x)
    for i in range(len(lis)):
        lis[i]=int(lis[i])
    print(min(lis))
