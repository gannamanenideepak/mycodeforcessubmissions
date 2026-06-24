t=int(input())
for _ in range(t):
    n=int(input())
    low=1
    high=10**9
    neq=[]
    for _ in range(n):
        a,x=map(int,input().split())
        if(a==1):
            low=max(low,x)
        elif(a==2):
            high=min(high,x)
        else:
            neq.append(x)

    if(low>high):
        print(0)
        continue
    ans=high-low+1
    for x in neq:
        if(low<=x<=high):
            ans-=1
    print(ans)