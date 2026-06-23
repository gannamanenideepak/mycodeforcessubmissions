a = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        s = a[i][j]
        if i > 0:
            s += a[i-1][j]
        if i < 2:
            s += a[i+1][j]
        if j > 0:
            s += a[i][j-1]
        if j < 2:
            s += a[i][j+1]

        if s % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()
