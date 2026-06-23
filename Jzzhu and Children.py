import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

max_rounds = -1
answer = -1

for i in range(n):
    rounds = (a[i] + m - 1) // m  # ceil division
    if rounds >= max_rounds:
        max_rounds = rounds
        answer = i + 1  # 1-based index

print(answer)
