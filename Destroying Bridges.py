t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    for r in range(1, n + 1):
        if r * (n - r) <= k:
            print(r)
            break