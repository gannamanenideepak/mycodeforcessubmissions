t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    s=sum(a)
    r=s%n

    print(r*(n-r))