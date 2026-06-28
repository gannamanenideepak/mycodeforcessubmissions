t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    pre=[0]*(n+1)
    for i in range(n):
        pre[i+1]=pre[i]+a[i]
    total=pre[n]
    for _ in range(q):
        l,r,k=map(int,input().split())
        seg=pre[r]-pre[l-1]
        new_sum=total-seg+k*(r-l+1)
        if(new_sum%2):
            print("YES")
        else:
            print("NO")