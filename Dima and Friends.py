n = int(input())
friends = list(map(int, input().split()))

S = sum(friends)
ans = 0

for d in range(1, 6):
    if (S + d) % (n + 1) != 1:
        ans += 1

print(ans)
