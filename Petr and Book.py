n = int(input())
a = list(map(int, input().split()))

day = 0  # 0 = Monday

while True:
    n -= a[day]
    if n <= 0:
        print(day + 1)  # Convert to 1-based index
        break
    day = (day + 1) % 7