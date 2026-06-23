n = int(input())
a = list(map(int, input().split()))

mn = min(a)

if a.count(mn) > 1:
    print("Still Rozdil")
else:
    print(a.index(mn) + 1)   # +1 for 1-based indexing
