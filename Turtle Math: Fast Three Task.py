t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    s=sum(lis)
    rem=s%3
    if rem == 0:
        print(0)
        continue
    cnt1 = 0
    cnt2 = 0
    for x in lis:
        if x % 3 == 1:
            cnt1 += 1
        elif x % 3 == 2:
            cnt2 += 1
    ans = float('inf')
    if rem == 1:
        if cnt1 > 0:
            ans = min(ans, 1) 
        ans = min(ans, 2) 
    else:
        if cnt2 > 0:
            ans = min(ans, 1) 
        ans = min(ans, 1)
    print(ans)