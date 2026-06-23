n, m = map(int, input().split())
count = 0

a = 0
while a * a <= n:
    b = 0
    while b * b <= m:
        if a*a + b == n and a + b*b == m:
            count += 1
        b += 1
    a += 1

print(count)
