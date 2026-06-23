a = input().strip()
b = input().strip()
c = input().strip()

combined = a + b

if sorted(combined) == sorted(c):
    print("YES")
else:
    print("NO")

