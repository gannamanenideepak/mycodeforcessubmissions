from collections import Counter

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    c=Counter(a)

    ok=False
    for v in c.values():
        if v%2:
            ok=True
            break

    if ok:
        print("YES")
    else:
        print("NO")