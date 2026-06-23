t = int(input())

for _ in range(t):
    n = int(input())
    r = n % 4

    if r == 0:
        print(0)
    elif r == 1:
        print(1)
    elif r == 2:
        print(1)
    else:  # r == 3
        print(2)
