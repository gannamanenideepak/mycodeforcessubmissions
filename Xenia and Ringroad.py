n, m = map(int, input().split())
a = list(map(int, input().split()))

curr = 1
time = 0

for target in a:
    if target >= curr:
        time += target - curr
    else:
        time += (n - curr) + target
    curr = target

print(time)
