n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

count = 0

for x, y in points:
    left = right = up = down = False

    for x2, y2 in points:
        if x2 == x and y2 > y:
            up = True
        elif x2 == x and y2 < y:
            down = True
        elif y2 == y and x2 > x:
            right = True
        elif y2 == y and x2 < x:
            left = True

    if left and right and up and down:
        count += 1

print(count)
