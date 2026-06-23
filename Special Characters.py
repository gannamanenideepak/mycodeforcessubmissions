t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2:
        print("NO")
    else:
        print("YES")

        s = ""
        ch = ord('A')

        for i in range(n // 2):
            s += chr(ch) * 2
            ch += 1

        print(s)