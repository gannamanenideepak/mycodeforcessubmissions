t=int(input())
for i in range(t):
    n=int(input())
    if(n<2020):
        print("NO")
    else:
        q=n//2020
        r=n%2020
        if(q>=r):
            print("YES")
        else:
            print("NO")
    