t=int(input())

v="aeiou"

for _ in range(t):
    n=int(input())

    q=n//5
    r=n%5

    ans=""

    for i in range(5):
        ans+=v[i]*(q+(i<r))

    print(ans)