t = int(input())

for _ in range(t):
    s, k, m = map(int, input().split())
    x = m % (2 * k)

    if x <= k:
        ans = s - x
    else:
        ans = s - (2 * k - x)

    print(max(0, ans))
