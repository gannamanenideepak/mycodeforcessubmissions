n = int(input())
a = list(map(int, input().split()))

min_diff = float('inf')
x, y = 0, 0

# check adjacent pairs
for i in range(n - 1):
    diff = abs(a[i] - a[i + 1])
    if diff < min_diff:
        min_diff = diff
        x, y = i + 1, i + 2  # 1-based index

# check circular pair (last, first)
diff = abs(a[n - 1] - a[0])
if diff < min_diff:
    x, y = n, 1

print(x, y)