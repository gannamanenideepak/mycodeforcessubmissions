t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    z = s.count('0')
    print(s[:z].count('1'))